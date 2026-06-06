# -*- coding: utf-8 -*-
"""
Catchment analysis algorithm for Landuse Analyst.
"""

import os
import time
import shutil
from typing import Callable, Dict, List, Optional

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterRasterLayer,
    QgsProcessingParameterPoint,
    QgsProcessingParameterFile,
    QgsProcessingParameterRasterDestination,
    QgsProcessingParameterFolderDestination,
    QgsProcessingContext,
    QgsProcessingUtils,
    QgsProject
)

from la.lib.lamodel import LaModel
from la.lib.lacatchment import LaCatchment, LaCatchmentInputs, DistanceMethod
from la.lib.lagrass import LaGrass
from la.lib.lautils import LaUtils


class LaCatchmentAlgorithm(QgsProcessingAlgorithm):
    """QGIS Processing Algorithm for Landuse Analyst Catchment Analysis."""

    INPUT_DEM = 'INPUT_DEM'
    INPUT_SETTLEMENT = 'INPUT_SETTLEMENT'
    INPUT_PROFILE = 'INPUT_PROFILE'
    INPUT_COMMON_CROP = 'INPUT_COMMON_CROP'
    INPUT_COMMON_GRAZING = 'INPUT_COMMON_GRAZING'
    OUTPUT_COST = 'OUTPUT_COST'
    OUTPUT_FOLDER = 'OUTPUT_FOLDER'

    def __init__(self):
        super(LaCatchmentAlgorithm, self).__init__()

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_DEM,
                self.tr('DEM Raster Layer')
            )
        )
        self.addParameter(
            QgsProcessingParameterPoint(
                self.INPUT_SETTLEMENT,
                self.tr('Settlement Location (Easting, Northing)')
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.INPUT_PROFILE,
                self.tr('Scenario XML Profile (*.xml)'),
                behavior=QgsProcessingParameterFile.File,
                extension='xml'
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_COMMON_CROP,
                self.tr('Common Crop Suitability Layer (Optional)'),
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT_COMMON_GRAZING,
                self.tr('Common Grazing Suitability Layer (Optional)'),
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                self.OUTPUT_COST,
                self.tr('Cost Surface Raster Destination (Optional)'),
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUT_FOLDER,
                self.tr('Output Directory for Catchment Masks (Optional)'),
                optional=True
            )
        )

    def name(self) -> str:
        return 'catchment'

    def displayName(self) -> str:
        return self.tr('Catchment Analysis')

    def group(self) -> str:
        return self.tr('Catchment')

    def groupId(self) -> str:
        return 'catchment'

    def shortHelpString(self) -> str:
        return self.tr(
            "Runs the Landuse Analyst catchment analysis model headlessly using a "
            "unified XML scenario profile, a DEM raster, and a settlement point."
        )

    def tr(self, theMessage: str) -> str:
        return QCoreApplication.translate('LaCatchmentAlgorithm', theMessage)

    def createInstance(self):
        return LaCatchmentAlgorithm()

    def processAlgorithm(self, parameters, context, feedback):
        # 1. Retrieve layers and parameters
        myDemLayer = self.parameterAsRasterLayer(parameters, self.INPUT_DEM, context)
        if not myDemLayer:
            raise QgsProcessingException(self.tr("Invalid input DEM layer."))

        myPoint = self.parameterAsPoint(parameters, self.INPUT_SETTLEMENT, context, myDemLayer.crs())
        myProfilePath = self.parameterAsFile(parameters, self.INPUT_PROFILE, context)
        
        myCcLayer = self.parameterAsRasterLayer(parameters, self.INPUT_COMMON_CROP, context)
        myCgLayer = self.parameterAsRasterLayer(parameters, self.INPUT_COMMON_GRAZING, context)

        myCostDest = self.parameterAsOutputLayer(parameters, self.OUTPUT_COST, context)
        myFolderDest = self.parameterAsFileOutput(parameters, self.OUTPUT_FOLDER, context)

        # 2. Setup scratch folder
        myScratchDir = context.temporaryFolder()
        if not myScratchDir:
            myScratchDir = QgsProcessingUtils.tempFolder()
        myRunDir = os.path.join(myScratchDir, "landuseanalyst", f"run_{int(time.time())}")
        os.makedirs(myRunDir, exist_ok=True)

        # 3. Import scenario profile
        print(f"Loading scenario profile from: {myProfilePath}")
        if not os.path.exists(myProfilePath):
            raise QgsProcessingException(self.tr(f"Scenario profile file not found: {myProfilePath}"))

        with open(myProfilePath, 'r', encoding='utf-8') as myFile:
            myXml = myFile.read()

        myModel = LaModel()
        # Clear registries to ensure fresh load without stale in-memory cached entries
        LaUtils.clearRegistries()
        if not myModel.importScenario(myXml):
            raise QgsProcessingException(self.tr("Failed to parse the XML scenario file."))

        # 4. Set Easting and Northing from input coordinates
        myEasting = myPoint.x()
        myNorthing = myPoint.y()
        print(f"Using settlement coordinates: Easting={myEasting:.2f}, Northing={myNorthing:.2f}")
        myModel.easting = myEasting
        myModel.northing = myNorthing

        # 5. Run calculations
        print("Running target calculations...")
        if myModel.baseOnPlants:
            if myModel.includeDairy:
                myDietLabels = myModel.doCalcsPlantsFirstIncludeDairy()
            else:
                myDietLabels = myModel.doCalcsPlantsFirstDairySeparate()
        else:
            if myModel.includeDairy:
                myDietLabels = myModel.doCalcsAnimalsFirstIncludeDairy()
            else:
                myDietLabels = myModel.doCalcsAnimalsFirstDairySeparate()
        myModel.mDietLabels = myDietLabels
        print(f"Calculated targets. Crops targets map: {getattr(myModel, 'mAreaTargetsCropsMap', None)}")

        # 6. Temporarily register layers in QgsProject so lacatchment _resolveLayerPath can find them
        myRegisteredLayers = []
        try:
            for myLyr in [myDemLayer, myCcLayer, myCgLayer]:
                if myLyr and not QgsProject.instance().mapLayer(myLyr.id()):
                    QgsProject.instance().addMapLayer(myLyr)
                    myRegisteredLayers.append(myLyr)

            # 7. Setup Grass wrapper and Catchment orchestrator
            print("Initializing GRASS environment...")
            myGrass = LaGrass(myDemLayer, myRunDir)
            myCatchment = LaCatchment(myGrass, thePrecisionPct=myModel.precision)

            # Connect logger signals to stdout
            myCatchment.logged.connect(lambda msg: print(f"Catchment Log: {msg}"))

            # Match distance method from Model loaded settings
            myMethod = DistanceMethod.WalkingTime
            if myModel.euclideanDistance:
                myMethod = DistanceMethod.Euclidean
            elif myModel.pathDistance:
                myMethod = DistanceMethod.PathDistance

            # Build inputs structure
            myInputs = LaCatchmentInputs(
                demLayerId=myDemLayer.id(),
                commonCropLayerId=myCcLayer.id() if myCcLayer else None,
                commonGrazingLayerId=myCgLayer.id() if myCgLayer else None,
                method=myMethod
            )

            # Run catchment analysis pipeline
            print("Executing catchment analysis...")
            myResults = myCatchment.runCatchmentAnalysis(
                myModel,
                myInputs,
                theIsCanceledFn=feedback.isCanceled
            )

            print(f"Catchment analysis finished. Cost raster path: {myResults.costRasterPath}")
            print(f"Items in results: {len(myResults.items)}")
            for myItem in myResults.items:
                print(f"  Item: {myItem.itemName}, Status: {myItem.status}, Output: {myItem.outputPath}, Message: {myItem.message}")

            # 8. Post-process outputs
            # Copy cost surface if output path is requested
            if myCostDest and myResults.costRasterPath and os.path.exists(myResults.costRasterPath):
                shutil.copyfile(myResults.costRasterPath, myCostDest)
                print(f"Saved cost surface to: {myCostDest}")
            else:
                print(f"Not saving cost surface. myCostDest: {myCostDest}, costRasterPath: {myResults.costRasterPath}")

            # Copy catchment raster masks to output folder if requested
            if myFolderDest:
                os.makedirs(myFolderDest, exist_ok=True)
                for myItem in myResults.items:
                    if myItem.outputPath and os.path.exists(myItem.outputPath):
                        myDestFile = os.path.join(myFolderDest, os.path.basename(myItem.outputPath))
                        shutil.copyfile(myItem.outputPath, myDestFile)
                feedback.pushInfo(f"Saved catchment raster masks to: {myFolderDest}")

            # Register layers to be loaded into the current project on completion
            from qgis.core import QgsProcessingContext
            for myItem in myResults.items:
                if myItem.outputPath and os.path.exists(myItem.outputPath):
                    myDetails = QgsProcessingContext.LayerDetails(
                        f"Catchment — {myItem.itemName}",
                        QgsProject.instance(),
                        self.OUTPUT_FOLDER
                    )
                    context.addLayerToLoadOnCompletion(myItem.outputPath, myDetails)

            return {
                self.OUTPUT_COST: myCostDest if myCostDest else myResults.costRasterPath,
                self.OUTPUT_FOLDER: myFolderDest if myFolderDest else myRunDir
            }

        finally:
            # Clean up temporarily registered layers
            for myLyr in myRegisteredLayers:
                QgsProject.instance().removeMapLayer(myLyr.id())
