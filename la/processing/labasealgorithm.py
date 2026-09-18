"""Shared helpers for the Landuse Analyst Processing algorithms."""

from typing import List, Optional, Tuple

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsFeature, QgsGeometry, QgsPointXY,
    QgsProcessingAlgorithm, QgsProcessingFeatureSource, QgsProject, QgsWkbTypes,
)


class LaBaseAlgorithm(QgsProcessingAlgorithm):
    """Common plumbing: translation, grouping, point extraction."""

    GROUP = "Regional analysis"
    GROUP_ID = "regional"

    def tr(self, theText: str) -> str:
        return QCoreApplication.translate("LaProcessing", theText)

    def group(self) -> str:
        return self.tr(self.GROUP)

    def groupId(self) -> str:
        return self.GROUP_ID

    def createInstance(self):
        return type(self)()

    @staticmethod
    def sitePoints(theSource: QgsProcessingFeatureSource, theTargetCrs: Optional[QgsCoordinateReferenceSystem] = None,
                   theSizeField: Optional[str] = None) -> Tuple[List[Tuple[float, float]], List[int], List[float]]:
        """
        ``(points, featureIds, sizes)`` for every feature of a point source.

        Multi-point / non-point geometries contribute their centroid. Points are
        transformed into ``theTargetCrs`` when given.
        """
        myTransform = None
        if theTargetCrs is not None and theTargetCrs.isValid() and theSource.sourceCrs() != theTargetCrs:
            myTransform = QgsCoordinateTransform(theSource.sourceCrs(), theTargetCrs, QgsProject.instance())
        myPoints, myIds, mySizes = [], [], []
        for myFeature in theSource.getFeatures():
            myGeometry: QgsGeometry = myFeature.geometry()
            if myGeometry is None or myGeometry.isEmpty():
                continue
            if myTransform is not None:
                myGeometry = QgsGeometry(myGeometry)
                myGeometry.transform(myTransform)
            if QgsWkbTypes.geometryType(myGeometry.wkbType()) == QgsWkbTypes.PointGeometry and not myGeometry.isMultipart():
                myPoint: QgsPointXY = myGeometry.asPoint()
            else:
                myPoint = myGeometry.centroid().asPoint()
            myPoints.append((float(myPoint.x()), float(myPoint.y())))
            myIds.append(int(myFeature.id()))
            mySize = 0.0
            if theSizeField:
                try:
                    mySize = float(myFeature[theSizeField] or 0.0)
                except (KeyError, TypeError, ValueError):
                    mySize = 0.0
            mySizes.append(mySize)
        return myPoints, myIds, mySizes

    @staticmethod
    def ringToGeometry(theRings) -> QgsGeometry:
        """GeoJSON-style ``[outer, hole, ...]`` rings → polygon geometry."""
        myPolygon = [[QgsPointXY(float(x), float(y)) for x, y in myRing] for myRing in theRings]
        return QgsGeometry.fromPolygonXY(myPolygon)

    @staticmethod
    def makeFeature(theGeometry: QgsGeometry, theAttributes: list) -> QgsFeature:
        myFeature = QgsFeature()
        myFeature.setGeometry(theGeometry)
        myFeature.setAttributes(theAttributes)
        return myFeature
