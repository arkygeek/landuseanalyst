"""``la:catchment`` — headless site-catchment analysis from a scenario file (June 2026 algorithm, re-based on the dock engine)."""

import os
import shutil
import time

from qgis.core import (
    QgsCoordinateTransformContext, QgsProcessing, QgsProcessingContext, QgsProcessingException,
    QgsProcessingParameterBoolean, QgsProcessingParameterFile, QgsProcessingParameterFolderDestination,
    QgsProcessingParameterNumber, QgsProcessingParameterPoint, QgsProcessingParameterRasterDestination,
    QgsProcessingParameterRasterLayer, QgsProcessingParameterVectorLayer, QgsProcessingUtils, QgsProject,
    QgsVectorFileWriter,
)

from la.processing.labasealgorithm import LaBaseAlgorithm


class LaCatchmentAlgorithm(LaBaseAlgorithm):
    DEM = "INPUT_DEM"
    SETTLEMENT = "INPUT_SETTLEMENT"
    SCENARIO = "INPUT_PROFILE"
    COMMON_CROP = "INPUT_COMMON_CROP"
    COMMON_GRAZING = "INPUT_COMMON_GRAZING"
    BARRIERS = "INPUT_BARRIERS"
    APPLY_SLOPE = "APPLY_SLOPE"
    SPLIT_FALLOW = "SPLIT_FALLOW"
    WINDOW = "WINDOW_PIXELS"
    OUTPUT_COST = "OUTPUT_COST"
    OUTPUT_FOLDER = "OUTPUT_FOLDER"

    GROUP = "Catchment"
    GROUP_ID = "catchment"

    def name(self) -> str:
        return "catchment"

    def displayName(self) -> str:
        return self.tr("Site catchment analysis")

    def shortHelpString(self) -> str:
        return self.tr(
            "Runs the Landuse Analyst catchment model without the docks: a scenario file "
            "(*.lascenario.json or the unified XML in la/thesis_scenarios/), a DEM and a settlement "
            "point. The diet model gives every crop and animal a land target; the walking-time search "
            "then finds that land around the site, honouring the profiles' slope bands, an optional "
            "barrier layer and the sown/fallow split. Writes the cost surface and one mask per item.")

    def initAlgorithm(self, theConfig=None):
        self.addParameter(QgsProcessingParameterRasterLayer(self.DEM, self.tr("DEM")))
        self.addParameter(QgsProcessingParameterPoint(self.SETTLEMENT, self.tr("Settlement location")))
        self.addParameter(QgsProcessingParameterFile(
            self.SCENARIO, self.tr("Scenario file (*.lascenario.json or *.xml)"),
            behavior=QgsProcessingParameterFile.File, fileFilter="Scenarios (*.lascenario.json *.json *.xml)"))
        self.addParameter(QgsProcessingParameterRasterLayer(
            self.COMMON_CROP, self.tr("Common crop suitability (optional)"), optional=True))
        self.addParameter(QgsProcessingParameterRasterLayer(
            self.COMMON_GRAZING, self.tr("Common grazing suitability (optional)"), optional=True))
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.BARRIERS, self.tr("Barriers: rivers / lakes / walls (optional)"),
            [QgsProcessing.TypeVectorLine, QgsProcessing.TypeVectorPolygon], optional=True))
        self.addParameter(QgsProcessingParameterBoolean(
            self.APPLY_SLOPE, self.tr("Apply each item's preferred slope band"), defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            self.SPLIT_FALLOW, self.tr("Split cropland into sown and fallow masks"), defaultValue=True))
        self.addParameter(QgsProcessingParameterNumber(
            self.WINDOW, self.tr("Working window in cells (0 = size from the targets)"),
            QgsProcessingParameterNumber.Integer, defaultValue=0, minValue=0, maxValue=1500))
        self.addParameter(QgsProcessingParameterRasterDestination(
            self.OUTPUT_COST, self.tr("Cost surface"), optional=True, createByDefault=True))
        self.addParameter(QgsProcessingParameterFolderDestination(
            self.OUTPUT_FOLDER, self.tr("Folder for the catchment masks"), optional=True))

    def processAlgorithm(self, theParameters, theContext, theFeedback):
        from la.lib import lascenarioio
        from la.lib.lacatchment import DistanceMethod, LaCatchment, LaCatchmentInputs, LaGisInputError
        from la.lib.lagrass import LaGrass
        from la.lib.lautils import LaUtils

        myDem = self.parameterAsRasterLayer(theParameters, self.DEM, theContext)
        if myDem is None:
            raise QgsProcessingException(self.tr("Invalid DEM layer."))
        myPoint = self.parameterAsPoint(theParameters, self.SETTLEMENT, theContext, myDem.crs())
        myScenarioPath = self.parameterAsFile(theParameters, self.SCENARIO, theContext)
        if not myScenarioPath or not os.path.exists(myScenarioPath):
            raise QgsProcessingException(self.tr(f"Scenario file not found: {myScenarioPath}"))
        myCropLayer = self.parameterAsRasterLayer(theParameters, self.COMMON_CROP, theContext)
        myGrazingLayer = self.parameterAsRasterLayer(theParameters, self.COMMON_GRAZING, theContext)
        myBarrierLayer = self.parameterAsVectorLayer(theParameters, self.BARRIERS, theContext)

        myScratch = theContext.temporaryFolder() or QgsProcessingUtils.tempFolder()
        myRunDir = os.path.join(myScratch, "landuseanalyst", f"run_{int(time.time())}")
        os.makedirs(myRunDir, exist_ok=True)

        # 1. Scenario → model + selections
        LaUtils.clearRegistries()
        if lascenarioio.isXmlScenario(myScenarioPath):
            myModel, myCrops, myAnimals, _ = lascenarioio.loadXmlScenario(myScenarioPath)
        else:
            myModel, myCrops, myAnimals, _ = lascenarioio.fromDict(lascenarioio.loadFile(myScenarioPath))
        myModel.mCropsMap, myModel.mAnimalsMap = dict(myCrops), dict(myAnimals)
        myModel.mEasting, myModel.mNorthing = float(myPoint.x()), float(myPoint.y())
        theFeedback.pushInfo(self.tr(f"Scenario '{myModel.mName}': {len(myCrops)} crops, {len(myAnimals)} animals"))

        # 2. Diet model
        if myModel.mIncludeDairy:
            myLabels = (myModel.doCalcsPlantsFirstIncludeDairy() if myModel.mBaseOnPlants
                        else myModel.doCalcsAnimalsFirstIncludeDairy())
        else:
            myLabels = (myModel.doCalcsPlantsFirstDairySeparate() if myModel.mBaseOnPlants
                        else myModel.doCalcsAnimalsFirstDairySeparate())
        myModel.mDietLabels = myLabels
        theFeedback.pushInfo(self.tr(
            f"Targets: {sum(myModel.mAreaTargetsCropsMap.values()):.1f} Ha crops, "
            f"{sum(myModel.mAreaTargetsAnimalsMap.values()):.1f} Ha grazing"))

        # 3. Barriers → GeoPackage the worker can read
        myBarriersPath = None
        if myBarrierLayer is not None:
            myBarriersPath = os.path.join(myRunDir, "barriers.gpkg")
            myOptions = QgsVectorFileWriter.SaveVectorOptions()
            myOptions.driverName = "GPKG"
            myError, myMessage, *_ = QgsVectorFileWriter.writeAsVectorFormatV3(
                myBarrierLayer, myBarriersPath, QgsCoordinateTransformContext(), myOptions)
            if myError != QgsVectorFileWriter.NoError:
                raise QgsProcessingException(self.tr(f"Could not export the barrier layer: {myMessage}"))

        # 4. Layers must be resolvable by id inside LaCatchment
        myRegistered = []
        try:
            for myLayer in (myDem, myCropLayer, myGrazingLayer):
                if myLayer is not None and QgsProject.instance().mapLayer(myLayer.id()) is None:
                    QgsProject.instance().addMapLayer(myLayer, False)
                    myRegistered.append(myLayer)
            myGrass = LaGrass(myDem, myRunDir)
            myCatchment = LaCatchment(myGrass, thePrecisionPct=int(myModel.mPrecision or 5))
            myCatchment.logged.connect(theFeedback.pushInfo)
            myCatchment.progress.connect(
                lambda done, it, mx: theFeedback.setProgress(100.0 * it / mx if mx else 0.0))
            myWindow = self.parameterAsInt(theParameters, self.WINDOW, theContext)
            myInputs = LaCatchmentInputs(
                demLayerId=myDem.id(),
                commonCropLayerId=myCropLayer.id() if myCropLayer is not None else None,
                commonGrazingLayerId=myGrazingLayer.id() if myGrazingLayer is not None else None,
                method=DistanceMethod.Euclidean if myModel.mEuclideanDistance else DistanceMethod.WalkingTime,
                windowPixels=myWindow or None,
                applySlopeLimits=self.parameterAsBool(theParameters, self.APPLY_SLOPE, theContext),
                splitFallow=self.parameterAsBool(theParameters, self.SPLIT_FALLOW, theContext),
                barriersPath=myBarriersPath,
            )
            try:
                myResults = myCatchment.runCatchmentAnalysis(myModel, myInputs, theIsCanceledFn=theFeedback.isCanceled)
            except LaGisInputError as e:
                raise QgsProcessingException(str(e)) from e
        finally:
            for myLayer in myRegistered:
                QgsProject.instance().removeMapLayer(myLayer.id())

        # 5. Outputs
        myOutputs = {}
        myCostDestination = self.parameterAsOutputLayer(theParameters, self.OUTPUT_COST, theContext)
        if myCostDestination and myResults.costRasterPath and os.path.exists(myResults.costRasterPath):
            shutil.copyfile(myResults.costRasterPath, myCostDestination)
            myOutputs[self.OUTPUT_COST] = myCostDestination
        myFolder = self.parameterAsFileOutput(theParameters, self.OUTPUT_FOLDER, theContext) or myRunDir
        os.makedirs(myFolder, exist_ok=True)
        for myItem in myResults.items:
            if not myItem.outputPath or not os.path.exists(myItem.outputPath) or myItem.category == "total":
                continue
            myDestination = os.path.join(myFolder, os.path.basename(myItem.outputPath))
            if os.path.abspath(myDestination) != os.path.abspath(myItem.outputPath):
                shutil.copyfile(myItem.outputPath, myDestination)
            myLabel = f"{myItem.itemName} {myItem.category}".strip()
            theContext.addLayerToLoadOnCompletion(
                myDestination, QgsProcessingContext.LayerDetails(f"Catchment — {myLabel}", theContext.project(), self.OUTPUT_FOLDER))
            theFeedback.pushInfo(f"{myLabel}: {myItem.achievedHa:.1f} Ha / target {myItem.targetHa:.1f} ({myItem.status.name})")
        myOutputs[self.OUTPUT_FOLDER] = myFolder
        return myOutputs
