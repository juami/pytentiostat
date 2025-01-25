import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_CA_exp_creator import (
    CA_main,
    CA_window_writer,
    check,
    config_writer_CA,
    get_AP_parameters,
    get_parameters,
    load_APwindow,
    load_folder,
    plot,
    preview_CA,
    save_file,
    time_converter,
    write_to_file_CA,
)


class TestGUICAExpCreator(unittest.TestCase):

    @patch('MultipleFiles.GUI_CA_exp_creator.QFileDialog.getExistingDirectory')
    def test_load_folder(self):
        """Test load_folder function."""
        mock_CA = MagicMock()
        mock_CA.load_folder_name.return_value = "/mock/path"
        load_folder(mock_CA)
        mock_CA.experiment_file_path.setText.assert_called_with("/mock/path")

    def test_get_AP_parameters(self):
        """Test get_AP_parameters function."""
        mock_exp = MagicMock()
        mock_exp.experiment_conversion_factor.text.return_value = "1.0"
        mock_exp.experiment_setpoint_gain.text.return_value = "2.0"
        mock_exp.experiment_setpoint_offset.text.return_value = "0.0"
        mock_exp.experiment_shunt_resistor.text.return_value = "0.1"
        mock_exp.experiment_time_step.text.return_value = "0.01"
        mock_exp.experiment_averag_number.text.return_value = "10"

        expected_params = [1.0, 2.0, 0.0, 0.1, 0.01, 10]
        self.assertEqual(get_AP_parameters(mock_exp), expected_params)

    @patch('MultipleFiles.GUI_CA_exp_creator.warning')
    def test_load_APwindow(self, mock_warning):
        """Test load_APwindow function."""
        mock_CA = MagicMock()
        mock_AP_params = [1.0, 2.0, 0.0, 0.1, 0.01, 10]
        load_APwindow(mock_CA, mock_AP_params)

        # Check if the parameters are set correctly
        self.assertEqual(mock_CA.AP_window().experiment_conversion_factor.text(), "1.0")
        self.assertEqual(mock_CA.AP_window().experiment_setpoint_gain.text(), "2.0")
        self.assertEqual(mock_CA.AP_window().experiment_setpoint_offset.text(), "0.0")
        self.assertEqual(mock_CA.AP_window().experiment_shunt_resistor.text(), "0.1")
        self.assertEqual(mock_CA.AP_window().experiment_time_step.text(), "0.01")
        self.assertEqual(mock_CA.AP_window().experiment_averag_number.text(), "10")

    def test_time_converter(self):
        """Test time_converter function."""
        self.assertEqual(time_converter(3661), "1:01:01")
        self.assertEqual(time_converter(-1), "0:00:00")

    def test_plot(self):
        """Test plot function."""
        x = [0, 1, 2]
        y = [0, 1, 4]
        canvas = plot(x, y)
        self.assertIsNotNone(canvas)

    @patch('MultipleFiles.GUI_CA_exp_creator.warning')
    def test_preview_CA(self, mock_warning):
        """Test preview_CA function."""
        mock_exp = MagicMock()
        mock_grid = MagicMock()
        mock_exp.experiment_step_number.text.return_value = "10"
        mock_exp.experiment_voltage.text.return_value = "5.0"
        mock_exp.experiment_time.text.return_value = "10"

        preview_CA(mock_exp, mock_grid)

        # Check if the grid is updated
        mock_grid.addWidget.assert_called()

    @patch('MultipleFiles.GUI_CA_exp_creator.yaml.dump')
    def test_save_file(self, mock_yaml_dump):
        """Test save_file function."""
        config_path_name = "/mock/path/config.yml"
        config_data = {"key": "value"}
        line_skipper = 0

        save_file(config_path_name, config_data, line_skipper)
        mock_yaml_dump.assert_called_once()

    def test_check(self):
        """Test check function."""
        self.assertTrue(check("123"))
        self.assertFalse(check("abc"))
        self.assertTrue(check("-123.45"))

    @patch('MultipleFiles.GUI_CA_exp_creator.warning')
    def test_get_parameters(self, mock_warning):
        """Test get_parameters function."""
        mock_exp = MagicMock()
        mock_exp.experiment_file_name.text.return_value = "test_experiment"
        mock_exp.experiment_file_path.text.return_value = "/mock/path"
        mock_exp.experiment_rest_time.text.return_value = "5"
        mock_exp.experiment_step_number.text.return_value = "10"
        mock_exp.experiment_voltage.text.return_value = "1.0"
        mock_exp.experiment_time.text.return_value = "10"

        AP_parameters = [1.0, 2.0, 0.0, 0.1, 0.01, 10]  # Mock advanced parameters
        expected_params = [
            "CA",  # Experiment type
            5,  # Rest time
            10,  # Step number
            "test_experiment",  # Output filename
            "/mock/path",  # Output path
            1.0,  # Voltage
            10  # Time
        ]

        result = get_parameters(mock_exp, "CA", AP_parameters)
        self.assertEqual(result, expected_params)

    @patch('MultipleFiles.GUI_CA_exp_creator.save_file')
    def test_config_writer_CA(self, mock_save_file):
        """Test config_writer_CA function."""
        # Define the input parameters
        exp_type = "CA"
        rt = 5
        stp_num = 10
        data_out_name = "test_experiment"
        data_out_path = "/mock/path"
        conv_fact = 1.0
        set_gain = 2.0
        set_offset = 0.0
        sr = 0.1
        ts = 0.01
        avg_num = 10
        ca_v = 1.0
        ca_time = 10

        # Call the function
        config_writer_CA(
            exp_type,
            rt,
            stp_num,
            data_out_name,
            data_out_path,
            conv_fact,
            set_gain,
            set_offset,
            sr,
            ts,
            avg_num,
            ca_v,
            ca_time,
        )

        # Check if save_file was called with the correct parameters
        expected_config_data = {
            "general_parameters": {
                "experiment_type": exp_type,
                "rest_time": rt,
                "step_number": stp_num,
                "data_output_filename": data_out_name,
                "data_output_path": data_out_path,
            },
            "chronoamperometry": {
                "voltage": ca_v,
                "time": ca_time,
            },
            "advanced_parameters": {
                "conversion_factor": conv_fact,
                "setpoint_gain": set_gain,
                "setpoint_offset": set_offset,
                "shunt_resistor": sr,
                "time_step": ts,
                "average_number": avg_num,
            },
        }

        # Verify that save_file was called with the correct parameters
        mock_save_file.assert_called_once()
        args, kwargs = mock_save_file.call_args[0]
        self.assertEqual(args[0], f"{data_out_path}/{data_out_name}_{exp_type}_config.yml")
        self.assertEqual(kwargs['config_data'], expected_config_data)

    @patch('MultipleFiles.GUI_CA_exp_creator.warning')
    def test_write_to_file_CA(self, mock_warning, mock_config_writer):
        """Test write_to_file_CA function."""
        mock_ui = MagicMock()
        mock_CA = MagicMock()
        mock_CA_window = MagicMock()
        AP_parameters = [1.0, 2.0, 0.0, 0.1, 0.01, 10]  # Mock advanced parameters

        # Mock the return values for get_parameters
        mock_ui.experiment_queue.count.return_value = 0
        mock_ui.experiment_queue.item.return_value = None

        write_to_file_CA(mock_ui, mock_CA, mock_CA_window, AP_parameters)

        # Check if config_writer_CA was called
        mock_config_writer.assert_called_once()

    @patch('MultipleFiles.GUI_CA_exp_creator.get_parameters')
    @patch('MultipleFiles.GUI_CA_exp_creator.warning')
    def test_CA_window_writer(self, mock_warning, mock_get_parameters):
        """Test CA_window_writer function."""
        mock_exp = MagicMock()
        config_data = {
            "general_parameters": {
                "data_output_filename": "test_experiment",
                "data_output_path": "/mock/path",
                "rest_time": 5,
                "step_number": 10,
            },
            "chronoamperometry": {
                "voltage": 1.0,
                "time": 10,
            }
        }

        CA_window_writer(mock_exp, config_data)

        # Check if the UI fields are set correctly
        mock_exp.experiment_file_name.setText.assert_called_with("test_experiment")
        mock_exp.experiment_file_path.setText.assert_called_with("/mock/path")
        mock_exp.experiment_rest_time.setText.assert_called_with("5")
        mock_exp.experiment_step_number.setText.assert_called_with("10")
        mock_exp.experiment_voltage.setText.assert_called_with("1.0")
        mock_exp.experiment_time.setText.assert_called_with("10")

    @patch('MultipleFiles.GUI_CA_exp_creator.Ui_Mainwindow')
    @patch('MultipleFiles.GUI_CA_exp_creator.CA_main')
    def test_CA_main(self, mock_CA_main, mock_Ui_Mainwindow):
        """Test CA_main function."""
        mock_ui = MagicMock()
        mock_config_data = None  # No config data for this test

        CA_main(mock_ui, mock_config_data)

        # Check if CA_main was called with the correct parameters
        mock_CA_main.assert_called_once_with(mock_ui, mock_config_data)


if __name__ == "__main__":
    unittest.main()
