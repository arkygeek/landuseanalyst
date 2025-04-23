# --- START OF FILE la/lib/lareports.py ---

from typing import Dict, Tuple
# Assuming la.lib.lautils contains LaUtils
# Assuming la.lib.laanimal contains LaAnimal
# Assuming la.lib.lacrop contains LaCrop
# Assuming la.lib.lamodel contains LaModel type hint (use forward reference if needed)

from la.lib.la import AreaUnits
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lamodel import LaModel

# Forward reference for type hint if LaModel imports this module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   from la.lib.lamodel import LaModel


def toHtmlCalorieCropTargets(model: 'LaModel') -> str:
    # --- Paste the content of LaModel.toHtmlCalorieCropTargets here ---
    # --- Remember to change 'self.' to 'model.' ---
    # --- Especially 'self.mDietLabels' to 'model.mDietLabels' ---
    """Generate HTML report for crop calorie targets."""
    myHtml = "<h3>Crop Calorie Targets</h3>"

    if not model.mDietLabels:
        return myHtml + "<p>No calculation results available</p>"

    myHtml += "<table border='1' cellpadding='4'>"
    myHtml += "<tr><th>Crop</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

    # Get crop calorie targets from mDietLabels if available
    myTotalCalories = 0
    myCropCalories = {}

    # Check for either cropCalorieTargets or mCropAreaTargetsMap
    # First check mCropAreaTargetsMap - this is available based on debug output
    if hasattr(model.mDietLabels, 'mCropAreaTargetsMap') and model.mDietLabels.mCropAreaTargetsMap:
        try:
            myCropCalories = {guid: float(area) * 1000 for guid, area in model.mDietLabels.mCropAreaTargetsMap.items()}
        except Exception as e:
            LaUtils.debug.log(f"Error processing mCropAreaTargetsMap: {str(e)}", "Warning")
    elif hasattr(model.mDietLabels, 'mCropAreaTargetsMap'):
        # If we have area targets but not calorie targets, we'll use area as a proxy
        myCropCalories = {guid: float(area) * 1000 for guid, area in model.mDietLabels.mCropAreaTargetsMap.items()}
    elif hasattr(model.mDietLabels, 'cropMCalories'):
        # Use cropMCalories if available (converted to kcal)
        try:
            # Convert PyQt property to string then float
            try:
                cropMCal = float(str(model.mDietLabels.cropMCalories))
            except Exception as e:
                LaUtils.debug.log(f"Error converting cropMCalories: {str(e)}", "Warning")
                cropMCal = 0.0
            # Distribute this evenly among crops if we have any crops
            if hasattr(model, 'mCropsMap') and model.mCropsMap:
                cropCount = len(model.mCropsMap)
                for cropGuid in model.mCropsMap.keys():
                    myCropCalories[cropGuid] = (cropMCal * 1000000) / cropCount  # Convert MCal to kcal and distribute
        except (TypeError, ValueError):
            # If conversion to float fails, use a default value
            LaUtils.debug.log("Could not convert cropMCalories to float", "Warning")

    myTotalCalories = sum(myCropCalories.values()) if myCropCalories else 0

    # Generate rows for each crop
    if myCropCalories:
        for myCropGuid, myCalories in myCropCalories.items():
            myCrop: LaCrop = LaUtils.getCrop(myCropGuid)
            myCropName = myCrop.name if myCrop and myCrop.name else "Unknown"
            myPercentage = (myCalories / myTotalCalories * 100) if myTotalCalories > 0 else 0
            myHtml += f"<tr><td>{myCropName}</td><td>{myCalories:,.0f}</td><td>{myPercentage:.1f}%</td></tr>"
    else:
        myHtml += "<tr><td colspan='3'>No crop calorie targets calculated</td></tr>"

    myHtml += "</table>"
    return myHtml

def toHtmlCalorieAnimalTargets(model: 'LaModel') -> str:
    """Generate HTML report for animal calorie targets."""
    myHtml = "<h3>Animal Calorie Targets</h3>"

    if not model.mDietLabels:
        return myHtml + "<p>No calculation results available</p>"

    myHtml += "<table border='1' cellpadding='4'>"
    myHtml += "<tr><th>Animal</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

    # Get animal calorie targets from mDietLabels if available
    myTotalCalories = 0
    myAnimalCalories = {}

    # Check for mAnimalAreaTargetsMap since it exists in the actual object
    if hasattr(model.mDietLabels, 'mAnimalAreaTargetsMap') and model.mDietLabels.mAnimalAreaTargetsMap:
        try:
            myAnimalCalories = {guid: float(area) * 1000 for guid, area in model.mDietLabels.mAnimalAreaTargetsMap.items()}
        except Exception as e:
            LaUtils.debug.log(f"Error processing mAnimalAreaTargetsMap: {str(e)}", "Warning")
    # Also try animalMCalories if it exists
    elif hasattr(model.mDietLabels, 'animalMCalories'):
        try:
            animalMCal = float(str(model.mDietLabels.animalMCalories))
            # Distribute this evenly among animals if we have any
            if hasattr(model, 'mAnimalsMap') and model.mAnimalsMap:
                animalCount = len(model.mAnimalsMap)
                for animalGuid in model.mAnimalsMap.keys():
                    myAnimalCalories[animalGuid] = (animalMCal * 1000000) / animalCount  # Convert MCal to kcal
        except Exception as e:
            LaUtils.debug.log(f"Error processing animalMCalories: {str(e)}", "Warning")
        myTotalCalories = sum(myAnimalCalories.values()) if myAnimalCalories else 0

    # Generate rows for each animal
    if myAnimalCalories:
        for myAnimalGuid, myCalories in myAnimalCalories.items():
            myAnimal: LaAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalName = myAnimal.name if myAnimal and myAnimal.name else "Unknown"
            myPercentage = (myCalories / myTotalCalories * 100) if myTotalCalories > 0 else 0
            myHtml += f"<tr><td>{myAnimalName}</td><td>{myCalories:,.0f}</td><td>{myPercentage:.1f}%</td></tr>"
    else:
        myHtml += "<tr><td colspan='3'>No animal calorie targets calculated</td></tr>"

    myHtml += "</table>"
    return myHtml

def toHtmlProductionCropTargets(model: 'LaModel') -> str:
    """
    Generate HTML report for crop production targets.
    This method returns a string containing the production
    targets for each crop from mProductionRequiredCropsMap
    """
    myString = "<h3> Crop Production Targets</h3>\n"
    myString += "<P STYLE=\"margin-bottom: 0in\"><BR>\n"
    myString += "\n"
    myString += "<table>"
    myString += "  <COL WIDTH=64*>\n"
    myString += "  <COL WIDTH=16*>\n"
    myString += "  <tr>\n"
    myString += "    <th>\n"
    myString += "      Crop\n"
    myString += "    </th>\n"
    myString += "    <th>\n"
    myString += "      Kg\n"
    myString += "    </th>\n"
    myString += "  </tr>\n"

    # Python equivalent of QMapIterator over mProductionRequiredCropsMap
    if hasattr(model, 'mProductionRequiredCropsMap'):
        for myCropGuid, myValue in model.mProductionRequiredCropsMap.items():
            myProductionTarget = float(myValue)
            myCrop = LaUtils.getCrop(myCropGuid)
            myCropParameter = LaUtils.getCropParameter(model.mCropsMap.get(myCropGuid, ""))
            # add to the string to create the xml file
            myString += "  <tr>\n"
            myString += "    <td>\n"
            myString += "      " + LaUtils.xmlEncode(myCrop.name) + "\n"
            myString += "    </td>\n"
            myString += "    <td>\n"
            myString += "      " + str(myProductionTarget) + "\n"
            myString += "    </td>\n"
            myString += "  </tr>\n"

    myString += "</table>\n"
    return myString

def toHtmlProductionAnimalTargets(model: 'LaModel') -> str:
    """
    Generate HTML report for animal production targets.
    This method returns a string containing the production
    targets for each animal from mProductionRequiredAnimalsMap
    """
    myString = "<h3> Animal Production Targets</h3>\n"
    myString += "<P STYLE=\"margin-bottom: 0in\"><BR>\n"
    myString += "\n"
    myString += "<table>"
    myString += "  <COL WIDTH=64*>\n"
    myString += "  <COL WIDTH=16*>\n"
    myString += "  <tr>\n"
    myString += "    <th>\n"
    myString += "      Animal\n"
    myString += "    </th>\n"
    myString += "    <th>\n"
    myString += "      Kg\n"
    myString += "    </th>\n"
    myString += "  </tr>\n"

    # Python equivalent of QMapIterator over mProductionRequiredAnimalsMap
    if hasattr(model, 'mProductionRequiredAnimalsMap'):
        for myAnimalGuid, myValue in model.mProductionRequiredAnimalsMap.items():
            myProductionTarget = float(myValue)
            myAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalParameter = LaUtils.getAnimalParameter(model.mAnimalsMap.get(myAnimalGuid, ""))
            # add to the string to create the xml file
            myString += "  <tr>\n"
            myString += "    <td>\n"
            myString += "      " + LaUtils.xmlEncode(myAnimal.name) + "\n"
            myString += "    </td>\n"
            myString += "    <td>\n"
            myString += "      " + str(myProductionTarget) + "\n"
            myString += "    </td>\n"
            myString += "  </tr>\n"

    myString += "</table>\n"
    return myString

def toHtmlAreaCropTargets(model: 'LaModel') -> str:
    """
    Generate HTML report for crop area targets.
    This method returns a string containing the area
    targets for each crop from mAreaTargetsCropsMap
    """
    # Loop through the mAreaTargetsCropsMap
    myString = "<h3> Crop Area Targets</h3>\n"
    myString += "<P STYLE=\"margin-bottom: 0in\"><BR>\n"
    myString += "\n"
    myString += "<table>"
    myString += "  <COL WIDTH=64*>\n"
    myString += "  <COL WIDTH=16*>\n"
    myString += "  <tr>\n"
    myString += "    <th>\n"
    myString += "      Crop\n"
    myString += "    </th>\n"
    myString += "    <th>\n"
    myString += "      Area\n"
    myString += "    </th>\n"
    myString += "  </tr>\n"

    # Python equivalent of QMapIterator over mAreaTargetsCropsMap
    if hasattr(model, 'mAreaTargetsCropsMap'):
        for myCropGuid, myValue in model.mAreaTargetsCropsMap.items():
            if myCropGuid != "CommonTarget":
                myAreaTarget = float(myValue)
                myCrop = LaUtils.getCrop(myCropGuid)
                myCropParameter = LaUtils.getCropParameter(model.mCropsMap.get(myCropGuid, ""))
                # add to the string to create the xml file
                myString += "  <tr>\n"
                myString += "    <td>\n"
                myString += "      " + LaUtils.xmlEncode(myCrop.name) + "\n"
                myString += "    </td>\n"
                myString += "    <td>\n"
                myString += "      " + str(myAreaTarget) + "\n"
                myString += "    </td>\n"
                myString += "  </tr>\n"
            else:
                myAreaTarget = str(model.mAreaTargetsCropsMap.get("CommonTarget", 0))
                myString += "  <tr>\n"
                myString += "    <td>\n"
                myString += "      CommonTarget\n"
                myString += "    </td>\n"
                myString += "    <td>\n"
                myString += "      " + myAreaTarget + "\n"
                myString += "    </td>\n"
                myString += "  </tr>\n"

    myString += "</table>\n"
    return myString

def toHtmlAreaAnimalTargets(model: 'LaModel') -> str:
    from la.lib.la import AreaUnits
    """
    Generate HTML report for animal area targets.
    This method returns a string containing the area
    targets for each animal from mAreaTargetsAnimalsMap
    """
    # Loop through the mAreaTargetsAnimalsMap
    myString = "<h3> Animal Area Targets</h3>\n"
    myString += "\n"
    myString += "<table>"
    myString += "  <tr>\n"
    myString += "    <th>\n"
    myString += "      Animal\n"
    myString += "    </th>\n"
    myString += "    <th>\n"
    myString += "      Area\n"
    myString += "    </th>\n"
    myString += "  </tr>\n"

    # Python equivalent of QMapIterator over mAreaTargetsAnimalsMap
    if hasattr(model, 'mAreaTargetsAnimalsMap'):
        for myAnimalGuid, myValue in model.mAreaTargetsAnimalsMap.items():
            if myAnimalGuid != "CommonTarget":
                myAreaTargetUnchanged = float(str(myValue))
                myAnimal = LaUtils.getAnimal(myAnimalGuid)
                myAnimalParameter = LaUtils.getAnimalParameter(model.mAnimalsMap.get(myAnimalGuid, ""))
                # For units, convert PyQt property to string and then to enum
                myUnitStr = str(myAnimalParameter.areaUnits)
                try:
                    myUnitEnum: AreaUnits = AreaUnits[myUnitStr]
                    myAreaTarget = LaUtils.convertAreaToHectares(myUnitEnum, int(myAreaTargetUnchanged))
                except (KeyError, ValueError):
                    # Fallback if conversion fails
                    myAreaTarget = myAreaTargetUnchanged
                # add to the string to create the xml file
                myString += "  <tr>\n"
                myString += "    <td>\n"
                myString += "      " + LaUtils.xmlEncode(myAnimal.name) + "\n"
                myString += "    </td>\n"
                myString += "    <td>\n"
                myString += "      " + str(myAreaTarget) + "\n"
                myString += "    </td>\n"
                myString += "  </tr>\n"
            else:
                myAreaTarget = str(model.mAreaTargetsAnimalsMap.get("CommonTarget", 0))
                myString += "  <tr>\n"
                myString += "    <td>\n"
                myString += "      CommonTarget\n"
                myString += "    </td>\n"
                myString += "    <td>\n"
                myString += "      " + myAreaTarget + "\n"
                myString += "    </td>\n"
                myString += "  </tr>\n"

    myString += "</table>\n"
    return myString

def toHtml(model: 'LaModel') -> str:
    # --- Paste the content of LaModel.toHtml here ---
    # --- Remember to change 'self.' to 'model.' ---
    """Generate HTML report for the model."""
    html = f"<h3>Model Settings</h3>"
    html += "<table border='1' cellpadding='4'>"
    html += f"<tr><td><b>Population:</b></td><td>{model.population}</td></tr>"
    html += f"<tr><td><b>Calories per person per day:</b></td><td>{model.caloriesPerPersonDaily}</td></tr>"

    method = "Plants First" if model.baseOnPlants else "Animals First"
    dairy = "Included in Calculation" if model.includeDairy else "Calculated Separately"
    dairy_limit = f"Limited to {model.limitDairyPercent}%" if model.limitDairy else "Not Limited"

    html += f"<tr><td><b>Calculation Method:</b></td><td>{method}</td></tr>"
    html += f"<tr><td><b>Dairy:</b></td><td>{dairy}</td></tr>"
    html += f"<tr><td><b>Dairy Limit:</b></td><td>{dairy_limit}</td></tr>"
    html += "</table>"

    return html

def getAreaTargetsAnimalsMap(model: 'LaModel') -> Dict[str, float]:
    """
    Get the animal area targets map from the model.

    Args:
        model: The LaModel instance containing the area targets

    Returns:
        A dictionary mapping animal GUIDs to their area targets
    """
    if hasattr(model, 'mAreaTargetsAnimalsMap'):
        return model.mAreaTargetsAnimalsMap
    return {}

def getAreaTargetsCropsMap(model: 'LaModel') -> Dict[str, float]:
    """
    Get the crop area targets map from the model.

    Args:
        model: The LaModel instance containing the area targets

    Returns:
        A dictionary mapping crop GUIDs to their area targets
    """
    if hasattr(model, 'mAreaTargetsCropsMap'):
        return model.mAreaTargetsCropsMap
    return {}
