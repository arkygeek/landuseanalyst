"""
export_thesis_scenarios.py — write the 108 Jorgenson thesis scenarios as
``*.lascenario.json`` files plus the per-period parameter profiles they use.

The scenario grid (3 periods × min/max population × meat 10/20/30 % ×
dairy 0/50/100 % × feed/no-feed) is defined once, in the web app's
``backend/seed_thesis.py``; this script imports it so both products stay
in lock-step. Chalcolithic "with feed" scenarios reference the bundled
``testData/`` parameter profiles verbatim; every other combination gets a
derived profile (period-specific share, optional fodder) written under
``la/scenarios/thesis/profiles/`` with a deterministic GUID.

Run with the QGIS Python (needs qgis.PyQt for the XML classes)::

    QT_QPA_PLATFORM=offscreen python scripts/export_thesis_scenarios.py \\
        --web /home/arkygeek/Dev/LA/landuseanalyst-web
"""

import argparse
import json
import os
import sys
import uuid

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, _REPO)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

_NAMESPACE = uuid.UUID("6f1c2b2e-0a5c-4f0e-9a2d-3b7b5b4a1c11")  # stable GUIDs for derived profiles


def _deterministicGuid(theName: str) -> str:
    return str(uuid.uuid5(_NAMESPACE, theName))


def _slug(theText: str) -> str:
    return "".join(c.lower() if c.isalnum() else "_" for c in theText).strip("_")


def main() -> int:
    myParser = argparse.ArgumentParser(description=__doc__)
    myParser.add_argument("--web", required=True, help="path to the landuseanalyst-web checkout")
    myParser.add_argument("--out", default=os.path.join(_REPO, "la", "scenarios", "thesis"))
    myParser.add_argument("--profiles", default=os.path.join(_REPO, "testData"), help="catalogue profile root")
    myArgs = myParser.parse_args()

    sys.path.insert(0, os.path.abspath(myArgs.web))
    from qgis.PyQt.QtWidgets import QApplication
    myApp = QApplication.instance() or QApplication([])  # noqa: F841 - Qt needs an app for QObject models

    import backend.seed_thesis as mySeed
    from la.lib.lautils import LaUtils
    from la.lib.lacropparameter import LaCropParameter
    from la.lib.laanimalparameter import LaAnimalParameter
    from la.lib import lascenarioio

    myProfileRoot = os.path.abspath(myArgs.profiles)
    LaUtils.userDataPath = staticmethod(lambda: myProfileRoot)
    LaUtils.userSettingsDirPath = staticmethod(lambda: myProfileRoot)

    myCrops = {c.name: g for g, c in LaUtils.getAvailableCrops().items()}
    myAnimals = {a.name: g for g, a in LaUtils.getAvailableAnimals().items()}
    myCropParameters = LaUtils.getAvailableCropParameters()
    myAnimalParameters = LaUtils.getAvailableAnimalParameters()

    def _baseCropParameter(theCropName):
        myGuid = myCrops[theCropName]
        return next((g, p) for g, p in myCropParameters.items() if p.cropGuid == myGuid)

    def _baseAnimalParameter(theAnimalName):
        myGuid = myAnimals[theAnimalName]
        return next((g, p) for g, p in myAnimalParameters.items() if p.animalGuid == myGuid)

    myDerivedCropDir = os.path.join(myArgs.out, "profiles", "cropParameterProfiles")
    myDerivedAnimalDir = os.path.join(myArgs.out, "profiles", "animalParameterProfiles")
    os.makedirs(myDerivedCropDir, exist_ok=True)
    os.makedirs(myDerivedAnimalDir, exist_ok=True)
    myWrittenProfiles = 0

    def _cropParameterFor(thePeriod, theCropName):
        myBaseGuid, myBase = _baseCropParameter(theCropName)
        if thePeriod.key == "chalcolithic":
            return myBaseGuid, myBase.name, float(myBase.percentTameCrop)
        myName = f"{theCropName} · {thePeriod.label} params"
        myGuid = _deterministicGuid(myName)
        myDerived = LaCropParameter(myBase)
        myDerived.setGuid(myGuid)
        myDerived.mName = myName
        myDerived.mDescription = f"Thesis-derived parameter set for {theCropName} in the {thePeriod.label} period."
        myDerived.mPercentTameCrop = float(thePeriod.crops[theCropName])
        myPath = os.path.join(myDerivedCropDir, f"{myGuid}.xml")
        with open(myPath, "w", encoding="utf-8") as myFile:
            myFile.write("<?xml version='1.0' encoding='utf-8'?>\n" + myDerived.toXml())
        nonlocal myWrittenProfiles
        myWrittenProfiles += 1
        return myGuid, myName, myDerived.mPercentTameCrop

    def _animalParameterFor(thePeriod, theAnimalName, theWithFeed):
        myBaseGuid, myBase = _baseAnimalParameter(theAnimalName)
        if thePeriod.key == "chalcolithic" and theWithFeed:
            return myBaseGuid, myBase.name, float(myBase.percentTameMeat)
        myFeedLabel = "with feed" if theWithFeed else "no feed"
        myName = f"{theAnimalName} · {thePeriod.label} · {myFeedLabel}"
        myGuid = _deterministicGuid(myName)
        myDerived = LaAnimalParameter(myBase)
        myDerived.setGuid(myGuid)
        myDerived.mName = myName
        myDerived.mDescription = f"Thesis-derived for {theAnimalName} in {thePeriod.label} ({myFeedLabel})."
        myDerived.mPercentTameMeat = float(thePeriod.animals[theAnimalName])
        myDerived.mFodderUse = bool(theWithFeed)
        if not theWithFeed:
            myDerived.mFoodSourceMap = {}
        myPath = os.path.join(myDerivedAnimalDir, f"{myGuid}.xml")
        with open(myPath, "w", encoding="utf-8") as myFile:
            myFile.write("<?xml version='1.0' encoding='utf-8'?>\n" + myDerived.toXml())
        nonlocal myWrittenProfiles
        myWrittenProfiles += 1
        return myGuid, myName, myDerived.mPercentTameMeat

    myCount = 0
    myIndex = []
    for myPeriod in mySeed.PERIODS:
        mySetIndex = 0
        for myMeat in mySeed.MEAT_LEVELS:
            for myPop in (myPeriod.pop_min, myPeriod.pop_max):
                for myComboIdx, (myDairy, myFeed) in enumerate(mySeed.DAIRY_FEED_COMBOS):
                    myNumber = mySetIndex * 6 + myComboIdx + 1
                    myName = mySeed._scenarioName(myPeriod, myNumber, myPop, myMeat, myDairy, myFeed)
                    myCropRows = []
                    for myCropName in myPeriod.crops:
                        myGuid, myParameterName, myPercent = _cropParameterFor(myPeriod, myCropName)
                        myCropRows.append({"guid": myCrops[myCropName], "parameterGuid": myGuid,
                                           "name": myCropName, "parameterName": myParameterName,
                                           "percent": myPercent})
                    myAnimalRows = []
                    for myAnimalName in myPeriod.animals:
                        myGuid, myParameterName, myPercent = _animalParameterFor(myPeriod, myAnimalName, myFeed)
                        myAnimalRows.append({"guid": myAnimals[myAnimalName], "parameterGuid": myGuid,
                                             "name": myAnimalName, "parameterName": myParameterName,
                                             "percent": myPercent})
                    myDocument = {
                        "schemaVersion": lascenarioio.SCHEMA_VERSION,
                        "generator": "landuseanalyst-qgis/export_thesis_scenarios",
                        "scenario": {
                            "name": myName,
                            "description": (
                                f"Thesis Scenario #{myNumber} for the {myPeriod.label} period at Tell Esh Shuna North. "
                                f"Population {int(myPop):,}, meat-share-of-diet {int(myMeat)}%, dairy utilisation "
                                f"{int(myDairy)}% of potential, {'with' if myFeed else 'without'} 90-day supplementary feed. "
                                "Calc mode: Animals First, Dairy Separate (thesis-target)."),
                            "period": myPeriod.label,
                            "population": float(myPop),
                            "caloriesPerPersonDaily": 2500,
                            "dietPercentFromPlants": float(myMeat),   # web's misnamed animal share
                            "meatPercentTame": 99.0,
                            "cropPercentTame": 90.0,
                            "dairyUtilisation": float(myDairy),
                            "baseOnPlants": False,
                            "includeDairy": False,
                            "limitDairy": False,
                            "limitDairyPercent": None,
                            "calculationType": "animals_first_dairy_separate",
                            "settlementX": 744800.0,
                            "settlementY": 3611100.0,
                            "crsEpsg": 32636,
                            "precisionPct": 5,
                            "methodEuclidean": False,
                            "cropSlopeMaxDegrees": 9.0,
                            "grazingSlopeMaxDegrees": 15.0,
                            "targetHa": 0.0,
                            "demPath": "",
                            "suitabilityPath": "",
                        },
                        "crops": myCropRows,
                        "animals": myAnimalRows,
                        "plugin": {"catchmentEnabled": False, "distanceMethod": "WalkingTime",
                                   "commonLandValue": 0.0, "commonLandAreaUnits": "Hectare",
                                   "specificLandEnergyType": "KCalories"},
                    }
                    myFileName = f"shuna_{_slug(myPeriod.key)}_s{myNumber:02d}{lascenarioio.FILE_SUFFIX}"
                    with open(os.path.join(myArgs.out, myFileName), "w", encoding="utf-8") as myFile:
                        json.dump(myDocument, myFile, indent=2, ensure_ascii=False)
                    myIndex.append({"file": myFileName, "name": myName})
                    myCount += 1
                mySetIndex += 1
    with open(os.path.join(myArgs.out, "index.json"), "w", encoding="utf-8") as myFile:
        json.dump(myIndex, myFile, indent=2, ensure_ascii=False)
    print(f"wrote {myCount} scenarios and {myWrittenProfiles} derived parameter profiles to {myArgs.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
