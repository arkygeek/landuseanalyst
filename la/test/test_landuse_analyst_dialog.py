# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'jjorgenson@gmail.com'
__date__ = '2022-03-22'
__copyright__ = 'Copyright 2022, Dr. Jason S. Jorgenson'

import unittest

from qgis.PyQt.QtWidgets import QDialogButtonBox, QDialog

from la.gui.lamainform import LaMainForm

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()


class LaMainFormTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = LaMainForm(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""
        self.dialog.accept()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        self.dialog.pushButtonExit.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

    def test_thesis_scenarios_ui(self):
        """Test that Jorgenson Thesis Scenarios and Shuna Demo UI works."""
        # 1. Assert grpThesis, cboThesisScenarios, and buttons exist
        self.assertTrue(hasattr(self.dialog, 'grpThesis'))
        self.assertTrue(hasattr(self.dialog, 'cboThesisScenarios'))
        self.assertTrue(hasattr(self.dialog, 'btnLoadThesisScenario'))
        self.assertTrue(hasattr(self.dialog, 'btnLoadShunaLayers'))

        # 2. Assert that the scenarios are loaded into the combobox
        scenario_count = self.dialog.cboThesisScenarios.count()
        self.assertEqual(scenario_count, 108)

        # 3. Test loading a scenario (e.g., S01 Chalcolithic)
        self.dialog.cboThesisScenarios.setCurrentIndex(0)
        scenario_name = self.dialog.cboThesisScenarios.currentText()
        self.assertIn("Chalcolithic", scenario_name)
        self.assertIn("S01", scenario_name)

        # Trigger load scenario
        self.dialog.on_btnLoadThesisScenario_clicked()

        # Verify model values loaded correctly
        self.assertEqual(self.dialog.mModel.population, 100)
        self.assertEqual(self.dialog.mModel.dietPercent, 10)
        self.assertEqual(self.dialog.mModel.dairyUtilisation, 0)
        self.assertTrue(self.dialog.mModel.includeDairy)

    def test_load_shuna_data(self):
        """Test loading Shuna rasters into the QGIS project."""
        from qgis.core import QgsProject
        
        # Clear existing layers first
        QgsProject.instance().removeAllMapLayers()
        
        # Trigger load Shuna layers
        self.dialog.on_btnLoadShunaLayers_clicked()
        
        # Check that Shuna DEM and Shuna Suitability layers are added
        layers = QgsProject.instance().mapLayers()
        names = [layer.name() for layer in layers.values()]
        self.assertIn("Shuna DEM", names)
        self.assertIn("Shuna Suitability", names)

if __name__ == "__main__":
    suite = unittest.makeSuite(LaMainFormTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


