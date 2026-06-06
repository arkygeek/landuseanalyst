# coding=utf-8
import unittest
import os
from qgis.PyQt.QtWidgets import QDialog
from la.gui.lacropparametermanager import LaCropParameterManager
from la.gui.laanimalparametermanager import LaAnimalParameterManager
from la.lib.lacropparameter import LaCropParameter
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lautils import LaUtils

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()

class LaGuiManagersTest(unittest.TestCase):
    def test_crop_parameter_manager_ui(self):
        """Test crop parameter manager dynamic UI elements and data flow."""
        manager = LaCropParameterManager(None)
        
        # Verify spinboxes are added
        self.assertTrue(hasattr(manager, "sbSlopeMin"))
        self.assertTrue(hasattr(manager, "sbSlopeMax"))
        self.assertEqual(manager.sbSlopeMin.suffix(), "°")
        self.assertEqual(manager.sbSlopeMax.suffix(), "°")

        # Test showing crop parameter updates spinbox values
        crop_param = LaCropParameter()
        crop_param.preferredSlopeMin = 2.5
        crop_param.preferredSlopeMax = 7.5
        
        manager.mCropParameter = crop_param
        manager.showCropParameter()
        
        self.assertEqual(manager.sbSlopeMin.value(), 2.5)
        self.assertEqual(manager.sbSlopeMax.value(), 7.5)
        
        # Test applying changes updates parameter values
        manager.sbSlopeMin.setValue(3.0)
        manager.sbSlopeMax.setValue(8.0)
        
        # Mocking toXmlFile to prevent writing during test
        original_to_xml = crop_param.toXmlFile
        crop_param.toXmlFile = lambda filepath: True
        
        manager.on_pbnApply_clicked()
        
        self.assertEqual(crop_param.preferredSlopeMin, 3.0)
        self.assertEqual(crop_param.preferredSlopeMax, 8.0)
        
        crop_param.toXmlFile = original_to_xml

    def test_animal_parameter_manager_ui(self):
        """Test animal parameter manager dynamic UI elements and data flow."""
        manager = LaAnimalParameterManager(None)
        
        # Verify spinboxes are added
        self.assertTrue(hasattr(manager, "sbSlopeMin"))
        self.assertTrue(hasattr(manager, "sbSlopeMax"))
        self.assertEqual(manager.sbSlopeMin.suffix(), "°")
        self.assertEqual(manager.sbSlopeMax.suffix(), "°")

        # Test showing animal parameter updates spinbox values
        animal_param = LaAnimalParameter()
        animal_param.preferredSlopeMin = 1.0
        animal_param.preferredSlopeMax = 12.0
        
        manager.mAnimalParameter = animal_param
        manager.showAnimalParameter()
        
        self.assertEqual(manager.sbSlopeMin.value(), 1.0)
        self.assertEqual(manager.sbSlopeMax.value(), 12.0)
        
        # Test applying changes updates parameter values
        manager.sbSlopeMin.setValue(2.0)
        manager.sbSlopeMax.setValue(14.0)
        
        # Mocking toXmlFile
        original_to_xml = animal_param.toXmlFile
        animal_param.toXmlFile = lambda filepath: True
        
        manager.on_pbnApply_clicked()
        
        self.assertEqual(animal_param.preferredSlopeMin, 2.0)
        self.assertEqual(animal_param.preferredSlopeMax, 14.0)
        
        animal_param.toXmlFile = original_to_xml

if __name__ == "__main__":
    suite = unittest.makeSuite(LaGuiManagersTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
