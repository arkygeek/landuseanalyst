"""
lareports.py - HTML report generation for the Landuse Analyst plugin.

Produces a thesis-style report layout rendered by Qt's QTextBrowser.
Qt's rich-text engine only supports a subset of HTML/CSS, so the layout
uses tables, inline styles, and bgcolor attributes rather than flexbox/grid.
"""

from typing import Dict, List, Tuple, Optional
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
# Top-level "Model Settings" / Summary + Selections + Diet Composition
# ---------------------------------------------------------------------------
def toHtml(model: "LaModel") -> str:
    """Top section: scenario header, summary metrics, selections, diet composition."""
    myHtml = _scenarioHeader(model)
    myHtml += _summaryPanel(model)
    myHtml += _selectionsPanel(model)
    myHtml += _dietCompositionPanel(model)
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
    """Tabular replacement for the thesis pie charts."""
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
    myHtml += '<br/>'
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
