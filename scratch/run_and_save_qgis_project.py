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
        
        from qgis.core import QgsCoordinateReferenceSystem
        crs = QgsCoordinateReferenceSystem("EPSG:32636")
        myProject.setCrs(crs)
        
        # 1. Add DEM
        myDemLayer = QgsRasterLayer(myWindowedDem, "Shuna DEM")
        myDemLayer.setCrs(crs)
        myProject.addMapLayer(myDemLayer)
        
        # 2. Add Cost Surface
        myCostLayer = None
        if myResults.costRasterPath and os.path.exists(myResults.costRasterPath):
            myCostLayer = QgsRasterLayer(myResults.costRasterPath, "Cost Surface (Walking Time)")
            myCostLayer.setCrs(crs)
            myProject.addMapLayer(myCostLayer)
            myCostLayer.setOpacity(0.55)
            
        # 3. Add Catchment Output
        myLayer = None
        myItem = myResults.items[0]
        if myItem.outputPath and os.path.exists(myItem.outputPath):
            myLayer = QgsRasterLayer(myItem.outputPath, f"WheatTest (achieved {myItem.achievedHa:.1f} Ha / target {myItem.targetHa:.1f} Ha)")
            myLayer.setCrs(crs)
            myProject.addMapLayer(myLayer)
            
            # Apply transparent blue style
            _QML_STYLE = os.path.join(_PROJECT_ROOT, "la", "resources", "styles", "catchment_mask.qml")
            if os.path.exists(_QML_STYLE):
                myLayer.loadNamedStyle(_QML_STYLE)
                myLayer.triggerRepaint()
        
        # Save project
        myProjectPath = os.path.join(_PROJECT_ROOT, "shuna_results.qgs")
        myProject.write(myProjectPath)
        print(f"SUCCESS: Saved raw QGIS project to {myProjectPath}")
        
        # Post-process XML to ensure canvas extent and CRS are correctly saved
        import xml.etree.ElementTree as ET
        
        print(f"Post-processing QGIS project XML at {myProjectPath}...")
        tree = ET.parse(myProjectPath)
        root = tree.getroot()
        
        # Helper to set UTM 36N SRS details on a spatialrefsys element
        def set_utm_srs(spatialrefsys):
            if spatialrefsys is None:
                return
            wkt_text = (
                'PROJCRS["WGS 84 / UTM zone 36N",'
                'BASEGEOGCRS["WGS 84",'
                'ENSEMBLE["World Geodetic System 1984 ensemble",MEMBER["World Geodetic System 1984 (Transit)"],MEMBER["World Geodetic System 1984 (G730)"],MEMBER["World Geodetic System 1984 (G873)"],MEMBER["World Geodetic System 1984 (G1150)"],MEMBER["World Geodetic System 1984 (G1674)"],MEMBER["World Geodetic System 1984 (G1762)"],MEMBER["World Geodetic System 1984 (G2139)"],ELLIPSOID["WGS 84",6378137,298.257223563,LENGTHUNIT["metre",1]],ENSEMBLEACCURACY[2.0]],'
                'PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433]],'
                'CS[ellipsoidal,2],'
                'AXIS["geodetic latitude (Lat)",north,ORDER[1],ANGLEUNIT["degree",0.0174532925199433]],'
                'AXIS["geodetic longitude (Lon)",east,ORDER[2],ANGLEUNIT["degree",0.0174532925199433]],'
                'USAGE[SCOPE["Horizontal component of 3D system."],AREA["World."],BBOX[-90,-180,90,180]],'
                'ID["EPSG",4326]],'
                'CONVERSION["UTM zone 36N",'
                'METHOD["Transverse Mercator",ID["EPSG",9807]],'
                'PARAMETER["Latitude of natural origin",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8801]],'
                'PARAMETER["Longitude of natural origin",33,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8802]],'
                'PARAMETER["Scale factor at natural origin",0.9996,SCALEUNIT["unity",1],ID["EPSG",8805]],'
                'PARAMETER["False easting",500000,LENGTHUNIT["metre",1],ID["EPSG",8806]],'
                'PARAMETER["False northing",0,LENGTHUNIT["metre",1],ID["EPSG",8807]],'
                'CS[Cartesian,2],'
                'AXIS["easting (E)",east,ORDER[1],LENGTHUNIT["metre",1]],'
                'AXIS["northing (N)",north,ORDER[2],LENGTHUNIT["metre",1]],'
                'USAGE[SCOPE["Engineering survey, topographic mapping."],AREA["Between 30°E and 36°E, northern hemisphere. Cyprus. Egypt. Eritrea. Ethiopia. Greece. Iraq. Israel. Jordan. Kenya. Lebanon. Saudi Arabia. Somalia. Sudan. Syria. Turkey. Uganda. Ukraine."],BBOX[0,30,84,36]],'
                'ID["EPSG",32636]]'
            )
            
            for child_name, val in [
                ("wkt", wkt_text),
                ("proj4", "+proj=utm +zone=36 +datum=WGS84 +units=m +no_defs"),
                ("srsid", "3120"),
                ("srid", "32636"),
                ("authid", "EPSG:32636"),
                ("description", "WGS 84 / UTM zone 36N"),
                ("projectionacronym", "utm"),
                ("ellipsoidacronym", "EPSG:7030"),
                ("geographicflag", "false")
            ]:
                el = spatialrefsys.find(child_name)
                if el is None:
                    el = ET.SubElement(spatialrefsys, child_name)
                el.text = val

        # Update projectCrs
        project_crs = root.find("projectCrs")
        if project_crs is None:
            project_crs = ET.SubElement(root, "projectCrs")
        spatialrefsys = project_crs.find("spatialrefsys")
        if spatialrefsys is None:
            spatialrefsys = ET.SubElement(project_crs, "spatialrefsys", nativeFormat="Wkt")
        set_utm_srs(spatialrefsys)

        # Update each layer's srs
        for layer in root.findall(".//maplayer"):
            srs = layer.find("srs")
            if srs is None:
                srs = ET.SubElement(layer, "srs")
            layer_srs_sys = srs.find("spatialrefsys")
            if layer_srs_sys is None:
                layer_srs_sys = ET.SubElement(srs, "spatialrefsys", nativeFormat="Wkt")
            set_utm_srs(layer_srs_sys)

        # Update mapcanvas extent and units
        mapcanvas = root.find("mapcanvas")
        if mapcanvas is None:
            mapcanvas = ET.SubElement(root, "mapcanvas", annotationsVisible="1", name="")
        
        units = mapcanvas.find("units")
        if units is None:
            units = ET.SubElement(mapcanvas, "units")
        units.text = "meters"
        
        extent = mapcanvas.find("extent")
        if extent is None:
            extent = ET.SubElement(mapcanvas, "extent")
        
        # Clear existing extent child elements and rebuild them
        for child in list(extent):
            extent.remove(child)
            
        xmin = ET.SubElement(extent, "xmin")
        xmin.text = "741793.00000000000000000"
        ymin = ET.SubElement(extent, "ymin")
        ymin.text = "3608100.99999812431633472"
        xmax = ET.SubElement(extent, "xmax")
        xmax.text = "747793.00000254344195127"
        ymax = ET.SubElement(extent, "ymax")
        ymax.text = "3614100.99999836552888155"

        tree.write(myProjectPath, encoding="UTF-8", xml_declaration=True)
        print(f"SUCCESS: Post-processed and saved QGIS project to {myProjectPath}")
        
    finally:
        lautils.LaUtils.getCrop = myOriginalGetCrop
        lautils.LaUtils.getCropParameter = myOriginalGetCropParameter

if __name__ == "__main__":
    main()
