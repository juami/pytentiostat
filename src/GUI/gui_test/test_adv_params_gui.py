import unittest

from PySide6 import QtWidgets

from src.GUI.code.Adv_params_GUI import Ui_Adv_Params


class TestUiAdvParams(unittest.TestCase):
    def setUp(self):
        """Set up the application and the UI before each test."""
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Adv_Params()
        self.ui.setupUi(self.window)

    def test_window_title(self):
        """Test if the window title is set correctly."""
        self.assertEqual(self.window.windowTitle(), "Adv Params")

    def test_labels_exist(self):
        """Test if all labels are created and have the correct text."""
        self.assertIsNotNone(self.ui.experiment_conversion_factor_label)
        self.assertIsNotNone(self.ui.experiment_averag_number_label)
        self.assertIsNotNone(self.ui.experiment_shunt_resistor_label)
        self.assertIsNotNone(self.ui.advanced_parameters_label)
        self.assertIsNotNone(self.ui.experiment_setpoint_gain_label)
        self.assertIsNotNone(self.ui.experiment_setpoint_offset_label)
        self.assertIsNotNone(self.ui.experiment_time_step_label)

        self.assertEqual(self.ui.experiment_conversion_factor_label.text(),
                         '<html><head/><body><p align="center">Conversion Factor</p></body></html>')
        self.assertEqual(self.ui.experiment_averag_number_label.text(),
                         '<html><head/><body><p align="center">Average Number</p></body></html>')
        self.assertEqual(self.ui.experiment_shunt_resistor_label.text(),
                         '<html><head/><body><p align="center">Shunt Resistor /mohm</p></body></html>')
        self.assertEqual(self.ui.advanced_parameters_label.text(),
                         '<html><head/><body><p align="center">Advanced Parameters</p></body></html>')
        self.assertEqual(self.ui.experiment_setpoint_gain_label.text(),
                         '<html><head/><body><p align="center">Setpoint Gain</p></body></html>')
        self.assertEqual(self.ui.experiment_setpoint_offset_label.text(),
                         '<html><head/><body><p align="center">Setpoint Offset</p></body></html>')
        self.assertEqual(self.ui.experiment_time_step_label.text(),
                         '<html><head/><body><p align="center">Time Step /s</p></body></html>')

    def test_line_edits_exist(self):
        """Test if all line edit fields are created."""
        self.assertIsNotNone(self.ui.experiment_setpoint_gain)
        self.assertIsNotNone(self.ui.experiment_shunt_resistor)
        self.assertIsNotNone(self.ui.experiment_setpoint_offset)
        self.assertIsNotNone(self.ui.experiment_time_step)
        self.assertIsNotNone(self.ui.experiment_averag_number)
        self.assertIsNotNone(self.ui.experiment_conversion_factor)

    def test_save_button_exists(self):
        """Test if the save button is created."""
        self.assertIsNotNone(self.ui.save_experiment_file_button)
        self.assertEqual(self.ui.save_experiment_file_button.text(), "Save ")

    def tearDown(self):
        """Clean up after each test."""
        self.window.close()


if __name__ == "__main__":
    unittest.main()
