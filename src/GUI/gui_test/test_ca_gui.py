import unittest

from PySide6 import QtWidgets

from src.GUI.code.CA_GUI import Ui_CA


class TestUiCA(unittest.TestCase):
    def setUp(self):
        """Set up the application and the UI before each test."""
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CA()
        self.ui.setupUi(self.window)

    def test_window_title(self):
        """Test if the window title is set correctly."""
        self.assertEqual(self.window.windowTitle(), "CA Experiment Creator")

    def test_labels_exist(self):
        """Test if all labels are created and have the correct text."""
        self.assertIsNotNone(self.ui.rest_time_label)
        self.assertIsNotNone(self.ui.experiment_type_label)
        self.assertIsNotNone(self.ui.experiment_time_label)
        self.assertIsNotNone(self.ui.general_parameters_label)
        self.assertIsNotNone(self.ui.output_filename_label)
        self.assertIsNotNone(self.ui.step_number_label)
        self.assertIsNotNone(self.ui.experiment_parameters_label)
        self.assertIsNotNone(self.ui.voltage_label)

        self.assertEqual(self.ui.rest_time_label.text(),
                         '<html><head/><body><p align="center">Rest Time</p></body></html>')
        self.assertEqual(self.ui.experiment_type_label.text(),
                         '<html><head/><body><p align="center">Experiment Type</p></body></html>')
        self.assertEqual(self.ui.experiment_time_label.text(),
                         '<html><head/><body><p align="center">Experiment Time</p></body></html>')
        self.assertEqual(self.ui.general_parameters_label.text(),
                         '<html><head/><body><p align="center">General Parameters</p></body></html>')
        self.assertEqual(self.ui.output_filename_label.text(),
                         '<html><head/><body><p align="center">Output Filename</p></body></html>')
        self.assertEqual(self.ui.step_number_label.text(),
                         '<html><head/><body><p align="center">Step Number</p></body></html>')
        self.assertEqual(self.ui.experiment_parameters_label.text(),
                         '<html><head/><body><p align="center">Experiment Parameters</p></body></html>')
        self.assertEqual(self.ui.voltage_label.text(),
                         '<html><head/><body><p align="center">Voltage</p></body></html>')

    def test_line_edits_exist(self):
        """Test if all line edit fields are created."""
        self.assertIsNotNone(self.ui.experiment_step_number)
        self.assertIsNotNone(self.ui.experiment_time)
        self.assertIsNotNone(self.ui.experiment_voltage)
        self.assertIsNotNone(self.ui.experiment_rest_time)
        self.assertIsNotNone(self.ui.experiment_file_name)
        self.assertIsNotNone(self.ui.experiment_file_path)
        self.assertIsNotNone(self.ui.experiment_duration)

    def test_buttons_exist(self):
        """Test if all buttons are created."""
        self.assertIsNotNone(self.ui.select_output_filepath_button)
        self.assertIsNotNone(self.ui.advanced_parameters_button)
        self.assertIsNotNone(self.ui.save_experiment_file_button)
        self.assertIsNotNone(self.ui.generate_preview_button)

        self.assertEqual(self.ui.select_output_filepath_button.text(), "Output Filepath")
        self.assertEqual(self.ui.advanced_parameters_button.text(), "Advanced Parameters")
        self.assertEqual(self.ui.save_experiment_file_button.text(), "Save Experiment File")
        self.assertEqual(self.ui.generate_preview_button.text(), "Generate Preview")

    def tearDown(self):
        """Clean up after each test."""
        self.window.close()


if __name__ == "__main__":
    unittest.main()
