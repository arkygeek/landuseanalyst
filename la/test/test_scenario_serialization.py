# coding=utf-8
import os
import unittest
from qgis.PyQt.QtCore import QCoreApplication

from la.test.utilities import get_qgis_app
QGIS_APP = get_qgis_app()

from la.lib.lamodel import LaModel
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lautils import LaUtils


class TestScenarioSerialization(unittest.TestCase):
    def setUp(self):
        # Clear registries before test
        LaUtils.clearRegistries()
        self.model = LaModel()

    def tearDown(self):
        # Clean up
        LaUtils.clearRegistries()

    def test_export_import_roundtrip(self):
        # 1. Setup model properties
        self.model.mName = "Test Scenario"
        self.model.population = 450
        self.model.easting = 744800.0
        self.model.northing = 3611100.0
        self.model.caloriesPerPersonDaily = 2200
        self.model.includeDairy = True

        # 2. Setup mock Crop and CropParameter
        crop_guid = "crop-uuid-1234"
        crop = LaCrop()
        crop.setGuid(crop_guid)
        crop.name = "Spelt Wheat"
        crop.cropYield = 1200
        crop.cropCalories = 3400
        
        param_guid = "param-uuid-5678"
        param = LaCropParameter()
        param.setGuid(param_guid)
        param.name = "Spelt Param"
        param.cropGuid = crop_guid
        param.preferredSlopeMin = 1.0
        param.preferredSlopeMax = 8.5

        # Register in-memory so export can find them
        LaUtils.registerCrop(crop)
        LaUtils.registerCropParameter(param)

        # Select the crop in the model mapping
        self.model.mCropsMap = {crop_guid: param_guid}

        # 3. Setup mock Animal and AnimalParameter
        animal_guid = "animal-uuid-9999"
        animal = LaAnimal()
        animal.setGuid(animal_guid)
        animal.name = "Goat"
        
        animal_param_guid = "animal-param-uuid-8888"
        animal_param = LaAnimalParameter()
        animal_param.setGuid(animal_param_guid)
        animal_param.name = "Goat Param"
        animal_param.preferredSlopeMin = 0.0
        animal_param.preferredSlopeMax = 20.0

        # Register in-memory
        LaUtils.registerAnimal(animal)
        LaUtils.registerAnimalParameter(animal_param)

        # Select the animal in the model mapping
        self.model.mAnimalsMap = {animal_guid: animal_param_guid}

        # 4. Export the scenario XML
        xml_data = self.model.exportScenario()
        
        # Verify XML structure has main sections
        self.assertIn("<landuseAnalystScenario>", xml_data)
        self.assertIn(f'cropGuid="{crop_guid}"', xml_data)
        self.assertIn(f'animalGuid="{animal_guid}"', xml_data)
        self.assertIn("<cropParameter", xml_data)
        self.assertIn("<animalParameter", xml_data)

        # 5. Clear registries and mapping to ensure fresh load
        LaUtils.clearRegistries()
        new_model = LaModel()
        
        # Verify clearing worked
        empty_crop = LaUtils.getCrop(crop_guid)
        self.assertEqual(empty_crop.name, "No Name Set")

        # 6. Import XML into new model
        success = new_model.importScenario(xml_data)
        self.assertTrue(success)

        # 7. Assertions on model properties
        self.assertEqual(new_model.mName, "Test Scenario")
        self.assertEqual(new_model.population, 450)
        self.assertEqual(new_model.easting, 744800.0)
        self.assertEqual(new_model.northing, 3611100.0)
        self.assertEqual(new_model.caloriesPerPersonDaily, 2200)
        self.assertTrue(new_model.includeDairy)

        # 8. Assertions on selection maps
        self.assertEqual(new_model.mCropsMap, {crop_guid: param_guid})
        self.assertEqual(new_model.mAnimalsMap, {animal_guid: animal_param_guid})

        # 9. Assertions on restored registries in LaUtils
        restored_crop = LaUtils.getCrop(crop_guid)
        self.assertEqual(restored_crop.name, "Spelt Wheat")
        self.assertEqual(restored_crop.cropYield, 1200)
        self.assertEqual(restored_crop.cropCalories, 3400)
        
        restored_param = LaUtils.getCropParameter(param_guid)
        self.assertEqual(restored_param.name, "Spelt Param")
        self.assertEqual(restored_param.preferredSlopeMin, 1.0)
        self.assertEqual(restored_param.preferredSlopeMax, 8.5)

        restored_animal = LaUtils.getAnimal(animal_guid)
        self.assertEqual(restored_animal.name, "Goat")

        restored_animal_param = LaUtils.getAnimalParameter(animal_param_guid)
        self.assertEqual(restored_animal_param.name, "Goat Param")
        self.assertEqual(restored_animal_param.preferredSlopeMax, 20.0)


if __name__ == "__main__":
    unittest.main()
