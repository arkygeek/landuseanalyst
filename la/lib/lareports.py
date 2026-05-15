"""
lareports.py - HTML report generation for the Landuse Analyst plugin.

Produces a thesis-style report layout for QTextBrowser, which is what
QGIS ships natively on every platform. Charts are generated via matplotlib
(also bundled with QGIS everywhere) → PNG → base64 → inline <img> tags,
so they render through QTextBrowser without needing PyQtWebEngine.

This means end users get the full report — tables AND charts — with zero
extra setup on any QGIS install.
"""

import math
from typing import Dict, List, Tuple, Optional, Sequence
from typing import TYPE_CHECKING

from la.lib.la import AreaUnits
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lamodel import LaModel

if TYPE_CHECKING:
    from la.lib.lamodel import LaModel


# Palette — keep close to the thesis figure
_BLUE_HEADER_BG  = "#3B5A8C"   # dark blue title bars
_BLUE_PANEL_BG   = "#E6ECF5"   # light blue panel fill
_GREEN_HEADER_BG = "#5C7A4C"   # green section title (selections panel)
_GREEN_PANEL_BG  = "#E0EAD5"
_ROW_ALT         = "#F2F5FA"
_SUBTOTAL_BG     = "#CFDBEF"
_HEADER_TEXT     = "white"
_MUTED           = "#666666"

# Categorical palettes for charts
_PALETTE_DIET      = ["#4CAF50", "#E65100", "#FFB300"]                         # plants / meat / dairy
_PALETTE_BREAKDOWN = ["#E65100", "#8D6E63", "#FFB300", "#A5D6A7", "#388E3C"]   # tame meat / wild meat / dairy / wild plants / crops
_PALETTE_ANIMALS   = ["#5C6BC0", "#EF5350", "#FFA726", "#26A69A", "#AB47BC", "#8D6E63"]
_PALETTE_CROPS     = ["#66BB6A", "#9CCC65", "#D4E157", "#FFEE58", "#FFCA28",
                      "#FFA726", "#FF7043", "#8D6E63", "#A1887F", "#BCAAA4", "#CFD8DC"]


def _sectionTitle(theTitle: str, theColor: str = _BLUE_HEADER_BG) -> str:
    """Heavy title bar that introduces a top-level section."""
    return (
        f'<table width="100%" cellpadding="6" cellspacing="0" border="0" '
        f'style="margin-top:14px; border-collapse:collapse;">'
        f'<tr bgcolor="{theColor}"><td style="color:{_HEADER_TEXT}; font-weight:bold; '
        f'font-size:12pt;">{theTitle}</td></tr></table>'
    )


def _styledTable(
    theHeaders: List[str],
    theRows: List[List[str]],
    theFooter: Optional[List[str]] = None,
    theNumericFromColumn: int = 1,
    theHeaderColor: str = _BLUE_HEADER_BG,
) -> str:
    """Build a consistently styled data table.

    :param theHeaders:            Column header labels.
    :param theRows:               Data rows; cells already formatted as strings.
    :param theFooter:             Optional totals row.
    :param theNumericFromColumn:  Columns at this index and beyond are right-aligned.
    :param theHeaderColor:        Header band color.
    """
    myHtml = (
        '<table width="100%" cellpadding="6" cellspacing="0" border="0" '
        'style="border-collapse:collapse; border:1px solid #C0CADD;">'
    )
    # Header row
    myHtml += f'<tr bgcolor="{theHeaderColor}">'
    for myIndex, myLabel in enumerate(theHeaders):
        myAlign = "right" if myIndex >= theNumericFromColumn else "left"
        myHtml += (
            f'<th align="{myAlign}" style="color:{_HEADER_TEXT}; '
            f'font-weight:bold; padding:6px 10px;">{myLabel}</th>'
        )
    myHtml += "</tr>"
    # Body rows
    for myRowIndex, myRow in enumerate(theRows):
        myBg = _ROW_ALT if myRowIndex % 2 else "white"
        myHtml += f'<tr bgcolor="{myBg}">'
        for myColIndex, myCell in enumerate(myRow):
            myAlign = "right" if myColIndex >= theNumericFromColumn else "left"
            myHtml += f'<td align="{myAlign}" style="padding:5px 10px;">{myCell}</td>'
        myHtml += "</tr>"
    # Footer / totals row
    if theFooter is not None:
        myHtml += f'<tr bgcolor="{_SUBTOTAL_BG}">'
        for myColIndex, myCell in enumerate(theFooter):
            myAlign = "right" if myColIndex >= theNumericFromColumn else "left"
            myHtml += (
                f'<td align="{myAlign}" style="padding:6px 10px; '
                f'font-weight:bold; border-top:2px solid #6B7FA0;">{myCell}</td>'
            )
        myHtml += "</tr>"
    myHtml += "</table>"
    return myHtml


def _kvRow(theLabel: str, theValue: str, theBgcolor: str = "white") -> str:
    return (
        f'<tr bgcolor="{theBgcolor}">'
        f'<td style="padding:5px 10px;">{theLabel}</td>'
        f'<td align="right" style="padding:5px 10px; font-weight:bold;">{theValue}</td>'
        f"</tr>"
    )


def _fmtNum(theValue, theDecimals: int = 0) -> str:
    """Format a number with comma thousands separator + N decimals; '—' on None/error."""
    try:
        myValue = float(theValue)
    except (TypeError, ValueError):
        return "—"
    return f"{myValue:,.{theDecimals}f}"


def _safeAttr(theObj, theAttr: str, theDefault=0.0):
    """Pull a (possibly PyQt-property) attribute and coerce to float."""
    try:
        return float(str(getattr(theObj, theAttr, theDefault)))
    except (TypeError, ValueError):
        return float(theDefault) if theDefault is not None else 0.0


# ---------------------------------------------------------------------------
# Chart helpers — matplotlib → PNG → base64 → inline <img>
# ---------------------------------------------------------------------------
# matplotlib ships with every QGIS install (Linux deb/rpm, Windows OSGeo4W,
# macOS bundle, conda-forge), so charts work out of the box for end users
# with no extra setup. We render through Figure + FigureCanvasAgg directly
# (no pyplot) so the chosen matplotlib backend in the running QGIS process
# doesn't affect us.

def _figureToImgTag(theFig, theMaxWidthCss: str = "100%") -> str:
    """Render a matplotlib Figure to a base64-encoded inline <img> tag."""
    import base64
    from io import BytesIO
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    myCanvas = FigureCanvasAgg(theFig)
    myBuffer = BytesIO()
    myCanvas.print_png(myBuffer)
    myEncoded = base64.b64encode(myBuffer.getvalue()).decode("ascii")
    return (
        f'<img src="data:image/png;base64,{myEncoded}" '
        f'style="max-width:{theMaxWidthCss}; vertical-align:top;"/>'
    )


def _chartPie(
    theSlices: List[Tuple[str, float, str]],
    theSize: Tuple[float, float] = (4.5, 4.5),
) -> str:
    """Pie chart with slice labels + autopct."""
    from matplotlib.figure import Figure

    myFiltered = [(l, float(v), c) for l, v, c in theSlices if float(v) > 0]
    if not myFiltered:
        return f'<div style="color:{_MUTED}; font-style:italic;">No data.</div>'

    myFig = Figure(figsize=theSize, facecolor="white", dpi=100)
    myAx = myFig.add_subplot(111)
    myLabels = [l for l, _, _ in myFiltered]
    myValues = [v for _, v, _ in myFiltered]
    myColors = [c for _, _, c in myFiltered]

    _, _, myAutotexts = myAx.pie(
        myValues,
        labels=myLabels,
        colors=myColors,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
        textprops={"fontsize": 10},
        pctdistance=0.72,
    )
    for myAutoText in myAutotexts:
        myAutoText.set_color("white")
        myAutoText.set_fontweight("bold")
    myAx.set_aspect("equal")
    myFig.tight_layout()
    return _figureToImgTag(myFig)


def _chartHorizontalBars(
    theItems: List[Tuple[str, float, str]],
    theSize: Tuple[float, float] = (6.8, 3.2),
    theValueFmt: str = "{:,.0f}",
) -> str:
    """Horizontal bar chart. Items: (label, value, color)."""
    from matplotlib.figure import Figure

    if not theItems:
        return f'<div style="color:{_MUTED}; font-style:italic;">No data.</div>'

    myFig = Figure(figsize=theSize, facecolor="white", dpi=100)
    myAx = myFig.add_subplot(111)
    myLabels = [item[0] for item in theItems]
    myValues = [float(item[1]) for item in theItems]
    myColors = [item[2] for item in theItems]
    myYPos = list(range(len(theItems)))

    myAx.barh(myYPos, myValues, color=myColors, edgecolor="white", linewidth=1)
    myAx.set_yticks(myYPos)
    myAx.set_yticklabels(myLabels, fontsize=10)
    myAx.invert_yaxis()

    myMax = max(myValues) if myValues else 0
    for myIndex, myValue in enumerate(myValues):
        myAx.text(
            myValue + myMax * 0.01,
            myIndex,
            theValueFmt.format(myValue),
            va="center",
            fontsize=9,
            color="#333",
        )

    myAx.spines["top"].set_visible(False)
    myAx.spines["right"].set_visible(False)
    myAx.tick_params(left=False)
    myAx.set_xlim(0, myMax * 1.18 if myMax > 0 else 1)
    myFig.tight_layout()
    return _figureToImgTag(myFig)


def _chartStackedVerticalBar(
    theStacks: List[Tuple[str, float, str]],
    theSize: Tuple[float, float] = (3.4, 5.4),
    theUnitLabel: str = "",
) -> str:
    """One vertical stacked bar — segments labelled inside, legend on right."""
    from matplotlib.figure import Figure

    myFiltered = [(l, float(v), c) for l, v, c in theStacks if float(v) > 0]
    if not myFiltered:
        return f'<div style="color:{_MUTED}; font-style:italic;">No data.</div>'

    myFig = Figure(figsize=theSize, facecolor="white", dpi=100)
    myAx = myFig.add_subplot(111)
    myTotal = sum(v for _, v, _ in myFiltered)
    myBottom = 0.0
    for myLabel, myValue, myColor in myFiltered:
        myAx.bar(
            0, myValue, bottom=myBottom, color=myColor, edgecolor="white",
            linewidth=1.5, width=0.55, label=myLabel,
        )
        if myValue / myTotal > 0.04:
            myAx.text(
                0, myBottom + myValue / 2.0,
                f"{myValue:,.1f}",
                ha="center", va="center",
                color="white", fontsize=9, fontweight="bold",
            )
        myBottom += myValue

    myAx.set_xticks([])
    if theUnitLabel:
        myAx.set_ylabel(theUnitLabel, fontsize=10)
    myAx.set_xlim(-0.6, 0.6)
    myAx.legend(
        loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=9, frameon=False,
    )
    myAx.spines["top"].set_visible(False)
    myAx.spines["right"].set_visible(False)
    myFig.tight_layout()
    return _figureToImgTag(myFig)


def _chartGroupedBars(
    theGroupLabels: List[str],
    theSeries: List[Tuple[str, List[float], str]],
    theSize: Tuple[float, float] = (6.2, 3.6),
    theValueFmt: str = "{:,.0f}",
) -> str:
    """Grouped vertical bars (e.g. Adults vs Offspring per animal)."""
    from matplotlib.figure import Figure

    if not theGroupLabels or not theSeries:
        return f'<div style="color:{_MUTED}; font-style:italic;">No data.</div>'

    myFig = Figure(figsize=theSize, facecolor="white", dpi=100)
    myAx = myFig.add_subplot(111)

    myN = len(theGroupLabels)
    myS = len(theSeries)
    myWidth = 0.8 / myS
    myXBase = list(range(myN))

    for myIndex, (myName, myValues, myColor) in enumerate(theSeries):
        myOffset = (myIndex - (myS - 1) / 2.0) * myWidth
        myValsFloat = [float(v) for v in myValues] + [0.0] * (myN - len(myValues))
        myXs = [x + myOffset for x in myXBase]
        myBars = myAx.bar(
            myXs, myValsFloat[:myN], myWidth, color=myColor,
            edgecolor="white", linewidth=1, label=myName,
        )
        for myBar, myVal in zip(myBars, myValsFloat[:myN]):
            if myVal > 0:
                myAx.text(
                    myBar.get_x() + myBar.get_width() / 2,
                    myBar.get_height(),
                    " " + theValueFmt.format(myVal),
                    ha="center", va="bottom", fontsize=8, color="#333",
                )

    myAx.set_xticks(myXBase)
    myAx.set_xticklabels(theGroupLabels, fontsize=10)
    myAx.legend(fontsize=9, loc="upper right", frameon=False)
    myAx.spines["top"].set_visible(False)
    myAx.spines["right"].set_visible(False)
    myAx.tick_params(bottom=False)
    myFig.tight_layout()
    return _figureToImgTag(myFig)


# ---------------------------------------------------------------------------
# Top-level "Model Settings" / Summary + Selections + Diet Composition
# ---------------------------------------------------------------------------
def toHtml(model: "LaModel", theIncludeCharts: bool = True) -> str:
    """Top section: scenario header, summary metrics, selections, and (if
    charts can render) the diet-composition pie panel.

    :param theIncludeCharts: when False (QTextBrowser mode), the SVG pie
        section is replaced with a small tabular fallback so the report
        doesn't show raw SVG text leaks.
    """
    myHtml = _scenarioHeader(model)
    myHtml += _summaryPanel(model)
    myHtml += _selectionsPanel(model)
    if theIncludeCharts:
        myHtml += _dietCompositionPanel(model)
    else:
        myHtml += _dietCompositionTablePanel(model)
    return myHtml


def _scenarioHeader(model: "LaModel") -> str:
    """Thesis-style top strip: settlement name, period, basic dimensions."""
    myName    = getattr(model, "name", "") or "(Unnamed)"
    myPeriod  = getattr(model, "period", "") or ""
    myPop     = int(_safeAttr(model, "population", 0))
    myKcalDay = int(_safeAttr(model, "caloriesPerPersonDaily", 0))

    myMethod = "Plants First" if getattr(model, "baseOnPlants", False) else "Animals First"
    myDairy  = "Included" if getattr(model, "includeDairy", False) else "Calculated Separately"

    myHtml = (
        f'<table width="100%" cellpadding="10" cellspacing="0" border="0" '
        f'style="border-collapse:collapse; background-color:{_BLUE_PANEL_BG}; '
        f'border:1px solid #B4C2D8; margin-bottom:12px;">'
    )
    myHtml += f'<tr bgcolor="{_BLUE_HEADER_BG}">'
    myHtml += (
        f'<td colspan="4" style="color:{_HEADER_TEXT}; font-weight:bold; '
        f'font-size:14pt; padding:10px 14px;">'
        f"Settlement: {myName} &nbsp;&nbsp;·&nbsp;&nbsp; Period: {myPeriod}"
        f"</td></tr>"
    )
    myHtml += (
        f'<tr>'
        f'<td><b>Minimum Population</b></td><td align="right">{myPop}</td>'
        f'<td><b>MCals Person⁻¹ Day⁻¹</b></td>'
        f'<td align="right">{myKcalDay / 1000.0:.3f}</td>'
        f"</tr>"
        f'<tr>'
        f'<td><b>Calculation Method</b></td><td align="right">{myMethod}</td>'
        f'<td><b>Dairy</b></td><td align="right">{myDairy}</td>'
        f"</tr>"
    )
    myHtml += "</table>"
    return myHtml


def _summaryPanel(model: "LaModel") -> str:
    """Top-right thesis panel: per-person/year, City, Crops/Animals MCal+Ha totals."""
    myDietLabels = getattr(model, "mDietLabels", None)
    if not myDietLabels:
        return _sectionTitle("Diet Summary") + "<p>No calculation results available.</p>"

    myKcalPerPersonDay = _safeAttr(model, "caloriesPerPersonDaily", 0.0)
    myMCalsPerPersonYr = myKcalPerPersonDay * 365.0 / 1000.0
    myCityMCalsYr      = _safeAttr(myDietLabels, "megaCaloriesSettlementAnnual", 0.0)
    myPlantPct         = _safeAttr(myDietLabels, "plantsPortionPct", 0.0)

    # MCals contributions
    myCropMCals      = _safeAttr(myDietLabels, "cropMCalories", 0.0)
    myAnimalMCals    = _safeAttr(myDietLabels, "animalMCalories", 0.0)
    myDairyMCals     = _safeAttr(myDietLabels, "dairyMCalories", 0.0)
    myWildAnimalMCals = _safeAttr(myDietLabels, "wildAnimalMCalories", 0.0)
    myWildPlantMCals  = _safeAttr(myDietLabels, "wildPlantsMCalories", 0.0)
    myDairySurplus    = _safeAttr(myDietLabels, "dairySurplusMCalories", 0.0)

    # Crop area total
    myCropAreaMap   = getattr(model, "mAreaTargetsCropsMap", {}) or {}
    myAnimalAreaMap = getattr(model, "mAreaTargetsAnimalsMap", {}) or {}
    myCropAreaHa    = sum(float(v) for k, v in myCropAreaMap.items() if k != "CommonTarget")
    myAnimalAreaHa  = sum(float(v) for k, v in myAnimalAreaMap.items() if k != "CommonTarget")
    myTotalLandHa   = _safeAttr(myDietLabels, "totalLandNeeded", myCropAreaHa + myAnimalAreaHa)

    myHtml  = _sectionTitle("Diet Summary")
    myHtml += (
        '<table width="100%" cellpadding="6" cellspacing="0" border="0" '
        'style="border-collapse:collapse; border:1px solid #C0CADD;">'
    )
    myHtml += _kvRow("MCals Person⁻¹ Year⁻¹", _fmtNum(myMCalsPerPersonYr, 1))
    myHtml += _kvRow("City MCals Year⁻¹",     _fmtNum(myCityMCalsYr, 0), _ROW_ALT)
    myHtml += _kvRow("Overall Plant Contribution", f"{myPlantPct:.2f}%")
    myHtml += "</table>"

    # MCals + Area combined table
    myHtml += '<br/>'
    myMCalRows = [
        ["Crops (Human + Animal)", _fmtNum(myCropMCals, 0),   _fmtNum(myCropAreaHa, 2)],
        ["Animals",                _fmtNum(myAnimalMCals, 0), _fmtNum(myAnimalAreaHa, 2)],
        ["Dairy",                  _fmtNum(myDairyMCals, 0),  "—"],
        ["Wild Meat",              _fmtNum(myWildAnimalMCals, 0), "—"],
        ["Wild Plants",            _fmtNum(myWildPlantMCals, 0),  "—"],
    ]
    myTotalMCals = myCropMCals + myAnimalMCals + myDairyMCals + myWildAnimalMCals + myWildPlantMCals
    myFooter = ["Total", _fmtNum(myTotalMCals, 0), _fmtNum(myTotalLandHa, 2)]
    myHtml += _styledTable(
        theHeaders=["Source", "MCals", "Area (Ha)"],
        theRows=myMCalRows,
        theFooter=myFooter,
        theNumericFromColumn=1,
    )

    if myDairySurplus > 0:
        myHtml += (
            f'<p style="color:{_MUTED}; font-style:italic; margin-top:6px;">'
            f"Dairy Surplus: {_fmtNum(myDairySurplus, 0)} MCals</p>"
        )

    return myHtml


def _selectionsPanel(model: "LaModel") -> str:
    """Mirror the thesis left panel: crop and animal selections with their %."""
    myHtml = _sectionTitle("Selections", _GREEN_HEADER_BG)

    # Two side-by-side tables: crops on the left, animals on the right.
    myCropRows: List[List[str]] = []
    for myCropGuid, myParamGuid in (getattr(model, "mCropsMap", {}) or {}).items():
        myCrop      = LaUtils.getCrop(myCropGuid)
        myCropParam = LaUtils.getCropParameter(myParamGuid) if myParamGuid else None
        myName  = myCrop.name if myCrop else "(unknown)"
        myShare = _safeAttr(myCropParam, "percentTameCrop", 0.0) if myCropParam else 0.0
        myCropRows.append([myName, f"{myShare:.2f}%"])

    myAnimalRows: List[List[str]] = []
    for myAnimalGuid, myParamGuid in (getattr(model, "mAnimalsMap", {}) or {}).items():
        myAnimal       = LaUtils.getAnimal(myAnimalGuid)
        myAnimalParam  = LaUtils.getAnimalParameter(myParamGuid) if myParamGuid else None
        myName  = myAnimal.name if myAnimal else "(unknown)"
        myShare = _safeAttr(myAnimalParam, "percentTameMeat", 0.0) if myAnimalParam else 0.0
        myAnimalRows.append([myName, f"{myShare:.2f}%"])

    myHtml += (
        '<table width="100%" cellpadding="0" cellspacing="10" border="0" '
        'style="border-collapse:separate;"><tr>'
        '<td valign="top" width="50%">'
    )
    myHtml += _styledTable(
        theHeaders=["Crop Selection", "Share"],
        theRows=myCropRows,
        theHeaderColor=_GREEN_HEADER_BG,
    )
    myHtml += '</td><td valign="top" width="50%">'
    myHtml += _styledTable(
        theHeaders=["Animal Selection", "Share"],
        theRows=myAnimalRows,
        theHeaderColor=_GREEN_HEADER_BG,
    )
    myHtml += '</td></tr></table>'

    # Settings sub-block (sliders + dairy)
    myMeatPct  = _safeAttr(model, "meatPercent", 0.0)
    myCropPct  = _safeAttr(model, "cropPercent", 0.0)
    myDietPct  = _safeAttr(model, "dietPercent", 0.0)
    myDairyUt  = _safeAttr(model, "dairyUtilisation", 0.0)
    myLimitOn  = bool(getattr(model, "limitDairy", False))
    myLimitPct = _safeAttr(model, "limitDairyPercent", 100.0)

    myHtml += '<br/>'
    myHtml += (
        '<table width="100%" cellpadding="6" cellspacing="0" border="0" '
        'style="border-collapse:collapse; border:1px solid #C0CADD;">'
    )
    myHtml += _kvRow("All Meat % (animal share of diet)", f"{myDietPct:.1f}%")
    myHtml += _kvRow("Domestic Animal Contribution",       f"{myMeatPct:.1f}%", _ROW_ALT)
    myHtml += _kvRow("Domestic Crop Contribution",         f"{myCropPct:.1f}%")
    myHtml += _kvRow("Dairy Utilisation",                  f"{myDairyUt:.1f}%", _ROW_ALT)
    myHtml += _kvRow("Dairy Limit", f"Limited to {myLimitPct:.0f}%" if myLimitOn else "Not Limited")
    myHtml += '</table>'

    return myHtml


def _dietCompositionPanel(model: "LaModel") -> str:
    """Two pie charts mirroring the thesis figure: top-level diet split
    (Plants / Meat / Dairy) and detailed breakdown."""
    myDietLabels = getattr(model, "mDietLabels", None)
    if not myDietLabels:
        return ""

    myPlantsPct      = _safeAttr(myDietLabels, "plantsPortionPct", 0.0)
    myDairyPct       = _safeAttr(myDietLabels, "dairyPortionPct", 0.0)
    myCropsPct       = _safeAttr(myDietLabels, "cropsPortionPct", 0.0)
    myTameMeatPct    = _safeAttr(myDietLabels, "tameMeatPortionPct", 0.0)
    myWildAnimalPct  = _safeAttr(myDietLabels, "wildAnimalPortionPct", 0.0)
    myWildPlantsPct  = _safeAttr(myDietLabels, "wildPlantsPortionPct", 0.0)
    myMeatPct        = myTameMeatPct + myWildAnimalPct

    myPiePlants = _chartPie(
        [
            ("Plants",  myPlantsPct,           _PALETTE_DIET[0]),
            ("Meat",    myMeatPct,             _PALETTE_DIET[1]),
            ("Dairy",   myDairyPct,            _PALETTE_DIET[2]),
        ],
        theSize=(4.0, 4.0),
    )
    myPieBreakdown = _chartPie(
        [
            ("Domestic Meat", myTameMeatPct,   _PALETTE_BREAKDOWN[0]),
            ("Wild Meat",     myWildAnimalPct, _PALETTE_BREAKDOWN[1]),
            ("Dairy",         myDairyPct,      _PALETTE_BREAKDOWN[2]),
            ("Wild Plants",   myWildPlantsPct, _PALETTE_BREAKDOWN[3]),
            ("Crops",         myCropsPct,      _PALETTE_BREAKDOWN[4]),
        ],
        theSize=(4.0, 4.0),
    )

    myHtml  = _sectionTitle("Diet Composition")
    myHtml += (
        '<table width="100%" cellpadding="10" cellspacing="0" border="0">'
        '<tr>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Diet Split</div>'
        f'{myPiePlants}</td>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Detailed Breakdown</div>'
        f'{myPieBreakdown}</td>'
        '</tr></table>'
    )
    return myHtml


def _dietCompositionTablePanel(model: "LaModel") -> str:
    """Tabular fallback for QTextBrowser mode (where SVG can't render)."""
    myDietLabels = getattr(model, "mDietLabels", None)
    if not myDietLabels:
        return ""

    myPlantsPct      = _safeAttr(myDietLabels, "plantsPortionPct", 0.0)
    myAnimalPct      = _safeAttr(myDietLabels, "animalPortionPct", 0.0)
    myDairyPct       = _safeAttr(myDietLabels, "dairyPortionPct", 0.0)
    myCropsPct       = _safeAttr(myDietLabels, "cropsPortionPct", 0.0)
    myTameMeatPct    = _safeAttr(myDietLabels, "tameMeatPortionPct", 0.0)
    myWildAnimalPct  = _safeAttr(myDietLabels, "wildAnimalPortionPct", 0.0)
    myWildPlantsPct  = _safeAttr(myDietLabels, "wildPlantsPortionPct", 0.0)

    myHtml  = _sectionTitle("Diet Composition")
    myHtml += _styledTable(
        theHeaders=["Top-level Split", "% of Diet"],
        theRows=[
            ["Plants",        f"{myPlantsPct:.2f}%"],
            ["Domestic Meat", f"{myTameMeatPct:.2f}%"],
            ["Dairy",         f"{myDairyPct:.2f}%"],
            ["Wild Meat",     f"{myWildAnimalPct:.2f}%"],
        ],
        theFooter=["Animal Total", f"{myAnimalPct + myDairyPct:.2f}%"],
    )
    myHtml += "<br/>"
    myHtml += _styledTable(
        theHeaders=["Plant Breakdown", "% of Diet"],
        theRows=[
            ["Domestic Crops", f"{myCropsPct:.2f}%"],
            ["Wild Plants",    f"{myWildPlantsPct:.2f}%"],
        ],
        theFooter=["Plant Total", f"{myPlantsPct:.2f}%"],
    )
    return myHtml


# ---------------------------------------------------------------------------
# Per-item target tables — Calorie, Production, Area × Crop, Animal
# ---------------------------------------------------------------------------
def toHtmlCalorieCropTargets(model: "LaModel") -> str:
    myCalMap = getattr(model.mDietLabels, "mCropCalorieKcalMap", None) or {}
    myTotal  = sum(myCalMap.values()) if myCalMap else 0.0

    myRows: List[List[str]] = []
    for myCropGuid, myKcal in myCalMap.items():
        myCrop = LaUtils.getCrop(myCropGuid)
        myName = myCrop.name if myCrop and myCrop.name else "Unknown"
        myPct  = (myKcal / myTotal * 100.0) if myTotal > 0 else 0.0
        myRows.append([myName, _fmtNum(myKcal, 0), f"{myPct:.1f}%"])

    myFooter = ["Total", _fmtNum(myTotal, 0), "100.0%"] if myRows else None
    myHtml  = _sectionTitle("Crop Calorie Targets")
    myHtml += _styledTable(
        theHeaders=["Crop", "Calories (kcal)", "% of Crop Total"],
        theRows=myRows or [["No crop calorie targets calculated", "", ""]],
        theFooter=myFooter,
    )
    return myHtml


def toHtmlCalorieAnimalTargets(model: "LaModel") -> str:
    myCalMap = getattr(model.mDietLabels, "mAnimalCalorieKcalMap", None) or {}
    myTotal  = sum(myCalMap.values()) if myCalMap else 0.0

    myRows: List[List[str]] = []
    for myAnimalGuid, myKcal in myCalMap.items():
        myAnimal = LaUtils.getAnimal(myAnimalGuid)
        myName   = myAnimal.name if myAnimal and myAnimal.name else "Unknown"
        myPct    = (myKcal / myTotal * 100.0) if myTotal > 0 else 0.0
        myRows.append([myName, _fmtNum(myKcal, 0), f"{myPct:.1f}%"])

    myFooter = ["Total", _fmtNum(myTotal, 0), "100.0%"] if myRows else None
    myHtml  = _sectionTitle("Animal Calorie Targets")
    myHtml += _styledTable(
        theHeaders=["Animal", "Calories (kcal)", "% of Animal Total"],
        theRows=myRows or [["No animal calorie targets calculated", "", ""]],
        theFooter=myFooter,
    )
    return myHtml


def toHtmlProductionCropTargets(model: "LaModel") -> str:
    myMap = getattr(model, "mProductionRequiredCropsMap", {}) or {}
    myRows: List[List[str]] = []
    myTotal = 0.0
    for myCropGuid, myKg in myMap.items():
        myCrop = LaUtils.getCrop(myCropGuid)
        myName = myCrop.name if myCrop else "Unknown"
        myRows.append([myName, _fmtNum(myKg, 0)])
        myTotal += float(myKg)

    myFooter = ["Total", _fmtNum(myTotal, 0)] if myRows else None
    myHtml  = _sectionTitle("Crop Production Targets")
    myHtml += _styledTable(
        theHeaders=["Crop", "Kilograms"],
        theRows=myRows or [["No crop production targets calculated", ""]],
        theFooter=myFooter,
    )
    return myHtml


def toHtmlProductionAnimalTargets(model: "LaModel") -> str:
    myMap = getattr(model, "mProductionRequiredAnimalsMap", {}) or {}
    myRows: List[List[str]] = []
    myTotal = 0.0
    for myAnimalGuid, myKg in myMap.items():
        myAnimal = LaUtils.getAnimal(myAnimalGuid)
        myName   = myAnimal.name if myAnimal else "Unknown"
        myRows.append([myName, _fmtNum(myKg, 0)])
        myTotal += float(myKg)

    myFooter = ["Total", _fmtNum(myTotal, 0)] if myRows else None
    myHtml  = _sectionTitle("Animal Production Targets")
    myHtml += _styledTable(
        theHeaders=["Animal", "Kilograms"],
        theRows=myRows or [["No animal production targets calculated", ""]],
        theFooter=myFooter,
    )
    return myHtml


def toHtmlAreaCropTargets(model: "LaModel") -> str:
    myMap = getattr(model, "mAreaTargetsCropsMap", {}) or {}
    myRows: List[List[str]] = []
    myTotal = 0.0
    for myCropGuid, myValue in myMap.items():
        if myCropGuid == "CommonTarget":
            continue
        myCrop = LaUtils.getCrop(myCropGuid)
        myName = myCrop.name if myCrop else "Unknown"
        myArea = float(myValue)
        myRows.append([myName, _fmtNum(myArea, 2)])
        myTotal += myArea

    myFooter = ["Total", _fmtNum(myTotal, 2)] if myRows else None
    myHtml  = _sectionTitle("Crop Area Targets")
    myHtml += _styledTable(
        theHeaders=["Crop", "Area (Ha)"],
        theRows=myRows or [["No crop area targets calculated", ""]],
        theFooter=myFooter,
    )
    return myHtml


def toHtmlAreaAnimalTargets(model: "LaModel") -> str:
    myMap = getattr(model, "mAreaTargetsAnimalsMap", {}) or {}
    myRows: List[List[str]] = []
    myTotal = 0.0
    for myAnimalGuid, myValue in myMap.items():
        if myAnimalGuid == "CommonTarget":
            continue
        myAnimal = LaUtils.getAnimal(myAnimalGuid)
        myName   = myAnimal.name if myAnimal else "Unknown"
        myArea   = float(myValue)
        myRows.append([myName, _fmtNum(myArea, 2)])
        myTotal += myArea

    myFooter = ["Total", _fmtNum(myTotal, 2)] if myRows else None
    myHtml  = _sectionTitle("Animal Area Targets")
    myHtml += _styledTable(
        theHeaders=["Animal", "Area (Ha)"],
        theRows=myRows or [["No animal area targets calculated", ""]],
        theFooter=myFooter,
    )
    return myHtml


# ---------------------------------------------------------------------------
# Chart panels — top-level functions called by the Run handler
# ---------------------------------------------------------------------------
def toHtmlMCalorieContributions(model: "LaModel") -> str:
    """Horizontal bar chart: Domestic Meat / Dairy / Wild Meat / Crops / Wild Plants."""
    myDietLabels = getattr(model, "mDietLabels", None)
    if not myDietLabels:
        return ""

    myMeat       = _safeAttr(myDietLabels, "animalMCalories", 0.0)
    myDairy      = _safeAttr(myDietLabels, "dairyMCalories", 0.0)
    myWildMeat   = _safeAttr(myDietLabels, "wildAnimalMCalories", 0.0)
    myCrops      = _safeAttr(myDietLabels, "cropMCalories", 0.0)
    myWildPlants = _safeAttr(myDietLabels, "wildPlantsMCalories", 0.0)

    myItems = [
        ("Domestic Meat", myMeat,       _PALETTE_BREAKDOWN[0]),
        ("Dairy",         myDairy,      _PALETTE_BREAKDOWN[2]),
        ("Wild Meat",     myWildMeat,   _PALETTE_BREAKDOWN[1]),
        ("Crops",         myCrops,      _PALETTE_BREAKDOWN[4]),
        ("Wild Plants",   myWildPlants, _PALETTE_BREAKDOWN[3]),
    ]

    myHtml  = _sectionTitle("MCalorie Contributions to the Overall Diet")
    myHtml += '<div style="padding:10px;">'
    myHtml += _chartHorizontalBars(myItems, theValueFmt="{:,.0f} MCals")
    myHtml += '</div>'
    return myHtml


def toHtmlHectaresLand(model: "LaModel") -> str:
    """Two vertical stacked bars: Hectares Grazing Land + Hectares Crop Land."""
    myAnimalAreaMap = getattr(model, "mAreaTargetsAnimalsMap", {}) or {}
    myCropAreaMap   = getattr(model, "mAreaTargetsCropsMap", {}) or {}

    myAnimalStacks: List[Tuple[str, float, str]] = []
    for myIndex, (myGuid, myValue) in enumerate(myAnimalAreaMap.items()):
        if myGuid == "CommonTarget":
            continue
        myAnimal = LaUtils.getAnimal(myGuid)
        myName   = myAnimal.name if myAnimal else "Unknown"
        myColor  = _PALETTE_ANIMALS[myIndex % len(_PALETTE_ANIMALS)]
        myAnimalStacks.append((myName, float(myValue), myColor))

    myCropStacks: List[Tuple[str, float, str]] = []
    for myIndex, (myGuid, myValue) in enumerate(myCropAreaMap.items()):
        if myGuid == "CommonTarget":
            continue
        myCrop  = LaUtils.getCrop(myGuid)
        myName  = myCrop.name if myCrop else "Unknown"
        myColor = _PALETTE_CROPS[myIndex % len(_PALETTE_CROPS)]
        myCropStacks.append((myName, float(myValue), myColor))

    myAnimalSvg = _chartStackedVerticalBar(
        myAnimalStacks, theUnitLabel="Hectares"
    )
    myCropSvg = _chartStackedVerticalBar(
        myCropStacks, theUnitLabel="Hectares"
    )

    myHtml  = _sectionTitle("Land Composition")
    myHtml += (
        '<table width="100%" cellpadding="10" cellspacing="0" border="0">'
        '<tr>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Hectares Grazing Land</div>'
        f'{myAnimalSvg}</td>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Hectares Crop Land</div>'
        f'{myCropSvg}</td>'
        '</tr></table>'
    )
    return myHtml


def toHtmlHerdCharts(model: "LaModel") -> str:
    """Two grouped bar charts: Animals per Hectare + Herd Sizes."""
    myHerdMap = getattr(model, "mAnimalHerdMap", {}) or {}
    myAreaMap = getattr(model, "mAreaTargetsAnimalsMap", {}) or {}

    if not myHerdMap:
        myHtml  = _sectionTitle("Herd Characteristics")
        myHtml += (
            f'<p style="color:{_MUTED}; font-style:italic; padding:10px;">'
            'Herd dynamics are only computed in Animals First / Dairy Separate '
            'mode. Switch to that mode to see Animals-per-Hectare and Herd-Size '
            'charts.</p>'
        )
        return myHtml

    myGuids       = list(myHerdMap.keys())
    myLabels      = [LaUtils.getAnimal(g).name if LaUtils.getAnimal(g) else "Unknown" for g in myGuids]
    myAdults      = [myHerdMap[g].get("adults",    0.0) for g in myGuids]
    myOffspring   = [myHerdMap[g].get("offspring", 0.0) for g in myGuids]
    myDensityAdults    = [(a / float(myAreaMap.get(g, 0)) if myAreaMap.get(g, 0) else 0.0)
                          for a, g in zip(myAdults, myGuids)]
    myDensityOffspring = [(o / float(myAreaMap.get(g, 0)) if myAreaMap.get(g, 0) else 0.0)
                          for o, g in zip(myOffspring, myGuids)]

    myAdultColor     = "#3F51B5"
    myOffspringColor = "#FF9800"

    myHerdSizesSvg = _chartGroupedBars(
        myLabels,
        [
            ("Adults",    myAdults,    myAdultColor),
            ("Offspring", myOffspring, myOffspringColor),
        ],
        theValueFmt="{:,.0f}",
    )
    myDensitySvg = _chartGroupedBars(
        myLabels,
        [
            ("Adults",    myDensityAdults,    myAdultColor),
            ("Offspring", myDensityOffspring, myOffspringColor),
        ],
        theValueFmt="{:,.1f}",
    )

    myHtml  = _sectionTitle("Herd Characteristics")
    myHtml += (
        '<table width="100%" cellpadding="10" cellspacing="0" border="0">'
        '<tr>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Herd Sizes</div>'
        f'{myHerdSizesSvg}</td>'
        f'<td align="center" valign="top" width="50%">'
        f'<div style="font-weight:bold; margin-bottom:6px;">Animals per Hectare</div>'
        f'{myDensitySvg}</td>'
        '</tr></table>'
    )
    return myHtml


# ---------------------------------------------------------------------------
# Full-report assembly — shared by the modal viewer and the PDF exporter
# ---------------------------------------------------------------------------
def buildFullReportHtml(model: "LaModel", theCalculationType: str = "") -> str:
    """Compose the complete thesis-style report HTML (tables + chart PNGs).

    Used by both the modal viewer (LaReportDialog) and the PDF exporter so
    they share the same source of truth. Includes basic styling and a
    wrapping <html>/<body> so it renders correctly through QTextBrowser
    and through QTextDocument.print_() to PDF.
    """
    return (
        "<html><head><meta charset='utf-8'><style>"
        "body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; "
        "       color: #222; }"
        "h1 { color: #3B5A8C; margin: 0 0 4px 0; }"
        "p.subtitle { color: #666; font-style: italic; margin: 0 0 12px 0; }"
        "</style></head><body>"
        "<h1>LanduseAnalyst Calculation Results</h1>"
        f"<p class='subtitle'>Calculation Method: {theCalculationType}</p>"
        + toHtml(model, theIncludeCharts=True)
        + toHtmlMCalorieContributions(model)
        + toHtmlCalorieCropTargets(model)
        + toHtmlCalorieAnimalTargets(model)
        + toHtmlProductionCropTargets(model)
        + toHtmlProductionAnimalTargets(model)
        + toHtmlAreaCropTargets(model)
        + toHtmlAreaAnimalTargets(model)
        + toHtmlHectaresLand(model)
        + toHtmlHerdCharts(model)
        + "</body></html>"
    )


# ---------------------------------------------------------------------------
# JSON serialization (for export)
# ---------------------------------------------------------------------------
def toDict(model: "LaModel") -> Dict:
    """Serialize the model + computed results to a plain-dict for JSON export.

    Keys use human-readable animal/crop names (resolved via LaUtils) rather
    than GUIDs so the export file is meaningful to a person reading it.
    """
    myDietLabels = getattr(model, "mDietLabels", None)

    def _resolveAnimals(theMap):
        myResult = {}
        for myGuid, myValue in (theMap or {}).items():
            if myGuid == "CommonTarget":
                myResult["__commonTarget"] = myValue
                continue
            myAnimal = LaUtils.getAnimal(myGuid)
            myName = myAnimal.name if myAnimal else myGuid
            myResult[myName] = myValue
        return myResult

    def _resolveCrops(theMap):
        myResult = {}
        for myGuid, myValue in (theMap or {}).items():
            if myGuid == "CommonTarget":
                myResult["__commonTarget"] = myValue
                continue
            myCrop = LaUtils.getCrop(myGuid)
            myName = myCrop.name if myCrop else myGuid
            myResult[myName] = myValue
        return myResult

    return {
        "settings": {
            "name":                   getattr(model, "name", ""),
            "period":                 getattr(model, "period", ""),
            "population":             int(_safeAttr(model, "population", 0)),
            "caloriesPerPersonDaily": int(_safeAttr(model, "caloriesPerPersonDaily", 0)),
            "dietPercent":            _safeAttr(model, "dietPercent", 0),
            "meatPercent":            _safeAttr(model, "meatPercent", 0),
            "cropPercent":            _safeAttr(model, "cropPercent", 0),
            "dairyUtilisation":       _safeAttr(model, "dairyUtilisation", 0),
            "baseOnPlants":           bool(getattr(model, "baseOnPlants", False)),
            "includeDairy":           bool(getattr(model, "includeDairy", False)),
            "limitDairy":             bool(getattr(model, "limitDairy", False)),
            "limitDairyPercent":      _safeAttr(model, "limitDairyPercent", 100),
        },
        "dietPortionPercent": {
            "plants":      _safeAttr(myDietLabels, "plantsPortionPct", 0),
            "animals":     _safeAttr(myDietLabels, "animalPortionPct", 0),
            "tameMeat":    _safeAttr(myDietLabels, "tameMeatPortionPct", 0),
            "wildMeat":    _safeAttr(myDietLabels, "wildAnimalPortionPct", 0),
            "dairy":       _safeAttr(myDietLabels, "dairyPortionPct", 0),
            "crops":       _safeAttr(myDietLabels, "cropsPortionPct", 0),
            "wildPlants":  _safeAttr(myDietLabels, "wildPlantsPortionPct", 0),
        },
        "mcalories": {
            "settlementAnnual": _safeAttr(myDietLabels, "megaCaloriesSettlementAnnual", 0),
            "perPersonAnnual":  _safeAttr(myDietLabels, "kiloCaloriesIndividualAnnual", 0),
            "crops":            _safeAttr(myDietLabels, "cropMCalories", 0),
            "animals":          _safeAttr(myDietLabels, "animalMCalories", 0),
            "dairy":            _safeAttr(myDietLabels, "dairyMCalories", 0),
            "wildMeat":         _safeAttr(myDietLabels, "wildAnimalMCalories", 0),
            "wildPlants":       _safeAttr(myDietLabels, "wildPlantsMCalories", 0),
            "dairySurplus":     _safeAttr(myDietLabels, "dairySurplusMCalories", 0),
        },
        "totalLandHa": _safeAttr(myDietLabels, "totalLandNeeded", 0),
        "crops": {
            "areaHa":     _resolveCrops(getattr(model, "mAreaTargetsCropsMap", {})),
            "productionKg": _resolveCrops(getattr(model, "mProductionRequiredCropsMap", {})),
            "calorieKcal":  _resolveCrops(getattr(myDietLabels, "mCropCalorieKcalMap", {})),
        },
        "animals": {
            "areaHa":     _resolveAnimals(getattr(model, "mAreaTargetsAnimalsMap", {})),
            "productionKg": _resolveAnimals(getattr(model, "mProductionRequiredAnimalsMap", {})),
            "calorieKcal":  _resolveAnimals(getattr(myDietLabels, "mAnimalCalorieKcalMap", {})),
            "herd":         _resolveAnimals(getattr(model, "mAnimalHerdMap", {})),
        },
    }


# ---------------------------------------------------------------------------
# Accessor helpers retained for compatibility
# ---------------------------------------------------------------------------
def getAreaTargetsAnimalsMap(model: "LaModel") -> Dict[str, float]:
    if hasattr(model, "mAreaTargetsAnimalsMap"):
        return model.mAreaTargetsAnimalsMap
    return {}


def getAreaTargetsCropsMap(model: "LaModel") -> Dict[str, float]:
    if hasattr(model, "mAreaTargetsCropsMap"):
        return model.mAreaTargetsCropsMap
    return {}
