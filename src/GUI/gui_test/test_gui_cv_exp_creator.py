import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_CV_exp_creator import (
    CV_data,
    CV_main,
    CV_window_writer,
    check,
    config_writer_CV,
    get_AP_parameters,
    get_parameters,
    load_APwindow,
    load_folder,
    plot,
    preview_CV,
    save_file,
    time_converter,
    write_to_file_CV,
)


class TestGUICVExpCreator(unittest.TestCase):

    def setUp(self):
        # Create a mock CV object with necessary attributes
        self.CV_mock = MagicMock()
        self.exp_mock = MagicMock()
        self.grid_mock = MagicMock()

    @patch("MultipleFiles.GUI_CV_exp_creator.QFileDialog.getExistingDirectory")
    def test_load_folder(self, mock_get_existing_directory):
        mock_get_existing_directory.return_value = "/mock/path"
        load_folder(self.CV_mock)
        self.CV_mock.experiment_file_path.setText.assert_called_with("/mock/path")

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

    @patch("MultipleFiles.GUI_CV_exp_creator.warning")
    def test_load_APwindow(self, mock_warning):
        AP_params = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        load_APwindow(self.CV_mock, AP_params)
        self.CV_mock.AP_window().experiment_conversion_factor.setText.assert_called_with("1.0")

    def test_time_converter(self):
        self.assertEqual(time_converter(3661), "1:01:01")
        self.assertEqual(time_converter(-1), "0:00:00")

    def test_plot(self):
        x = [0, 1, 2]
        y = [0, 1, 0]
        canvas = plot(x, y)
        self.assertIsNotNone(canvas)

    def test_CV_data(self):
        stp_num = 10
        cv_sv = 0.0
        cv_ftv = 1.0
        cv_stv = 0.5
        cv_sr = 0.1
        times_step_list, steps_list = CV_data(stp_num, cv_sv, cv_ftv, cv_stv, cv_sr)
        self.assertEqual(len(times_step_list), stp_num)
        self.assertEqual(len(steps_list), stp_num)

    @patch("MultipleFiles.GUI_CV_exp_creator.warning")
    def test_preview_CV(self, mock_warning):
        self.exp_mock.experiment_step_number.text.return_value = "10"
        self.exp_mock.experiment_start_voltage.text.return_value = "0.0"
        self.exp_mock.experiment_first_vertex_voltage.text.return_value = "1.0"
        self.exp_mock.experiment_second_vertex_voltage.text.return_value = "0.5"
        self.exp_mock.experiment_sweep_rate.text.return_value = "0.1"
        self.exp_mock.experiment_cycle_number.text.return_value = "1"

        preview_CV(self.exp_mock, self.grid_mock)
        self.assertTrue(self.grid_mock.count() > 0)

    @patch("builtins.open", new_callable=MagicMock)
    def test_save_file(self, mock_open):
        config_path_name = "test_config.yml"
        config_data = {"key": "value"}
        line_skipper = 0

        save_file(config_path_name, config_data, line_skipper)
        mock_open.assert_called_once_with(config_path_name, "w")

    @patch("MultipleFiles.GUI_CV_exp_creator.save_file")
    def test_config_writer_CV(self, mock_save_file):
        config_writer_CV(
            "CV",
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
            0.5,
            0.1,
            1
        )
        mock_save_file.assert_called()

    def test_check(self):
        self.assertTrue(check("123"))
        self.assertFalse(check("abc"))
        self.assertFalse(check("-123.45"))

    @patch("MultipleFiles.GUI_CV_exp_creator.warning")
    def test_get_parameters(self, mock_warning):
        self.exp_mock.experiment_file_name.text.return_value = "output"
        self.exp_mock.experiment_file_path.text.return_value = "/mock/path"
        self.exp_mock.experiment_rest_time.text.return_value = "10"
        self.exp_mock.experiment_step_number.text.return_value = "5"
        self.exp_mock.experiment_start_voltage.text.return_value = "0.0"
        self.exp_mock.experiment_first_vertex_voltage.text.return_value = "1.0"
        self.exp_mock.experiment_second_vertex_voltage.text.return_value = "0.5"
        self.exp_mock.experiment_sweep_rate.text.return_value = "0.1"
        self.exp_mock.experiment_cycle_number.text.return_value = "1"

        AP_parameters = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        params = get_parameters(self.exp_mock, "CV", AP_parameters)
        self.assertEqual(len(params), 12)

    @patch("MultipleFiles.GUI_CV_exp_creator.warning")
    def test_write_to_file_CV(self, mock_warning):
        self.exp_mock.experiment_file_name.text.return_value = "output"
        self.exp_mock.experiment_file_path.text.return_value = "/mock/path"
        AP_params = [1.0, 2.0, 0.0, 1000.0, 0.01, 5]
        write_to_file_CV(self.CV_mock, self.CV_mock, self.CV_mock, AP_params)
        self.assertTrue(mock_warning.called)

    @patch("MultipleFiles.GUI_CV_exp_creator.warning")
    def test_CV_window_writer(self, mock_warning):
        config_data = {
            "general_parameters": {
                "experiment_type": "CV",
                "data_output_filename": "output",
                "data_output_path": "/mock/path",
                "rest_time": 10,
                "step_number": 5,
            },
            "cyclic_voltammetry": {
                "start_voltage": 0.0,
                "first_turnover_voltage": 1.0,
                "second_turnover_voltage": 0.5,
                "sweep_rate": 0.1,
                "number_of_cycles": 1,
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
        CV_window_writer(self.exp_mock, config_data)
        self.assertEqual(self.exp_mock.experiment_file_name.setText.call_count, 1)

    @patch("MultipleFiles.GUI_CV_exp_creator.QMainWindow")
    def test_CV_main(self, mock_QMainWindow):
        config_data = None
        CV = CV_main(self.CV_mock, config_data)
        self.assertIsNotNone(CV)


if __name__ == "__main__":
    unittest.main()
