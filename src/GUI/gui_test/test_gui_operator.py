import time
import unittest
from unittest.mock import MagicMock, patch

import numpy as np

from src.GUI.code.GUI_operator import experiment, read_write, start_exp


class TestGUIOperator(unittest.TestCase):

    def setUp(self):
        # Create mock objects for Arduino pins and other parameters
        self.d9_mock = MagicMock()
        self.a0_mock = MagicMock()
        self.a2_mock = MagicMock()
        self.ini_plot_mock = MagicMock()
        self.times = []
        self.voltages = []
        self.currents = []
        self.pr_mock = MagicMock()
        self.tr_mock = MagicMock()

    @patch("MultipleFiles.GUI_operator.cr.get_rest")
    def test_start_exp(self, mock_get_rest):
        mock_get_rest.return_value = 1  # Mock the rest time
        normalized_start = 0.5  # Example normalized start value
        start_time = start_exp(self.d9_mock, normalized_start, None)

        # Check if the pin was written correctly
        self.d9_mock.write.assert_called_once_with(normalized_start)
        time.sleep(1)  # Simulate the sleep time
        self.assertAlmostEqual(start_time, time.time(), delta=0.1)

    @patch("MultipleFiles.GUI_operator.time.sleep")
    def test_read_write(self, mock_sleep):
        # Set up mock parameters
        start_time = time.time()
        step_number = 5
        steps_list = np.linspace(0, 1, num=step_number + 1).tolist()  # Convert to list
        current_exp_time = 10
        average = 5
        time_step = 0.1
        cf = 1.0
        sr = 1000.0
        cycle_number = 1

        # Mock the read values
        self.a0_mock.read.side_effect = [0.5] * average
        self.a2_mock.read.side_effect = [0.5] * average

        # Call the read_write function
        times, voltages, currents = read_write(
            start_time,
            self.d9_mock,
            self.a0_mock,
            self.a2_mock,
            step_number,
            steps_list,
            current_exp_time,
            average,
            time_step,
            cf,
            sr,
            self.ini_plot_mock,
            self.times,
            self.voltages,
            self.currents,
            self.pr_mock,
            self.tr_mock,
            total_exp_time=30,
            passed_exp_time=0,
            cycle_number=cycle_number,
        )

        # Check if the voltages and currents were calculated correctly
        self.assertEqual(len(times), (step_number + 1) * cycle_number)  # Adjusted for the number of steps
        self.assertEqual(len(voltages), (step_number + 1) * cycle_number)
        self.assertEqual(len(currents), (step_number + 1) * cycle_number)

        # Check if the progress bar was updated
        self.pr_mock.setValue.assert_called()
        self.tr_mock.setText.assert_called()

    @patch("MultipleFiles.GUI_operator.start_exp")
    @patch("MultipleFiles.GUI_operator.read_write")
    @patch("MultipleFiles.GUI_operator.cr.get_adv_params")
    @patch("MultipleFiles.GUI_operator.cr.get_steps")
    @patch("MultipleFiles.GUI_operator.cr.get_exp_type")
    def test_experiment(self, mock_get_exp_type, mock_get_steps, mock_get_adv_params, mock_read_write, mock_start_exp):
        # Mock the return values
        mock_get_exp_type.return_value = "LSV"
        mock_get_steps.return_value = 5
        mock_get_adv_params.return_value = (1.0, 1.0, 0.0, 1000.0, 0.01, 5)

        # Mock the start_exp function
        mock_start_exp.return_value = time.time()

        # Call the experiment function
        times, voltages, currents = experiment(
            {},  # config_data
            None,  # board
            self.a0_mock,
            self.a2_mock,
            self.d9_mock,
            self.ini_plot_mock,
            self.times,
            self.voltages,
            self.currents,
            self.pr_mock,
            self.tr_mock,
            total_exp_time=30,
            passed_exp_time=0,
        )

        # Check if read_write was called
        mock_read_write.assert_called()
        self.assertEqual(len(times), (5 + 1))  # 5 steps + 1 for the end
        self.assertEqual(len(voltages), (5 + 1))
        self.assertEqual(len(currents), (5 + 1))


if __name__ == "__main__":
    unittest.main()
