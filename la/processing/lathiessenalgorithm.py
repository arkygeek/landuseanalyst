"""``la:thiessen`` — Thiessen (Voronoi) territories clipped to an extent."""

from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsField, QgsFields, QgsProcessing, QgsProcessingException, QgsProcessingParameterExtent,
    QgsProcessingParameterFeatureSink, QgsProcessingParameterFeatureSource, QgsProcessingParameterNumber,
    QgsWkbTypes,
)

from la.processing.labasealgorithm import LaBaseAlgorithm


class LaThiessenAlgorithm(LaBaseAlgorithm):
    SITES = "SITES"
    EXTENT = "EXTENT"
    BUFFER_PCT = "BUFFER_PCT"
    OUTPUT = "OUTPUT"

    def name(self) -> str:
        return "thiessen"

    def displayName(self) -> str:
        return self.tr("Thiessen territories")

    def shortHelpString(self) -> str:
        return self.tr(
            "Splits the region between settlements with Voronoi (Thiessen) polygons — every location "
            "belongs to the nearest site. The tessellation is clipped to the given extent, or to the "
            "sites' bounding box grown by the buffer percentage. Renfrew's simplest territorial model; "
            "compare with XTent for size-weighted influence.")

    def initAlgorithm(self, theConfig=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.SITES, self.tr("Settlement points"), [QgsProcessing.TypeVectorPoint]))
        self.addParameter(QgsProcessingParameterExtent(self.EXTENT, self.tr("Clip extent"), optional=True))
        self.addParameter(QgsProcessingParameterNumber(
            self.BUFFER_PCT, self.tr("Bounding-box buffer (% of extent) when no clip extent is given"),
            QgsProcessingParameterNumber.Double, defaultValue=10.0, minValue=0.0, maxValue=500.0))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, self.tr("Thiessen territories"), QgsProcessing.TypeVectorPolygon))

    def processAlgorithm(self, theParameters, theContext, theFeedback):
        from la.lib import laregional

        mySource = self.parameterAsSource(theParameters, self.SITES, theContext)
        if mySource is None:
            raise QgsProcessingException(self.tr("No settlement layer."))
        myPoints, myIds, _ = self.sitePoints(mySource)
        if len(myPoints) < 3:
            raise QgsProcessingException(self.tr("At least three settlements are needed."))
        myCrs = mySource.sourceCrs()
        if self.parameterAsExtent(theParameters, self.EXTENT, theContext, myCrs).isNull():
            myBbox = laregional.fitBbox(myPoints, self.parameterAsDouble(theParameters, self.BUFFER_PCT, theContext) / 100.0)
        else:
            myExtent = self.parameterAsExtent(theParameters, self.EXTENT, theContext, myCrs)
            myBbox = (myExtent.xMinimum(), myExtent.yMinimum(), myExtent.xMaximum(), myExtent.yMaximum())

        myFields = QgsFields()
        myFields.append(QgsField("site_fid", QVariant.Int))
        myFields.append(QgsField("area_ha", QVariant.Double))
        mySink, myDestination = self.parameterAsSink(
            theParameters, self.OUTPUT, theContext, myFields, QgsWkbTypes.Polygon, myCrs)
        if mySink is None:
            raise QgsProcessingException(self.tr("Could not create the output layer."))

        myRings = laregional.computeThiessen(myPoints, myBbox)
        for myIndex, myRing in enumerate(myRings):
            if theFeedback.isCanceled():
                break
            if len(myRing) < 4:
                continue
            myGeometry = self.ringToGeometry([myRing])
            mySink.addFeature(self.makeFeature(myGeometry, [myIds[myIndex], myGeometry.area() / 10000.0]))
            theFeedback.setProgress(100 * (myIndex + 1) / len(myRings))
        return {self.OUTPUT: myDestination}
