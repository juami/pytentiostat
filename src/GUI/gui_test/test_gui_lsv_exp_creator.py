import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_LSV_exp_creator import (
    LSV_main,
    LSV_window_writer,
    check,
    config_writer_LSV,
    get_AP_parameters,
    get_parameters,
    load_APwindow,
    load_folder,
    plot,
    preview_LSV,
    save_file,
    time_converter,
    write_to_file_LSV,
)


class TestGUILSVExpCreator(unittest.TestCase):

    def setUp(self):
        # Create mock objects for the UI components
        self.LSV_mock = MagicMock()
        self.exp_mock = MagicMock()
        self.grid_mock = MagicMock()

    @patch("MultipleFiles.GUI_LSV_exp_creator.QFileDialog.getExistingDirectory")
    def test_load_folder(self, mock_get_existing_directory):
        mock_get_existing_directory.return_value = "/mock/path"
        load_folder(self.LSV_mock)
        self.LSV_mock.experiment_file_path.setText.assert_called_with("/mock/path")

    def test_get_AP_parameters(self):
        # Set mock values
        self.exp_mock.experiment_conversion_factor.text.return_value = "1.0"
        self.exp_mock.experiment_setpoint_gain.text.return_value = "2.0"
        self.exp_mock.experiment_setpoint_offset.text.return_value = "0.0"
        self.exp_mock.experiment_shunt_resistor.text.return_value = "1000"
        self.exp_mock.experiment_time_step.text.return_value = "0.01"
        self.exp_mock.experiment_averag_number.text.return_value = "5"

        expected_params = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        actual_params = get_AP_parameters(self.exp_mock)
        self.assertEqual(actual_params, expected_params)

    @patch("MultipleFiles.GUI_LSV_exp_creator.warning")
    def test_load_APwindow(self, mock_warning):
        AP_params = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        load_APwindow(self.LSV_mock, AP_params)
        self.LSV_mock.AP_window().experiment_conversion_factor.setText.assert_called_with("1.0")

    def test_time_converter(self):
        self.assertEqual(time_converter(3661), "1:01:01")
        self.assertEqual(time_converter(-1), "0:00:00")

    def test_plot(self):
        x = [0, 1, 2]
        y = [0, 1, 0]
        canvas = plot(x, y)
        self.assertIsNotNone(canvas)

    def test_preview_LSV(self):
        self.exp_mock.experiment_step_number.text.return_value = "10"
        self.exp_mock.experiment_start_voltage.text.return_value = "0.0"
        self.exp_mock.experiment_end_voltage.text.return_value = "1.0"
        self.exp_mock.experiment_sweep_rate.text.return_value = "0.1"

        preview_LSV(self.exp_mock, self.grid_mock)
        self.assertTrue(self.grid_mock.count() > 0)

    @patch("builtins.open", new_callable=MagicMock)
    def test_save_file(self, mock_open):
        config_path_name = "test_config.yml"
        config_data = {"key": "value"}
        line_skipper = 0

        save_file(config_path_name, config_data, line_skipper)
        mock_open.assert_called_once_with(config_path_name, "w")

    @patch("MultipleFiles.GUI_LSV_exp_creator.save_file")
    def test_config_writer_LSV(self, mock_save_file):
        config_writer_LSV(
            "LSV",
            10,
            5,
            "output",
            "/mock/path",
            1.0,
            2.0,
            0.0,
            1000.0,
            0.01,
            5,
            0.0,
            1.0,
            0.1,
        )
        mock_save_file.assert_called()

    def test_check(self):
        self.assertTrue(check("123"))
        self.assertFalse(check("abc"))
        self.assertFalse(check("-123.45"))

    @patch("MultipleFiles.GUI_LSV_exp_creator.warning")
    def test_get_parameters(self, mock_warning):
        self.exp_mock.experiment_file_name.text.return_value = "output"
        self.exp_mock.experiment_file_path.text.return_value = "/mock/path"
        self.exp_mock.experiment_rest_time.text.return_value = "10"
        self.exp_mock.experiment_step_number.text.return_value = "5"
        self.exp_mock.experiment_start_voltage.text.return_value = "0.0"
        self.exp_mock.experiment_end_voltage.text.return_value = "1.0"
        self.exp_mock.experiment_sweep_rate.text.return_value = "0.1"

        AP_parameters = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        params = get_parameters(self.exp_mock, "LSV", AP_parameters)
        self.assertEqual(len(params), 12)

    @patch("MultipleFiles.GUI_LSV_exp_creator.warning")
    def test_write_to_file_LSV(self, mock_warning):
        self.exp_mock.experiment_file_name.text.return_value = "output"
        self.exp_mock.experiment_file_path.text.return_value = "/mock/path"
        AP_params = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        write_to_file_LSV(self.LSV_mock, self.LSV_mock, self.LSV_mock, AP_params)
        self.assertTrue(mock_warning.called)

    @patch("MultipleFiles.GUI_LSV_exp_creator.QMainWindow")
    def test_LSV_window_writer(self, mock_main_window):
        config_data = {
            "general_parameters": {
                "experiment_type": "LSV",
                "data_output_filename": "output",
                "data_output_path": "/mock/path",
                "rest_time": 10,
                "step_number": 5,
            },
            "linear_sweep_voltammetry": {
                "start_voltage": 0.0,
                "end_voltage": 1.0,
                "sweep_rate": 0.1,
            },
            "advanced_parameters": {
                "conversion_factor": 1.0,
                "setpoint_gain": 2.0,
                "setpoint_offset": 0.0,
                "shunt_resistor": 1000.0,
                "time_step": 0.01,
                "average_number": 5,
            },
        }
        LSV_window_writer(self.exp_mock, config_data)
        self.assertEqual(self.exp_mock.experiment_file_name.setText.call_count, 1)

    @patch("MultipleFiles.GUI_LSV_exp_creator.QMainWindow")
    def test_LSV_main(self, mock_QMainWindow):
        config_data = None
        LSV = LSV_main(self.LSV_mock, config_data)
        self.assertIsNotNone(LSV)


if __name__ == "__main__":
    unittest.main()
