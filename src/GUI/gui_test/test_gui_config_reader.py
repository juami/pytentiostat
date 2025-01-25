import unittest
from unittest.mock import mock_open, patch

import yaml

from src.GUI.code.GUI_config_reader import (
    check_config_inputs,
    get_adv_params,
    get_ca_params,
    get_cv_params,
    get_exp_time,
    get_exp_type,
    get_lsv_params,
    get_output_params,
    get_rest,
    get_steps,
    parse_config_file,
)


class TestGUIConfigReader(unittest.TestCase):

    def setUp(self):
        # Sample configuration data
        self.config_data = {
            "general_parameters": {
                "data_output_filename": "output",
                "data_output_path": "desktop",
                "experiment_type": "cyclic_voltammetry",
                "rest_time": 10,
                "step_number": 5,
            },
            "linear_sweep_voltammetry": {
                "start_voltage": 0,
                "end_voltage": 1,
                "sweep_rate": 0.1,
            },
            "chronoamperometry": {
                "voltage": 0.5,
                "time": 60,
            },
            "cyclic_voltammetry": {
                "start_voltage": -0.5,
                "first_turnover_voltage": 0.0,
                "second_turnover_voltage": 0.5,
                "sweep_rate": 0.1,
                "number_of_cycles": 3,
            },
            "advanced_parameters": {
                "conversion_factor": 1.0,
                "setpoint_gain": 10,
                "setpoint_offset": 0,
                "shunt_resistor": 1000,
                "time_step": 0.01,
                "average_number": 5,
            }
        }

    @patch("builtins.open", new_callable=mock_open, read_data=yaml.dump({}))
    def test_parse_config_file(self, mock_file):
        mock_file.return_value.read.return_value = yaml.dump(self.config_data)
        config = parse_config_file("dummy_path")
        self.assertEqual(config, self.config_data)

    def test_get_output_params(self):
        out_name_ts, out_path = get_output_params(self.config_data)
        self.assertTrue("output_", out_name_ts)
        self.assertTrue(out_path.endswith("Desktop"))

    def test_get_lsv_params(self):
        start_voltage, end_voltage, sweep_rate = get_lsv_params(self.config_data)
        self.assertEqual(start_voltage, 0)
        self.assertEqual(end_voltage, 1)
        self.assertEqual(sweep_rate, 0.1)

    def test_get_ca_params(self):
        voltage, time = get_ca_params(self.config_data)
        self.assertEqual(voltage, 0.5)
        self.assertEqual(time, 60)

    def test_get_cv_params(self):
        params = get_cv_params(self.config_data)
        self.assertEqual(params[0], -0.5)
        self.assertEqual(params[1], 0.0)
        self.assertEqual(params[2], 0.5)
        self.assertEqual(params[3], 0.1)
        self.assertEqual(params[4], 3)

    def test_get_exp_type(self):
        exp_type = get_exp_type(self.config_data)
        self.assertEqual(exp_type, "cyclic_voltammetry")

    def test_get_exp_time(self):
        exp_time = get_exp_time(self.config_data)
        self.assertEqual(exp_time, 60)

    def test_get_rest(self):
        rest_time = get_rest(self.config_data)
        self.assertEqual(rest_time, 10)

    def test_get_steps(self):
        step_number = get_steps(self.config_data)
        self.assertEqual(step_number, 5)

    def test_get_adv_params(self):
        adv_params = get_adv_params(self.config_data)
        self.assertEqual(adv_params[0], 1.0)
        self.assertEqual(adv_params[1], 10)
        self.assertEqual(adv_params[2], 0)
        self.assertEqual(adv_params[3], 1000)
        self.assertEqual(adv_params[4], 0.01)
        self.assertEqual(adv_params[5], 5)

    def test_check_config_inputs(self):
        self.assertTrue(check_config_inputs(10))
        self.assertTrue(check_config_inputs("10"))
        self.assertFalse(check_config_inputs("not_a_number"))


if __name__ == "__main__":
    unittest.main()
