"""
lascenarioio.py — scenario files (``*.lascenario.json``) shared with the web app.

Layout (``schemaVersion`` 1)::

    {
      "schemaVersion": 1,
      "scenario": { ...web ScenarioWrite field names... },
      "crops":    [{"guid", "parameterGuid", "name", "parameterName", "percent"}],
      "animals":  [ ...same shape... ],
      "plugin":   { layer sources and engine options only the plugin uses },
      "results":  { optional RunRead-shaped summary of the last calculation }
    }

The ``scenario`` block uses the web API's names verbatim so
``toWebPayload()`` can be POSTed to ``/scenarios``. One naming trap is
documented inline: the web column ``dietPercentFromPlants`` is *misnamed* —
its engine reads it as the share of calories from animals (identical to the
plugin's ``mDietPercent``), so the value is copied, not inverted.
"""

import json
import os
from typing import Dict, List, Optional, Tuple

from la.lib.la import AreaUnits, EnergyType
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils

SCHEMA_VERSION = 1
FILE_SUFFIX = ".lascenario.json"


def calculationTypeKey(theModel: LaModel) -> str:
    """Web ``CalculationType`` value for the model's flags."""
    myFirst = "plants_first" if theModel.mBaseOnPlants else "animals_first"
    myDairy = "include_dairy" if theModel.mIncludeDairy else "dairy_separate"
    return f"{myFirst}_{myDairy}"


def _minSlopeCap(theParameters) -> Optional[float]:
    myCaps = [float(p.slopeMaxDegrees) for p in theParameters if getattr(p, "applySlopeLimit", True)]
    return min(myCaps) if myCaps else None


def toDict(theModel: LaModel, theSelectedCrops: Dict[str, str], theSelectedAnimals: Dict[str, str],
           thePluginBlock: Optional[Dict] = None, theResults: Optional[Dict] = None) -> Dict:
    """
    Serialise a scenario.

    :param theModel: The model holding population / diet / settlement inputs.
    :param theSelectedCrops: ``cropGuid → cropParameterGuid``.
    :param theSelectedAnimals: ``animalGuid → animalParameterGuid``.
    :param thePluginBlock: Plugin-only runtime settings (layer sources, engine options).
    :param theResults: Optional results summary (see :func:`resultsBlock`).
    """
    myCrops: List[Dict] = []
    myCropParameters = []
    for myGuid, myParameterGuid in theSelectedCrops.items():
        myCrop = LaUtils.getCrop(myGuid)
        myParameter = LaUtils.getCropParameter(myParameterGuid) if myParameterGuid else None
        if myParameter is not None and myParameter.name:
            myCropParameters.append(myParameter)
        myCrops.append({
            "guid": myGuid,
            "parameterGuid": myParameterGuid,
            "name": getattr(myCrop, "name", ""),
            "parameterName": getattr(myParameter, "name", "") if myParameter else "",
            "percent": float(getattr(myParameter, "percentTameCrop", 0.0) or 0.0) if myParameter else 0.0,
        })
    myAnimals: List[Dict] = []
    myAnimalParameters = []
    for myGuid, myParameterGuid in theSelectedAnimals.items():
        myAnimal = LaUtils.getAnimal(myGuid)
        myParameter = LaUtils.getAnimalParameter(myParameterGuid) if myParameterGuid else None
        if myParameter is not None and myParameter.name:
            myAnimalParameters.append(myParameter)
        myAnimals.append({
            "guid": myGuid,
            "parameterGuid": myParameterGuid,
            "name": getattr(myAnimal, "name", ""),
            "parameterName": getattr(myParameter, "name", "") if myParameter else "",
            "percent": float(getattr(myParameter, "percentTameMeat", 0.0) or 0.0) if myParameter else 0.0,
        })

    myScenario = {
        "name": theModel.mName,
        "description": theModel.mDescription or "",
        "period": theModel.mPeriod,
        "population": float(theModel.mPopulation),
        "caloriesPerPersonDaily": int(theModel.mCaloriesPerPersonDaily),
        # Misnamed on the web (see module docstring): this IS the animal share.
        "dietPercentFromPlants": float(theModel.mDietPercent),
        "meatPercentTame": float(theModel.mMeatPercent),
        "cropPercentTame": float(theModel.mPercentOfDietThatIsFromCrops),
        "dairyUtilisation": float(theModel.mDairyUtilisation),
        "baseOnPlants": bool(theModel.mBaseOnPlants),
        "includeDairy": bool(theModel.mIncludeDairy),
        "limitDairy": bool(theModel.mLimitDairy),
        "limitDairyPercent": float(theModel.mLimitDairyPercentage) if theModel.mLimitDairy else None,
        "calculationType": calculationTypeKey(theModel),
        "settlementX": float(theModel.mEasting),
        "settlementY": float(theModel.mNorthing),
        "crsEpsg": int(theModel.mProjection or 0),
        "precisionPct": int(theModel.mPrecision or 5),
        "methodEuclidean": bool(theModel.mEuclideanDistance),
        # Web caps are scenario-wide; the most restrictive per-item cap is the lossless-enough mapping.
        "cropSlopeMaxDegrees": _minSlopeCap(myCropParameters),
        "grazingSlopeMaxDegrees": _minSlopeCap(myAnimalParameters),
        "targetHa": 0.0,
        "demPath": "",
        "suitabilityPath": "",
    }
    myDocument = {
        "schemaVersion": SCHEMA_VERSION,
        "generator": "landuseanalyst-qgis",
        "scenario": myScenario,
        "crops": myCrops,
        "animals": myAnimals,
        "plugin": dict(thePluginBlock or {}),
    }
    myDocument["plugin"].setdefault("commonLandValue", float(theModel.mCommonLandValue or 0.0))
    myDocument["plugin"].setdefault("commonLandAreaUnits", theModel.mCommonLandAreaUnits.name)
    myDocument["plugin"].setdefault("specificLandEnergyType", theModel.mSpecificLandEnergyType.name)
    if theResults:
        myDocument["results"] = theResults
    return myDocument


def resultsBlock(theModel: LaModel, theCalculationType: str = "") -> Optional[Dict]:
    """RunRead-shaped summary of the last diet calculation, or None when there is none."""
    myLabels = getattr(theModel, "mDietLabels", None)
    if myLabels is None or not theModel.mAreaTargetsCropsMap and not theModel.mAreaTargetsAnimalsMap:
        return None
    myCropHa = float(sum(theModel.mAreaTargetsCropsMap.values()))
    myGrazingHa = float(sum(theModel.mAreaTargetsAnimalsMap.values()))
    return {
        "calculationType": calculationTypeKey(theModel),
        "calculationLabel": theCalculationType,
        "mcalSettlementAnnual": float(myLabels.megaCaloriesSettlementAnnual),
        "mcalPerPersonAnnual": float(myLabels.kiloCaloriesIndividualAnnual),
        "mcalCrops": float(myLabels.cropMCalories),
        "mcalAnimals": float(myLabels.animalMCalories),
        "mcalDairy": float(myLabels.dairyMCalories),
        "mcalWildMeat": float(myLabels.wildAnimalMCalories),
        "mcalWildPlants": float(myLabels.wildPlantsMCalories),
        "mcalDairySurplus": float(myLabels.dairySurplusMCalories),
        "dietPlantsPct": float(myLabels.plantsPortionPct),
        "dietAnimalsPct": float(myLabels.animalPortionPct),
        "dietTameMeatPct": float(myLabels.tameMeatPortionPct),
        "dietWildMeatPct": float(myLabels.wildAnimalPortionPct),
        "dietDairyPct": float(myLabels.dairyPortionPct),
        "dietCropsPct": float(myLabels.cropsPortionPct),
        "dietWildPlantsPct": float(myLabels.wildPlantsPortionPct),
        "totalLandHa": myCropHa + myGrazingHa,
        "cropLandHa": myCropHa,
        "grazingLandHa": myGrazingHa,
        "fallowAreaHa": float(sum((getattr(theModel, "mAreaTargetsCropsFallowMap", {}) or {}).values())),
        "fallowMcalPool": float(getattr(theModel, "mFallowMCalPool", 0.0) or 0.0),
        "fallowMcalAllocated": float(getattr(theModel, "mFallowMCalAllocated", 0.0) or 0.0),
        "items": [
            {"itemType": "crop", "guid": g, "name": LaUtils.getCrop(g).name, "areaHa": float(v),
             "sownAreaHa": float((getattr(theModel, "mAreaTargetsCropsSownMap", {}) or {}).get(g, v)),
             "fallowAreaHa": float((getattr(theModel, "mAreaTargetsCropsFallowMap", {}) or {}).get(g, 0.0))}
            for g, v in theModel.mAreaTargetsCropsMap.items()
        ] + [
            {"itemType": "animal", "guid": g, "name": LaUtils.getAnimal(g).name, "areaHa": float(v)}
            for g, v in theModel.mAreaTargetsAnimalsMap.items()
        ],
    }


def fromDict(theDocument: Dict) -> Tuple[LaModel, Dict[str, str], Dict[str, str], Dict]:
    """
    Rebuild ``(model, selectedCrops, selectedAnimals, pluginBlock)`` from a document.

    Unknown crop/animal GUIDs are resolved by name against the local catalogue
    (the web keys by database id, so a file from the web carries names).
    :raises ValueError: when the document is not a Landuse Analyst scenario.
    """
    if not isinstance(theDocument, dict) or "scenario" not in theDocument:
        raise ValueError("Not a Landuse Analyst scenario file (missing 'scenario' block).")
    myVersion = int(theDocument.get("schemaVersion", 1))
    if myVersion > SCHEMA_VERSION:
        raise ValueError(f"Scenario schema {myVersion} is newer than this plugin understands ({SCHEMA_VERSION}).")
    myScenario = theDocument["scenario"]
    myModel = LaModel()
    myModel.mName = str(myScenario.get("name", "") or "")
    myModel.mDescription = str(myScenario.get("description", "") or "")
    myModel.mPeriod = str(myScenario.get("period", "") or "")
    myModel.mPopulation = int(round(float(myScenario.get("population") or 100)))
    myModel.mCaloriesPerPersonDaily = int(myScenario.get("caloriesPerPersonDaily") or 2500)
    myModel.mDietPercent = int(round(float(myScenario.get("dietPercentFromPlants") or 0)))
    myModel.mMeatPercent = int(round(float(myScenario.get("meatPercentTame") or 0)))
    myModel.mPercentOfDietThatIsFromCrops = int(round(float(myScenario.get("cropPercentTame") or 0)))
    myModel.mDairyUtilisation = int(round(float(myScenario.get("dairyUtilisation") or 0)))
    myModel.mBaseOnPlants = bool(myScenario.get("baseOnPlants", False))
    myModel.mIncludeDairy = bool(myScenario.get("includeDairy", False))
    myModel.mLimitDairy = bool(myScenario.get("limitDairy", False))
    if myScenario.get("limitDairyPercent") is not None:
        myModel.mLimitDairyPercentage = int(round(float(myScenario["limitDairyPercent"])))
    myCalcType = str(myScenario.get("calculationType") or "")
    if myCalcType:
        myModel.mBaseOnPlants = myCalcType.startswith("plants_first")
        myModel.mIncludeDairy = myCalcType.endswith("include_dairy")
    myModel.mEasting = int(round(float(myScenario.get("settlementX") or 0)))
    myModel.mNorthing = int(round(float(myScenario.get("settlementY") or 0)))
    myModel.mProjection = int(myScenario.get("crsEpsg") or 0)
    myModel.mPrecision = int(myScenario.get("precisionPct") or 5)
    myModel.mEuclideanDistance = bool(myScenario.get("methodEuclidean", False))
    myModel.mWalkingTime = not myModel.mEuclideanDistance

    myPlugin = dict(theDocument.get("plugin") or {})
    myUnitsName = str(myPlugin.get("commonLandAreaUnits", "Hectare"))
    myUnits = AreaUnits[myUnitsName] if myUnitsName in AreaUnits.__members__ else AreaUnits.Hectare
    if myPlugin.get("commonLandValue") is not None:
        myModel.setCommonLandValue(float(myPlugin["commonLandValue"]), myUnits)
    myEnergyName = str(myPlugin.get("specificLandEnergyType", "KCalories"))
    if myEnergyName in EnergyType.__members__:
        myModel.mSpecificLandEnergyType = EnergyType[myEnergyName]

    mySelectedCrops = _resolveSelections(
        theDocument.get("crops") or [], LaUtils.getAvailableCrops(), LaUtils.getAvailableCropParameters(), "cropGuid")
    mySelectedAnimals = _resolveSelections(
        theDocument.get("animals") or [], LaUtils.getAvailableAnimals(), LaUtils.getAvailableAnimalParameters(), "animalGuid")
    return myModel, mySelectedCrops, mySelectedAnimals, myPlugin


def _resolveSelections(theRows: List[Dict], theItems: Dict, theParameters: Dict, theLinkAttr: str) -> Dict[str, str]:
    myByName = {str(getattr(i, "name", "")).lower(): g for g, i in theItems.items()}
    mySelected: Dict[str, str] = {}
    for myRow in theRows:
        myGuid = str(myRow.get("guid") or "")
        if myGuid not in theItems:
            myGuid = myByName.get(str(myRow.get("name", "")).lower(), "")
        if not myGuid:
            continue
        myParameterGuid = str(myRow.get("parameterGuid") or "")
        if myParameterGuid not in theParameters:
            myCandidates = {g: p for g, p in theParameters.items() if str(getattr(p, theLinkAttr, "")) == myGuid}
            myWanted = str(myRow.get("parameterName", "")).lower()
            myParameterGuid = next((g for g, p in myCandidates.items() if str(p.name).lower() == myWanted), "")
            if not myParameterGuid:
                myParameterGuid = next(iter(myCandidates), "")
        mySelected[myGuid] = myParameterGuid
    return mySelected


def toWebPayload(theDocument: Dict) -> Dict:
    """The ``scenario`` block only, ready for ``POST /scenarios`` on the web API."""
    return dict(theDocument["scenario"])


def saveFile(thePath: str, theDocument: Dict) -> str:
    myPath = thePath if thePath.endswith(FILE_SUFFIX) or thePath.endswith(".json") else thePath + FILE_SUFFIX
    with open(myPath, "w", encoding="utf-8") as myFile:
        json.dump(theDocument, myFile, indent=2, ensure_ascii=False)
    return myPath


def loadFile(thePath: str) -> Dict:
    with open(thePath, "r", encoding="utf-8") as myFile:
        return json.load(myFile)


def defaultFileName(theModel: LaModel) -> str:
    myName = theModel.mName or "scenario"
    mySafe = "".join(c if c.isalnum() or c in "-_." else "_" for c in str(myName)).strip("_") or "scenario"
    return os.path.join(os.path.expanduser("~"), mySafe + FILE_SUFFIX)
