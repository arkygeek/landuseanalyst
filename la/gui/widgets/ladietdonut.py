"""
ladietdonut.py — live donut chart of the diet composition.

Pure ``QPainter``; no QtCharts (not shipped with every QGIS) and no
matplotlib (too slow for per-slider-tick redraws). Mirrors the web app's
``DietComposer`` donut so the two UIs read the same way.
"""

from typing import List, Optional, Tuple

from qgis.PyQt.QtCore import QRectF, Qt
from qgis.PyQt.QtGui import QColor, QFont, QPainter, QPen
from qgis.PyQt.QtWidgets import QSizePolicy, QWidget

# (label, LaDietLabels attribute, colour)
_SEGMENTS: List[Tuple[str, str, QColor]] = [
    ("Domestic crops", "cropsPortionPct",      QColor(60, 140, 80)),
    ("Wild plants",    "wildPlantsPortionPct", QColor(150, 200, 120)),
    ("Domestic meat",  "tameMeatPortionPct",   QColor(170, 70, 60)),
    ("Wild meat",      "wildAnimalPortionPct", QColor(230, 150, 80)),
    ("Dairy",          "dairyPortionPct",      QColor(90, 130, 200)),
]


class LaDietDonut(QWidget):
    """Donut of the five diet portions with a legend underneath."""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._mValues: List[float] = [0.0] * len(_SEGMENTS)
        self._mHasData = False
        self.setMinimumHeight(230)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setToolTip("Share of annual calories by source. Updates as you move the sliders.")

    def setLabels(self, theLabels) -> None:
        """
        Update from an ``LaDietLabels`` (or None to show the empty state).

        :param theLabels: ``la.lib.ladietlabels.LaDietLabels`` or None.
        """
        if theLabels is None:
            self._mHasData = False
            self._mValues = [0.0] * len(_SEGMENTS)
        else:
            self._mHasData = True
            self._mValues = [
                max(0.0, float(getattr(theLabels, myAttr, 0.0) or 0.0)) for _, myAttr, _ in _SEGMENTS
            ]
        self.update()

    def plantsPercent(self) -> float:
        return self._mValues[0] + self._mValues[1]

    # ------------------------------------------------------------------
    def paintEvent(self, theEvent) -> None:  # noqa: N802 - Qt override
        myPainter = QPainter(self)
        myPainter.setRenderHint(QPainter.Antialiasing)
        myPalette = self.palette()
        myTextColour = myPalette.color(myPalette.WindowText)
        myMuted = QColor(myTextColour)
        myMuted.setAlpha(140)

        myLegendHeight = 18 * len(_SEGMENTS) + 6
        myDiameter = max(40.0, min(self.width() - 16.0, self.height() - myLegendHeight - 12.0))
        myLeft = (self.width() - myDiameter) / 2.0
        myRect = QRectF(myLeft, 6.0, myDiameter, myDiameter)
        myRing = max(10.0, myDiameter * 0.17)

        myTotal = sum(self._mValues)
        myPen = QPen()
        myPen.setWidthF(myRing)
        myPen.setCapStyle(Qt.FlatCap)
        myInner = myRect.adjusted(myRing / 2, myRing / 2, -myRing / 2, -myRing / 2)

        if not self._mHasData or myTotal <= 0:
            myPen.setColor(QColor(myMuted))
            myPainter.setPen(myPen)
            myPainter.drawArc(myInner, 0, 360 * 16)
        else:
            myStart = 90.0 * 16  # 12 o'clock, clockwise
            for (_, _, myColour), myValue in zip(_SEGMENTS, self._mValues):
                mySpan = -myValue / myTotal * 360.0 * 16
                if abs(mySpan) < 1:
                    continue
                myPen.setColor(myColour)
                myPainter.setPen(myPen)
                myPainter.drawArc(myInner, int(myStart), int(mySpan))
                myStart += mySpan

        # Centre text
        myPainter.setPen(myTextColour)
        myFont = QFont(self.font())
        myFont.setPointSizeF(max(9.0, myDiameter / 9.0))
        myFont.setBold(True)
        myPainter.setFont(myFont)
        myCentre = f"{self.plantsPercent():.0f}% plants" if self._mHasData else "—"
        myPainter.drawText(myRect, Qt.AlignCenter, myCentre)

        # Legend
        myY = int(myRect.bottom()) + 10
        myFont = QFont(self.font())
        myPainter.setFont(myFont)
        for (myLabel, _, myColour), myValue in zip(_SEGMENTS, self._mValues):
            myPainter.setPen(Qt.NoPen)
            myPainter.setBrush(myColour)
            myPainter.drawRoundedRect(QRectF(10, myY + 3, 12, 12), 2, 2)
            myPainter.setPen(myTextColour if self._mHasData else myMuted)
            myPainter.drawText(30, myY + 13, myLabel)
            myPainter.drawText(
                QRectF(0, myY, self.width() - 10, 18), Qt.AlignRight | Qt.AlignVCenter,
                f"{myValue:.1f} %" if self._mHasData else "",
            )
            myY += 18
        myPainter.end()
