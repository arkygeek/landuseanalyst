"""
lalayerstyles.py — QGIS renderers for the layers Landuse Analyst produces.

All styling lives here so :mod:`la.gui.lacatchmenttask` and the main form
share one look: green catchment masks for crops, amber for grazing, a warm
semi-transparent walking-cost gradient, a red settlement marker and an
opt-in shaded-relief treatment for the DEM.
"""

import os
from typing import Optional

from qgis.PyQt.QtGui import QColor
from qgis.core import (
    QgsColorRampShader,
    QgsHillshadeRenderer,
    QgsMarkerSymbol,
    QgsPalettedRasterRenderer,
    QgsProject,
    QgsRasterLayer,
    QgsRasterShader,
    QgsSingleBandPseudoColorRenderer,
    QgsSingleSymbolRenderer,
    QgsVectorLayer,
)

_QML_MASK_STYLE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),  # la/
    "resources", "styles", "catchment_mask.qml",
)

# Mask fills: crop land vs grazing land.
_CROP_COLOUR    = QColor(46, 139, 87, 170)    # sea green
_FALLOW_COLOUR  = QColor(154, 205, 50, 150)   # yellow-green: rested cropland
_GRAZING_COLOUR = QColor(218, 165, 32, 170)   # goldenrod

# Walking-cost ramp (seconds): near → far. Warm tans keep the DEM legible.
_COST_RAMP = [
    (0.0,   QColor(255, 255, 229)),
    (0.25,  QColor(254, 227, 145)),
    (0.5,   QColor(254, 153, 41)),
    (0.75,  QColor(204, 76, 2)),
    (1.0,   QColor(102, 37, 6)),
]
_COST_OPACITY = 0.45

# Elevation ramp for the shaded-relief helper (metres, relative to layer range).
_DEM_RAMP = [
    (0.0,  QColor(38, 115, 0)),      # valley floor greens
    (0.25, QColor(139, 190, 60)),
    (0.5,  QColor(230, 220, 120)),
    (0.75, QColor(160, 110, 60)),
    (1.0,  QColor(255, 255, 255)),   # peaks
]


class LaLayerStyles:
    """Static helpers that apply the plugin's renderers to QGIS layers."""

    @staticmethod
    def applyCatchmentMaskStyle(theLayer: QgsRasterLayer, theIsCrop: bool = True, theCategory: str = "") -> None:
        """
        Style a ``{0,1}`` catchment mask: value 1 filled, 0 transparent.

        :param theLayer: Loaded mask raster layer.
        :param theIsCrop: True for crop land (green), False for grazing (amber).
        :param theCategory: ``"fallow"`` picks the lighter rested-cropland colour.
        """
        myColour = _CROP_COLOUR if theIsCrop else _GRAZING_COLOUR
        if theCategory == "fallow":
            myColour = _FALLOW_COLOUR
        myClasses = [
            QgsPalettedRasterRenderer.Class(1, myColour, "Catchment"),
        ]
        myRenderer = QgsPalettedRasterRenderer(theLayer.dataProvider(), 1, myClasses)
        theLayer.setRenderer(myRenderer)
        theLayer.triggerRepaint()

    @staticmethod
    def applyCostSurfaceStyle(theLayer: QgsRasterLayer) -> None:
        """
        Semi-transparent warm gradient over the walking-cost raster.

        :param theLayer: Loaded cost-surface raster layer (seconds).
        """
        myStats = theLayer.dataProvider().bandStatistics(1)
        myMin = float(myStats.minimumValue)
        myMax = float(myStats.maximumValue)
        if not myMax > myMin:
            myMax = myMin + 1.0
        LaLayerStyles._applyPseudoColour(theLayer, myMin, myMax, _COST_RAMP)
        theLayer.setOpacity(_COST_OPACITY)
        theLayer.triggerRepaint()

    @staticmethod
    def applySettlementStyle(theLayer: QgsVectorLayer) -> None:
        """
        Bright red circle with a black outline for the settlement seed.

        :param theLayer: Point memory layer holding the seed.
        """
        mySymbol = QgsMarkerSymbol.createSimple({
            "name": "circle",
            "color": "220,30,30,255",
            "outline_color": "0,0,0,255",
            "outline_width": "0.4",
            "size": "4.0",
        })
        theLayer.setRenderer(QgsSingleSymbolRenderer(mySymbol))
        theLayer.triggerRepaint()

    @staticmethod
    def applyShadedRelief(theDemLayer: QgsRasterLayer) -> Optional[QgsRasterLayer]:
        """
        Colour the DEM by elevation and overlay a multiply-blended hillshade.

        Adds a duplicate ``<name> hillshade`` layer directly above the DEM in
        the layer tree. Returns that hillshade layer (or None if the DEM has
        no tree node).

        :param theDemLayer: The elevation raster to style.
        """
        myStats = theDemLayer.dataProvider().bandStatistics(1)
        LaLayerStyles._applyPseudoColour(
            theDemLayer, float(myStats.minimumValue), float(myStats.maximumValue), _DEM_RAMP
        )
        theDemLayer.triggerRepaint()

        myProject = QgsProject.instance()
        myNode = myProject.layerTreeRoot().findLayer(theDemLayer.id())
        if myNode is None:
            return None
        myHillshade = QgsRasterLayer(theDemLayer.source(), f"{theDemLayer.name()} hillshade")
        if not myHillshade.isValid():
            return None
        myRenderer = QgsHillshadeRenderer(myHillshade.dataProvider(), 1, 315.0, 45.0)
        myRenderer.setMultiDirectional(True)
        myHillshade.setRenderer(myRenderer)
        myHillshade.setBlendMode(myHillshade.blendMode().__class__.CompositionMode_Multiply)
        myProject.addMapLayer(myHillshade, False)
        myParent = myNode.parent()
        myIndex = myParent.children().index(myNode)
        myParent.insertLayer(myIndex, myHillshade)
        myHillshade.triggerRepaint()
        return myHillshade

    # ------------------------------------------------------------------
    @staticmethod
    def _applyPseudoColour(theLayer: QgsRasterLayer, theMin: float, theMax: float, theRamp) -> None:
        myShaderFunction = QgsColorRampShader()
        myShaderFunction.setColorRampType(QgsColorRampShader.Interpolated)
        myItems = []
        for myFraction, myColour in theRamp:
            myValue = theMin + myFraction * (theMax - theMin)
            myItems.append(QgsColorRampShader.ColorRampItem(myValue, myColour, f"{myValue:.0f}"))
        myShaderFunction.setColorRampItemList(myItems)
        myShader = QgsRasterShader()
        myShader.setRasterShaderFunction(myShaderFunction)
        myRenderer = QgsSingleBandPseudoColorRenderer(theLayer.dataProvider(), 1, myShader)
        myRenderer.setClassificationMin(theMin)
        myRenderer.setClassificationMax(theMax)
        theLayer.setRenderer(myRenderer)
