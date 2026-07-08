import os

import pytest
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

# Sample configuration data for testing
sample_config = {
    "general_parameters": {
        "data_output_filename": "test_output",
        "data_output_path": "desktop",
        "experiment_type": "cyclic_voltammetry",
        "rest_time": 10,
        "step_number": 5,
    },
    "linear_sweep_voltammetry": {
        "start_voltage": 0.0,
        "end_voltage": 1.0,
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
        "setpoint_gain": 2.0,
        "setpoint_offset": 0.1,
        "shunt_resistor": 1000,
        "time_step": 0.01,
        "average_number": 10,
    },
}


# Create a temporary YAML file for testing
@pytest.fixture
def temp_config_file(tmp_path):
    config_file = tmp_path / "config.yml"
    with open(config_file, "w") as file:
        yaml.dump(sample_config, file)
    return config_file


def test_parse_config_file(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    assert config_data == sample_config


def test_get_output_params(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    out_name_ts, out_path = get_output_params(config_data)
    assert out_name_ts.startswith("test_output_")
    assert out_path == os.path.join(os.path.expanduser("~"), "Desktop")


def test_get_lsv_params(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    start_voltage, end_voltage, sweep_rate = get_lsv_params(config_data)
    assert start_voltage == 0.0
    assert end_voltage == 1.0
    assert sweep_rate == 0.1


def test_get_ca_params(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    voltage, time = get_ca_params(config_data)
    assert voltage == 0.5
    assert time == 60


def test_get_cv_params(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    (
        start_voltage,
        first_turnover,
        second_turnover,
        sweep_rate,
        cycle_number,
    ) = get_cv_params(config_data)
    assert start_voltage == -0.5
    assert first_turnover == 0.0
    assert second_turnover == 0.5
    assert sweep_rate == 0.1
    assert cycle_number == 3


def test_get_exp_type(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    exp_type = get_exp_type(config_data)
    assert exp_type == "cyclic_voltammetry"


def test_get_exp_time(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    exp_time = get_exp_time(config_data)
    assert exp_time == 60


def test_get_rest(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    rest_time = get_rest(config_data)
    assert rest_time == 10


def test_get_steps(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    step_number = get_steps(config_data)
    assert step_number == 5


def test_get_adv_params(temp_config_file):
    config_data = parse_config_file(temp_config_file)
    (
        conversion_factor,
        set_gain,
        set_offset,
        shunt_resistor,
        time_step,
        average_number,
    ) = get_adv_params(config_data)
    assert conversion_factor == 1.0
    assert set_gain == 2.0
    assert set_offset == 0.1
    assert shunt_resistor == 1000
    assert time_step == 0.01
    assert average_number == 10


def test_check_config_inputs():
    assert check_config_inputs(10) is True
    assert check_config_inputs("10") is True
    assert check_config_inputs("abc") is False
    assert check_config_inputs(None) is False
