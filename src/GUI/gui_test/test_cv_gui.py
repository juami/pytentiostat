import unittest

from PySide6 import QtWidgets

from src.GUI.code.CV_GUI import Ui_CV


class TestUiCV(unittest.TestCase):
    def setUp(self):
        """Set up the application and the UI before each test."""
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CV()
        self.ui.setupUi(self.window)

    def test_window_title(self):
        """Test if the window title is set correctly."""
        self.assertEqual(self.window.windowTitle(), "CV Experiment Creator")

    def test_labels_exist(self):
        """Test if all labels are created and have the correct text."""
        self.assertIsNotNone(self.ui.rest_time_label)
        self.assertIsNotNone(self.ui.experiment_type_label)
        self.assertIsNotNone(self.ui.output_filename_label)
        self.assertIsNotNone(self.ui.step_number_label)
        self.assertIsNotNone(self.ui.sweep_rate_label)
        self.assertIsNotNone(self.ui.first_vertex_voltage_label)
        self.assertIsNotNone(self.ui.second_vertex_voltage_label)
        self.assertIsNotNone(self.ui.start_voltage_label)
        self.assertIsNotNone(self.ui.cycle_number_label)
        self.assertIsNotNone(self.ui.experiment_parameters_label)

        self.assertEqual(self.ui.rest_time_label.text(),
                         '<html><head/><body><p align="center">Rest Time</p></body></html>')
        self.assertEqual(self.ui.experiment_type_label.text(),
                         '<html><head/><body><p align="center">Experiment Type</p></body></html>')
        self.assertEqual(self.ui.output_filename_label.text(),
                         '<html><head/><body><p align="center">Output Filename</p></body></html>')
        self.assertEqual(self.ui.step_number_label.text(),
                         '<html><head/><body><p align="center">Step Number</p></body></html>')
        self.assertEqual(self.ui.sweep_rate_label.text(),
                         '<html><head/><body><p align="center">Sweep Rate</p></body></html>')
        self.assertEqual(self.ui.first_vertex_voltage_label.text(),
                         '<html><head/><body><p align="center">1st Vertex Voltage</p></body></html>')
        self.assertEqual(self.ui.second_vertex_voltage_label.text(),
                         '<html><head/><body><p align="center">2nd Vertex Voltage</p></body></html>')
        self.assertEqual(self.ui.start_voltage_label.text(),
                         '<html><head/><body><p align="center">Start Voltage</p></body></html>')
        self.assertEqual(self.ui.cycle_number_label.text(),
                         '<html><head/><body><p align="center">Cycle Number</p></body></html>')
        self.assertEqual(self.ui.experiment_parameters_label.text(),
                         '<html><head/><body><p align="center">Experiment Parameters</p></body></html>')

    def test_line_edits_exist(self):
        """Test if all line edit fields are created."""
        self.assertIsNotNone(self.ui.experiment_file_name)
        self.assertIsNotNone(self.ui.experiment_file_path)
        self.assertIsNotNone(self.ui.experiment_sweep_rate)
        self.assertIsNotNone(self.ui.experiment_rest_time)
        self.assertIsNotNone(self.ui.experiment_cycle_number)
        self.assertIsNotNone(self.ui.experiment_step_number)
        self.assertIsNotNone(self.ui.experiment_start_voltage)
        self.assertIsNotNone(self.ui.experiment_first_vertex_voltage)
        self.assertIsNotNone(self.ui.experiment_second_vertex_voltage)

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
