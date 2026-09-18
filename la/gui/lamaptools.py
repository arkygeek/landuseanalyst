"""
lamaptools.py — map-canvas interaction for Landuse Analyst.

:class:`LaSeedMapTool` lets the user click the settlement location on the
QGIS canvas instead of typing coordinates. It draws a red vertex marker at
the seed and reports the click in the canvas CRS; the settings dock converts
to the DEM's CRS.
"""

from typing import Optional

from qgis.PyQt.QtCore import Qt, pyqtSignal
from qgis.PyQt.QtGui import QColor
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsPointXY, QgsProject
from qgis.gui import QgsMapCanvas, QgsMapToolEmitPoint, QgsVertexMarker


class LaSeedMapTool(QgsMapToolEmitPoint):
    """
    Click-to-place tool for the settlement seed.

    :signal seedPicked(QgsPointXY): the clicked point in the canvas CRS.
    :signal deactivatedTool(): the tool was switched off (Esc or another tool).
    """

    seedPicked = pyqtSignal(QgsPointXY)
    deactivatedTool = pyqtSignal()

    def __init__(self, theCanvas: QgsMapCanvas) -> None:
        super().__init__(theCanvas)
        self.mCanvas = theCanvas
        self.mMarker: Optional[QgsVertexMarker] = None
        self.setCursor(Qt.CrossCursor)
        self.canvasClicked.connect(self._onCanvasClicked)

    def _onCanvasClicked(self, thePoint: QgsPointXY, theButton) -> None:
        if theButton != Qt.LeftButton:
            return
        self.showMarker(thePoint)
        self.seedPicked.emit(thePoint)

    def showMarker(self, theCanvasPoint: QgsPointXY) -> None:
        """Place (or move) the red seed marker at ``theCanvasPoint`` (canvas CRS)."""
        if self.mMarker is None:
            self.mMarker = QgsVertexMarker(self.mCanvas)
            self.mMarker.setIconType(QgsVertexMarker.ICON_CIRCLE)
            self.mMarker.setColor(QColor(220, 30, 30))
            self.mMarker.setFillColor(QColor(220, 30, 30, 160))
            self.mMarker.setIconSize(14)
            self.mMarker.setPenWidth(2)
        self.mMarker.setCenter(theCanvasPoint)
        self.mMarker.show()

    def showMarkerAt(self, theX: float, theY: float, theCrs: QgsCoordinateReferenceSystem) -> None:
        """Place the marker for a point given in ``theCrs`` (e.g. the DEM CRS)."""
        myPoint = QgsPointXY(theX, theY)
        myCanvasCrs = self.mCanvas.mapSettings().destinationCrs()
        if theCrs.isValid() and myCanvasCrs.isValid() and theCrs != myCanvasCrs:
            myTransform = QgsCoordinateTransform(theCrs, myCanvasCrs, QgsProject.instance())
            try:
                myPoint = myTransform.transform(myPoint)
            except Exception:  # out-of-range coordinates: leave the marker where it is
                return
        self.showMarker(myPoint)

    def clearMarker(self) -> None:
        if self.mMarker is not None:
            self.mCanvas.scene().removeItem(self.mMarker)
            self.mMarker = None

    def deactivate(self) -> None:  # noqa: N802 - Qt override
        super().deactivate()
        self.deactivatedTool.emit()

    def keyPressEvent(self, theEvent) -> None:  # noqa: N802 - Qt override
        if theEvent.key() == Qt.Key_Escape:
            self.mCanvas.unsetMapTool(self)
        else:
            super().keyPressEvent(theEvent)
