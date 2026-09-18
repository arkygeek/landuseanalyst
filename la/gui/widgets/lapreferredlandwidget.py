"""
lapreferredlandwidget.py — "Preferred land" group for the parameter editors.

Edits the per-item slope band (``applySlopeLimit``, ``slopeMinDegrees``,
``slopeMaxDegrees``) shared by :class:`la.lib.lacropparameter.LaCropParameter`
and :class:`la.lib.laanimalparameter.LaAnimalParameter`.
"""

from typing import Optional

from qgis.PyQt.QtWidgets import (
    QCheckBox, QFormLayout, QGridLayout, QLabel, QLayout, QVBoxLayout, QWidget,
)
from qgis.gui import QgsCollapsibleGroupBox, QgsDoubleSpinBox


class LaPreferredLandWidget(QgsCollapsibleGroupBox):
    """Slope-band editor. ``loadFrom`` / ``applyTo`` move values to and from a parameter object."""

    def __init__(self, theKindLabel: str = "this item", parent: Optional[QWidget] = None) -> None:
        super().__init__("Preferred land (slope)", parent)
        self.setObjectName("grpPreferredLand")
        myLayout = QVBoxLayout(self)
        self.cbApplySlopeLimit = QCheckBox(f"Restrict {theKindLabel} to a slope band", self)
        self.cbApplySlopeLimit.setObjectName("cbApplySlopeLimit")
        self.cbApplySlopeLimit.setToolTip(
            "When on, only cells whose slope (derived from the DEM) lies inside the band count as "
            "suitable land in the catchment search. Off = the suitability raster alone decides.")
        myLayout.addWidget(self.cbApplySlopeLimit)
        myForm = QFormLayout()
        self.sbSlopeMinDegrees = QgsDoubleSpinBox(self)
        self.sbSlopeMinDegrees.setObjectName("sbSlopeMinDegrees")
        self.sbSlopeMinDegrees.setRange(0.0, 89.5)
        self.sbSlopeMinDegrees.setDecimals(1)
        self.sbSlopeMinDegrees.setSingleStep(0.5)
        self.sbSlopeMinDegrees.setSuffix(" °")
        self.sbSlopeMinDegrees.setToolTip("Gentlest usable slope. 0 = no lower bound.")
        myForm.addRow("Minimum slope", self.sbSlopeMinDegrees)
        self.sbSlopeMaxDegrees = QgsDoubleSpinBox(self)
        self.sbSlopeMaxDegrees.setObjectName("sbSlopeMaxDegrees")
        self.sbSlopeMaxDegrees.setRange(0.0, 90.0)
        self.sbSlopeMaxDegrees.setDecimals(1)
        self.sbSlopeMaxDegrees.setSingleStep(0.5)
        self.sbSlopeMaxDegrees.setSuffix(" °")
        self.sbSlopeMaxDegrees.setToolTip("Steepest usable slope. Thesis: 9° for crops, 15° for grazing; olives tolerate ~20°.")
        myForm.addRow("Maximum slope", self.sbSlopeMaxDegrees)
        myLayout.addLayout(myForm)
        self.lblHint = QLabel(
            "Applied per crop / animal during the catchment search; with no suitability raster the "
            "band alone defines suitable land.", self)
        self.lblHint.setWordWrap(True)
        self.lblHint.setStyleSheet("QLabel { color: palette(mid); }")
        myLayout.addWidget(self.lblHint)
        self.cbApplySlopeLimit.toggled.connect(self._onToggled)
        self._onToggled(self.cbApplySlopeLimit.isChecked())

    def _onToggled(self, theChecked: bool) -> None:
        self.sbSlopeMinDegrees.setEnabled(theChecked)
        self.sbSlopeMaxDegrees.setEnabled(theChecked)

    def loadFrom(self, theParameter) -> None:
        """Show ``theParameter``'s slope band."""
        self.cbApplySlopeLimit.setChecked(bool(getattr(theParameter, "applySlopeLimit", True)))
        self.sbSlopeMinDegrees.setValue(float(getattr(theParameter, "slopeMinDegrees", 0.0)))
        self.sbSlopeMaxDegrees.setValue(float(getattr(theParameter, "slopeMaxDegrees", 9.0)))

    def applyTo(self, theParameter) -> None:
        """Write the edited slope band back onto ``theParameter``."""
        theParameter.applySlopeLimit = self.cbApplySlopeLimit.isChecked()
        myMin = self.sbSlopeMinDegrees.value()
        myMax = self.sbSlopeMaxDegrees.value()
        if myMax < myMin:
            myMin, myMax = myMax, myMin
        theParameter.slopeMinDegrees = myMin
        theParameter.slopeMaxDegrees = myMax

    @staticmethod
    def attachBelow(theAnchorWidget: QWidget, theWidget: "LaPreferredLandWidget") -> bool:
        """
        Add ``theWidget`` to the layout that holds ``theAnchorWidget`` (below it).

        Works for grid, form and box layouts; returns False when the anchor
        has no layout (the caller then falls back to the dialog's top layout).
        """
        if theAnchorWidget is None:
            return False
        myParent = theAnchorWidget.parentWidget()
        myLayout: Optional[QLayout] = myParent.layout() if myParent is not None else None
        if myLayout is None:
            return False
        if isinstance(myLayout, QGridLayout):
            myLayout.addWidget(theWidget, myLayout.rowCount(), 0, 1, max(1, myLayout.columnCount()))
        elif isinstance(myLayout, QFormLayout):
            myLayout.addRow(theWidget)
        else:
            myLayout.addWidget(theWidget)
        return True
