import os
import sys
import numpy as np
from osgeo import gdal

# Setup paths
_TEST_DIR = "/home/arkygeek/Dev/LA/landuseanalyst/la/test"
_PROJECT_ROOT = "/home/arkygeek/Dev/LA/landuseanalyst"
sys.path.insert(0, _PROJECT_ROOT)
sys.path.insert(0, _TEST_DIR)

from la.test.utilities import get_qgis_app
QGIS_APP = get_qgis_app()

from qgis.core import QgsProject, QgsRasterLayer
from la.test.test_lacatchment_shuna import (
    _windowDem, _buildSuitabilityRaster, _StubCrop, _StubParameter,
    _StubModel, _DemLayer, SETTLEMENT_X, SETTLEMENT_Y, _SHUNA_DEM,
    _SCRATCH_DIR, _TARGET_HA, _PRECISION
)
from la.lib.lagrass import LaGrass
from la.lib.lacatchment import LaCatchment, LaCatchmentInputs, DistanceMethod
from la.lib import lautils

def main():
    os.makedirs(_SCRATCH_DIR, exist_ok=True)
    myWindowedDem = _windowDem(_SHUNA_DEM, os.path.join(_SCRATCH_DIR, "windowedDem.tif"))
    mySuit = _buildSuitabilityRaster(myWindowedDem, os.path.join(_SCRATCH_DIR, "suitWheatTest.tif"))

    myCropGuid = "test-crop-guid-1"
    myParameterGuid = "test-param-guid-1"
    myCropsByGuid = {myCropGuid: _StubCrop("WheatTest")}
    myParamsByGuid = {myParameterGuid: _StubParameter("WheatTestParam", mySuit, False)}
    
    myOriginalGetCrop = lautils.LaUtils.getCrop
    myOriginalGetCropParameter = lautils.LaUtils.getCropParameter

    try:
        lautils.LaUtils.getCrop = staticmethod(lambda theGuid: myCropsByGuid.get(theGuid))
        lautils.LaUtils.getCropParameter = staticmethod(lambda theGuid: myParamsByGuid.get(theGuid))

        myModel = _StubModel(
            theEasting=SETTLEMENT_X,
            theNorthing=SETTLEMENT_Y,
            theCropsMap={myCropGuid: myParameterGuid},
            theCropTargets={myCropGuid: _TARGET_HA},
            thePrecision=_PRECISION,
        )
        myGrass = LaGrass(_DemLayer(myWindowedDem), _SCRATCH_DIR)
        myCatchment = LaCatchment(myGrass, _PRECISION)
        myInputs = LaCatchmentInputs(
            demLayerId="",
            commonCropLayerId=None,
            commonGrazingLayerId=None,
            method=DistanceMethod.WalkingTime,
        )
        myResults = myCatchment.runCatchmentAnalysis(myModel, myInputs)
        
        # Now create the QGIS project
        myProject = QgsProject.instance()
        myProject.clear()
        
        # 1. Add DEM
        myDemLayer = QgsRasterLayer(myWindowedDem, "Shuna DEM")
        myProject.addMapLayer(myDemLayer)
        
        # 2. Add Cost Surface
        if myResults.costRasterPath and os.path.exists(myResults.costRasterPath):
            myCostLayer = QgsRasterLayer(myResults.costRasterPath, "Cost Surface (Walking Time)")
            myProject.addMapLayer(myCostLayer)
            myCostLayer.setOpacity(0.55)
            
        # 3. Add Catchment Output
        myItem = myResults.items[0]
        if myItem.outputPath and os.path.exists(myItem.outputPath):
            myLayer = QgsRasterLayer(myItem.outputPath, f"WheatTest (achieved {myItem.achievedHa:.1f} Ha / target {myItem.targetHa:.1f} Ha)")
            myProject.addMapLayer(myLayer)
            
            # Apply transparent blue style
            _QML_STYLE = os.path.join(_PROJECT_ROOT, "la", "resources", "styles", "catchment_mask.qml")
            if os.path.exists(_QML_STYLE):
                myLayer.loadNamedStyle(_QML_STYLE)
                myLayer.triggerRepaint()
        
        # Save project
        myProjectPath = os.path.join(_PROJECT_ROOT, "shuna_results.qgs")
        myProject.write(myProjectPath)
        print(f"SUCCESS: Saved QGIS project to {myProjectPath}")
        
    finally:
        lautils.LaUtils.getCrop = myOriginalGetCrop
        lautils.LaUtils.getCropParameter = myOriginalGetCropParameter

if __name__ == "__main__":
    main()
