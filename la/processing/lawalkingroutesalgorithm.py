"""``la:walkingroutes`` — least-cost walking routes between settlements over a DEM."""

import os
import tempfile

from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsCoordinateTransformContext, QgsField, QgsFields, QgsGeometry, QgsPointXY, QgsProcessing,
    QgsProcessingException, QgsProcessingParameterFeatureSink, QgsProcessingParameterFeatureSource,
    QgsProcessingParameterNumber, QgsProcessingParameterRasterDestination, QgsProcessingParameterRasterLayer,
    QgsProcessingParameterVectorLayer, QgsVectorFileWriter, QgsWkbTypes,
)

from la.processing.labasealgorithm import LaBaseAlgorithm


class LaWalkingRoutesAlgorithm(LaBaseAlgorithm):
    DEM = "DEM"
    SITES = "SITES"
    BARRIERS = "BARRIERS"
    BUFFER_M = "BUFFER_M"
    WAYPOINT = "WAYPOINT"
    ROUTES = "ROUTES"
    ACCUMULATION = "ACCUMULATION"

    def name(self) -> str:
        return "walkingroutes"

    def displayName(self) -> str:
        return self.tr("Walking routes between settlements")

    def shortHelpString(self) -> str:
        return self.tr(
            "Least-cost walking routes (Tobler's hiking function, both directions) between every pair of "
            "neighbouring settlements (Delaunay), with a way-point pull that bundles paths through "
            "intermediate sites. Optional rivers / lakes / walls act as fords or barriers. Outputs the "
            "route lines with their walking time and how many other routes share their busiest cell, "
            "and an accumulation raster of route usage on the DEM window.")

    def initAlgorithm(self, theConfig=None):
        self.addParameter(QgsProcessingParameterRasterLayer(self.DEM, self.tr("DEM (metres, projected CRS)")))
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.SITES, self.tr("Settlement points"), [QgsProcessing.TypeVectorPoint]))
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.BARRIERS, self.tr("Barriers (rivers / lakes / walls)"),
            [QgsProcessing.TypeVectorLine, QgsProcessing.TypeVectorPolygon], optional=True))
        self.addParameter(QgsProcessingParameterNumber(
            self.BUFFER_M, self.tr("Window buffer around the sites (metres)"), QgsProcessingParameterNumber.Double,
            defaultValue=5000.0, minValue=0.0))
        self.addParameter(QgsProcessingParameterNumber(
            self.WAYPOINT, self.tr("Way-point pull strength (1 = none)"), QgsProcessingParameterNumber.Double,
            defaultValue=2.0, minValue=1.0, maxValue=20.0))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.ROUTES, self.tr("Walking routes"), QgsProcessing.TypeVectorLine))
        self.addParameter(QgsProcessingParameterRasterDestination(
            self.ACCUMULATION, self.tr("Route usage raster"), optional=True, createByDefault=False))

    def processAlgorithm(self, theParameters, theContext, theFeedback):
        import numpy as np
        from la.lib import lapathnetwork, laraster

        myDem = self.parameterAsRasterLayer(theParameters, self.DEM, theContext)
        mySource = self.parameterAsSource(theParameters, self.SITES, theContext)
        if myDem is None or mySource is None:
            raise QgsProcessingException(self.tr("A DEM and a settlement layer are required."))
        myCrs = myDem.crs()
        myPoints, myIds, _ = self.sitePoints(mySource, theTargetCrs=myCrs)
        if len(myPoints) < 3:
            raise QgsProcessingException(self.tr("At least three settlements are needed for a Delaunay network."))

        myBarriersPath = None
        myBarrierLayer = self.parameterAsVectorLayer(theParameters, self.BARRIERS, theContext)
        if myBarrierLayer is not None:
            myBarriersPath = os.path.join(tempfile.mkdtemp(prefix="la_routes_"), "barriers.gpkg")
            myOptions = QgsVectorFileWriter.SaveVectorOptions()
            myOptions.driverName = "GPKG"
            myError, myMessage, *_ = QgsVectorFileWriter.writeAsVectorFormatV3(
                myBarrierLayer, myBarriersPath, QgsCoordinateTransformContext(), myOptions)
            if myError != QgsVectorFileWriter.NoError:
                raise QgsProcessingException(self.tr(f"Could not export the barrier layer: {myMessage}"))

        theFeedback.pushInfo(self.tr(f"Routing {len(myPoints)} settlements over {myDem.source()}"))
        try:
            myResult = lapathnetwork.walkingRoutes(
                myDem.source(), myPoints,
                theWindowBufferM=self.parameterAsDouble(theParameters, self.BUFFER_M, theContext),
                theWayPointStrength=self.parameterAsDouble(theParameters, self.WAYPOINT, theContext),
                theBarriersPath=myBarriersPath,
            )
        except (ValueError, FileNotFoundError, ImportError) as e:
            raise QgsProcessingException(str(e)) from e

        myFields = QgsFields()
        myFields.append(QgsField("origin_fid", QVariant.Int))
        myFields.append(QgsField("dest_fid", QVariant.Int))
        myFields.append(QgsField("cost_s", QVariant.Double))
        myFields.append(QgsField("cost_h", QVariant.Double))
        myFields.append(QgsField("peak_usage", QVariant.Int))
        mySink, myDestination = self.parameterAsSink(
            theParameters, self.ROUTES, theContext, myFields, QgsWkbTypes.LineString, myCrs)
        if mySink is None:
            raise QgsProcessingException(self.tr("Could not create the routes layer."))
        for myRoute, (myOrigin, myDest), myCost, myPeak in zip(
                myResult.routes, myResult.routeIds, myResult.routeCosts, myResult.routePeakUsage):
            if theFeedback.isCanceled():
                break
            if len(myRoute) < 2:
                continue
            myGeometry = QgsGeometry.fromPolylineXY([QgsPointXY(float(x), float(y)) for x, y in myRoute])
            mySink.addFeature(self.makeFeature(
                myGeometry, [myIds[myOrigin], myIds[myDest], float(myCost), float(myCost) / 3600.0, int(myPeak)]))

        myOutputs = {self.ROUTES: myDestination}
        myAccumulationPath = self.parameterAsOutputLayer(theParameters, self.ACCUMULATION, theContext)
        if myAccumulationPath:
            laraster._writeGeoTiff(myAccumulationPath, myResult.accumulation.astype(np.int32),
                                   myResult.windowGeoTransform, myResult.projectionWkt or myCrs.toWkt(), np.int32, 0)
            myOutputs[self.ACCUMULATION] = myAccumulationPath
        myMissing = [myIds[i] for i in range(len(myPoints)) if i not in myResult.inCoverage]
        if myMissing:
            theFeedback.pushWarning(self.tr(f"{len(myMissing)} settlement(s) fall outside the DEM and were skipped: {myMissing}"))
        return myOutputs
