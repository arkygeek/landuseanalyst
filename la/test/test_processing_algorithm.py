# coding=utf-8
import os
import shutil
import tempfile
import unittest

from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsRasterLayer,
    QgsPointXY,
    QgsCoordinateReferenceSystem
)

from la.test.utilities import get_qgis_app
QGIS_APP = get_qgis_app()

# Initialize QGIS Processing framework
from processing.core.Processing import Processing
Processing.initialize()

from la.processing.la_processing_provider import LaProcessingProvider
from la.lib.lamodel import LaModel
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.lautils import LaUtils


class TestProcessingAlgorithm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provider = LaProcessingProvider()
        QgsApplication.processingRegistry().addProvider(cls.provider)

    @classmethod
    def tearDownClass(cls):
        QgsApplication.processingRegistry().removeProvider(cls.provider)

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        
        # Paths
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.shuna_dem_path = os.path.join(self.test_dir, "xmlData", "GrassData", "demShuna")
        
        # Create a small windowed DEM so r.walk runs fast
        self.windowed_dem_path = os.path.join(self.temp_dir, "windowed_dem.tif")
        self._windowDem(self.shuna_dem_path, self.windowed_dem_path)
        
        # Load layers
        self.dem_layer = QgsRasterLayer(self.windowed_dem_path, "DEM")
        QgsProject.instance().addMapLayer(self.dem_layer)
        
        # Setup scenario XML
        self.xml_path = os.path.join(self.temp_dir, "test_scenario.xml")
        self._createTestScenario(self.xml_path)

    def tearDown(self):
        QgsProject.instance().removeMapLayer(self.dem_layer.id())
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        LaUtils.clearRegistries()

    def _windowDem(self, source_path, out_path):
        from osgeo import gdal
        ds = gdal.Open(source_path)
        gt = ds.GetGeoTransform()
        proj = ds.GetProjection()
        dem = ds.GetRasterBand(1).ReadAsArray()
        
        # Center UTM 36N coordinates: 744800, 3611100
        center_col = int((744800.0 - gt[0]) / gt[1])
        center_row = int((3611100.0 - gt[3]) / gt[5])
        
        win_size = 50  # Very small size for rapid unit testing
        half = win_size // 2
        col_start = center_col - half
        row_start = center_row - half
        window = dem[row_start:row_start + win_size, col_start:col_start + win_size]
        
        new_gt = (
            gt[0] + col_start * gt[1], gt[1], 0.0,
            gt[3] + row_start * gt[5], 0.0, gt[5],
        )
        
        out_ds = gdal.GetDriverByName("GTiff").Create(
            out_path, win_size, win_size, 1, gdal.GDT_Float32,
            options=["COMPRESS=LZW", "TILED=YES"],
        )
        out_ds.SetGeoTransform(new_gt)
        out_ds.SetProjection(proj)
        out_ds.GetRasterBand(1).WriteArray(window)
        out_ds.FlushCache()

    def _createTestScenario(self, out_path):
        # Create a simple scenario containing a single crop with a target area of 50.0 Ha
        model = LaModel()
        model.mName = "Headless Test Scenario"
        model.population = 100
        model.easting = 744800.0
        model.northing = 3611100.0
        model.caloriesPerPersonDaily = 2500
        model.baseOnPlants = True
        model.includeDairy = False
        model.precision = 5
        
        # Setup mock Crop and CropParameter
        crop_guid = "crop-uuid-1"
        crop = LaCrop()
        crop.setGuid(crop_guid)
        crop.name = "WheatTest"
        crop.cropYield = 1000
        crop.cropCalories = 3000
        
        param_guid = "param-uuid-1"
        param = LaCropParameter()
        param.setGuid(param_guid)
        param.name = "WheatTestParam"
        param.cropGuid = crop_guid
        param.percentTameCrop = 100.0
        param.preferredSlopeMin = 0.0
        param.preferredSlopeMax = 10.0
        
        # Register in-memory so serialization works
        LaUtils.registerCrop(crop)
        LaUtils.registerCropParameter(param)
        
        model.mCropsMap = {crop_guid: param_guid}
        
        xml_data = model.exportScenario()
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(xml_data)

    def test_catchment_algorithm_execution(self):
        import processing
        
        # Outputs
        cost_path = os.path.join(self.temp_dir, "cost_surface.tif")
        out_folder = os.path.join(self.temp_dir, "catchments")
        os.makedirs(out_folder, exist_ok=True)
        
        params = {
            'INPUT_DEM': self.dem_layer.id(),
            'INPUT_SETTLEMENT': '744800.0,3611100.0',
            'INPUT_PROFILE': self.xml_path,
            'OUTPUT_COST': cost_path,
            'OUTPUT_FOLDER': out_folder
        }
        
        # Execute
        print("\n--- Running processing.run ---")
        try:
            res = processing.run("la:catchment", params)
            print(f"Result dictionary: {res}")
        except Exception as e:
            print(f"Exception during processing.run: {e}")
            raise
            
        print(f"Temp dir contents: {os.listdir(self.temp_dir)}")
        if os.path.exists(out_folder):
            print(f"Out folder contents: {os.listdir(out_folder)}")
            
        self.assertIsNotNone(res)
        self.assertTrue(os.path.exists(cost_path), f"Cost path {cost_path} does not exist.")
        self.assertTrue(os.path.exists(out_folder))
        
        # Verify catchment output GeoTIFF was generated inside the folder
        files = os.listdir(out_folder)
        self.assertTrue(any(f.startswith("WheatTest_") and f.endswith(".tif") for f in files))
