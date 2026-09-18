"""``la:xtent`` — XTent political territories (Renfrew & Level 1979)."""

from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsField, QgsFields, QgsProcessing, QgsProcessingException, QgsProcessingParameterExtent,
    QgsProcessingParameterFeatureSink, QgsProcessingParameterFeatureSource, QgsProcessingParameterField,
    QgsProcessingParameterNumber, QgsProcessingParameterRasterDestination, QgsWkbTypes,
)

from la.processing.labasealgorithm import LaBaseAlgorithm


class LaXtentAlgorithm(LaBaseAlgorithm):
    SITES = "SITES"
    SIZE_FIELD = "SIZE_FIELD"
    EXTENT = "EXTENT"
    SIZE_EXPONENT = "SIZE_EXPONENT"
    DISTANCE_DECAY = "DISTANCE_DECAY"
    RESOLUTION = "RESOLUTION"
    OUTPUT = "OUTPUT"
    LABELS = "LABELS"

    def name(self) -> str:
        return "xtent"

    def displayName(self) -> str:
        return self.tr("XTent influence territories")

    def shortHelpString(self) -> str:
        return self.tr(
            "Renfrew & Level's XTent model: a site's influence I = size^a − k·distance; each cell "
            "belongs to the site with the highest positive influence, so large centres absorb small "
            "neighbours. Thesis defaults a = 0.5, k = 0.001 per metre. Outputs territory polygons "
            "(holes kept) and, optionally, the winner-index raster.")

    def initAlgorithm(self, theConfig=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.SITES, self.tr("Settlement points"), [QgsProcessing.TypeVectorPoint]))
        self.addParameter(QgsProcessingParameterField(
            self.SIZE_FIELD, self.tr("Site size field (hectares)"), parentLayerParameterName=self.SITES,
            type=QgsProcessingParameterField.Numeric))
        self.addParameter(QgsProcessingParameterExtent(self.EXTENT, self.tr("Analysis extent"), optional=True))
        self.addParameter(QgsProcessingParameterNumber(
            self.SIZE_EXPONENT, self.tr("Size exponent a"), QgsProcessingParameterNumber.Double,
            defaultValue=0.5, minValue=0.0, maxValue=5.0))
        self.addParameter(QgsProcessingParameterNumber(
            self.DISTANCE_DECAY, self.tr("Distance decay k (per metre)"), QgsProcessingParameterNumber.Double,
            defaultValue=0.001, minValue=0.0))
        self.addParameter(QgsProcessingParameterNumber(
            self.RESOLUTION, self.tr("Grid resolution (metres)"), QgsProcessingParameterNumber.Integer,
            defaultValue=250, minValue=1))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, self.tr("XTent territories"), QgsProcessing.TypeVectorPolygon))
        self.addParameter(QgsProcessingParameterRasterDestination(
            self.LABELS, self.tr("Winner-index raster"), optional=True, createByDefault=False))

    def processAlgorithm(self, theParameters, theContext, theFeedback):
        import numpy as np
        from la.lib import laraster, laregional, laxtent

        mySource = self.parameterAsSource(theParameters, self.SITES, theContext)
        if mySource is None:
            raise QgsProcessingException(self.tr("No settlement layer."))
        mySizeField = self.parameterAsString(theParameters, self.SIZE_FIELD, theContext)
        myPoints, myIds, mySizes = self.sitePoints(mySource, theSizeField=mySizeField)
        if len(myPoints) < 2:
            raise QgsProcessingException(self.tr("At least two settlements are needed."))
        myCrs = mySource.sourceCrs()
        myExtent = self.parameterAsExtent(theParameters, self.EXTENT, theContext, myCrs)
        if myExtent.isNull():
            myBbox = laregional.fitBbox(myPoints, 0.10)
        else:
            myBbox = (myExtent.xMinimum(), myExtent.yMinimum(), myExtent.xMaximum(), myExtent.yMaximum())
        mySites = [(x, y, s) for (x, y), s in zip(myPoints, mySizes)]
        myA = self.parameterAsDouble(theParameters, self.SIZE_EXPONENT, theContext)
        myK = self.parameterAsDouble(theParameters, self.DISTANCE_DECAY, theContext)
        myResolution = self.parameterAsInt(theParameters, self.RESOLUTION, theContext)

        myFields = QgsFields()
        myFields.append(QgsField("site_fid", QVariant.Int))
        myFields.append(QgsField("size_ha", QVariant.Double))
        myFields.append(QgsField("area_ha", QVariant.Double))
        mySink, myDestination = self.parameterAsSink(
            theParameters, self.OUTPUT, theContext, myFields, QgsWkbTypes.Polygon, myCrs)
        if mySink is None:
            raise QgsProcessingException(self.tr("Could not create the output layer."))

        theFeedback.pushInfo(self.tr(f"XTent on {len(mySites)} sites, a={myA}, k={myK}, {myResolution} m cells"))
        myCollection = laxtent.computeXtentFeatures(mySites, myBbox, myA, myK, myResolution)
        for myFeature in myCollection["features"]:
            if theFeedback.isCanceled():
                break
            myGeometry = self.ringToGeometry(myFeature["geometry"]["coordinates"])
            mySiteIndex = int(myFeature["properties"]["site"])
            mySink.addFeature(self.makeFeature(
                myGeometry, [myIds[mySiteIndex], float(mySizes[mySiteIndex]), myGeometry.area() / 10000.0]))

        myOutputs = {self.OUTPUT: myDestination}
        myLabelsPath = self.parameterAsOutputLayer(theParameters, self.LABELS, theContext)
        if myLabelsPath:
            myLabels, myGeoTransform = laxtent.xtentLabels(mySites, myBbox, myA, myK, myResolution)
            laraster._writeGeoTiff(myLabelsPath, myLabels.astype(np.int32), myGeoTransform, myCrs.toWkt(), np.int32, -1)
            myOutputs[self.LABELS] = myLabelsPath
        return myOutputs
