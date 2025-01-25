import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_run_exp import (
    calculate_time,
    run_exp,
    run_exp_main,
    set_icon,
    total_time,
)


class TestGUIRunExp(unittest.TestCase):

    @patch('GUI_run_exp.parse_config_file')
    def test_calculate_time_CA(self, mock_parse):
        """Test the calculate_time function for CA experiment type."""
        mock_parse.return_value = {
            "chronoamperometry": {"time": 10}
        }
        filename = "experiment_CA.yml"
        result = calculate_time(filename)
        self.assertEqual(result, 10)

    @patch('GUI_run_exp.parse_config_file')
    def test_calculate_time_CV(self, mock_parse):
        """Test the calculate_time function for CV experiment type."""
        mock_parse.return_value = {
            "cyclic_voltammetry": {
                "number_of_cycles": 2,
                "start_voltage": 0,
                "first_turnover_voltage": 1,
                "second_turnover_voltage": 2,
                "sweep_rate": 0.1
            }
        }
        filename = "experiment_CV.yml"
        result = calculate_time(filename)
        self.assertEqual(result, 60)  # (2 * (1 + 1 + 1) / 0.1) * 1000

    @patch('GUI_run_exp.parse_config_file')
    def test_calculate_time_LSV(self, mock_parse):
        """Test the calculate_time function for LSV experiment type."""
        mock_parse.return_value = {
            "linear_sweep_voltammetry": {
                "start_voltage": 0,
                "end_voltage": 1,
                "sweep_rate": 0.1
            }
        }
        filename = "experiment_LSV.yml"
        result = calculate_time(filename)
        self.assertEqual(result, 10000)  # (1 - 0) / 0.1 * 1000

    @patch('GUI_run_exp.calculate_time')
    def test_total_time(self, mock_calculate):
        """Test the total_time function."""
        ui_mock = MagicMock()
        ui_mock.experiment_queue.count.return_value = 2
        ui_mock.experiment_queue.item.side_effect = [
            MagicMock(data=MagicMock(return_value="experiment_CA.yml")),
            MagicMock(data=MagicMock(return_value="experiment_CV.yml"))
        ]
        mock_calculate.side_effect = [10, 60]  # Mock return values for calculate_time

        result = total_time(ui_mock)
        self.assertEqual(result, [10, 60])

    @patch('GUI_run_exp.QIcon')
    def test_set_icon(self, mock_qicon):
        """Test the set_icon function."""
        ui_mock = MagicMock()
        ui_mock.experiment_queue.count.return_value = 2
        ui_mock.experiment_queue.item.side_effect = [
            MagicMock(data=MagicMock(return_value="experiment_CA.yml")),
            MagicMock(data=MagicMock(return_value="experiment_CV.yml"))
        ]

        set_icon(ui_mock)

        # Check if the icons were set correctly
        ui_mock.experiment_queue.item(0).setData.assert_called_with(1, mock_qicon.return_value)
        ui_mock.experiment_queue.item(1).setData.assert_called_with(1, mock_qicon.return_value)

    @patch('GUI_run_exp.warning')
    @patch('GUI_run_exp.parse_config_file')
    @patch('GUI_run_exp.experiment')
    @patch('GUI_run_exp.total_time')
    @patch('GUI_run_exp.set_icon')
    def test_run_exp(self, mock_set_icon, mock_total_time, mock_experiment, mock_parse, mock_warning):
        """Test the run_exp function."""
        ui_mock = MagicMock()
        ui_mock.experiment_queue.count.return_value = 1
        ui_mock.experiment_queue.item.return_value.data.return_value = "experiment_CA.yml"
        ui_mock.start_abort_experiment_button.isChecked.return_value = True
        mock_parse.return_value = {
            "general_parameters": {
                "data_output_filename": "output",
                "data_output_path": "./"
            }
        }
        mock_total_time.return_value = [10]
        mock_experiment.return_value = ([], [], [])

        run_exp(ui_mock, "COM3", ("board", "a0", "a2", "d9"), MagicMock(), MagicMock(), MagicMock(), MagicMock())

        # Check if the experiment was run
        mock_experiment.assert_called()
        ui_mock.experiment_status_indicator.setIcon.assert_called()

    @patch('GUI_run_exp.run_exp')
    def test_run_exp_main(self, mock_run_exp):
        """Test the run_exp_main function."""
        ui_mock = MagicMock()
        com_mock = "COM3"
        board_objects_mock = ("board", "a0", "a2", "d9")
        grid_mock = MagicMock()

        run_exp_main(ui_mock, com_mock, board_objects_mock, grid_mock)

        # Check if run_exp was called with the correct parameters
        mock_run_exp.assert_called_with(ui_mock, com_mock, board_objects_mock, MagicMock(), grid_mock, MagicMock(), MagicMock())


if __name__ == '__main__':
    unittest.main()
