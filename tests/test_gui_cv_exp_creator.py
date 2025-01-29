import os
import tempfile
from unittest.mock import MagicMock

import numpy as np
import pytest

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

# Sample data for testing
sample_AP_params = [4.798, 1.03, 0, 0.202, 0.003, 9]
sample_exp_params = {
    "experiment_file_name": "test_output",
    "experiment_file_path": tempfile.gettempdir(),
    "experiment_rest_time": "10",
    "experiment_step_number": "5",
    "experiment_start_voltage": "0.5",
    "experiment_first_vertex_voltage": "1.0",
    "experiment_second_vertex_voltage": "0.0",
    "experiment_sweep_rate": "0.1",
    "experiment_cycle_number": "3",
}


# Mocking the UI class
class MockUiCV:
    def __init__(self):
        self.experiment_file_path = MagicMock()
        self.load_folder_name = MagicMock(return_value=tempfile.gettempdir())
        self.AP_window = MagicMock(return_value=(MagicMock(), MagicMock()))
        self.plot_area = MagicMock()
        self.save_experiment_file_button = MagicMock()
        self.experiment_queue = MagicMock()


class MockUiExperiment:
    def __init__(self):
        self.experiment_file_name = MagicMock()
        self.experiment_file_path = MagicMock()
        self.experiment_rest_time = MagicMock()
        self.experiment_step_number = MagicMock()
        self.experiment_start_voltage = MagicMock()
        self.experiment_first_vertex_voltage = MagicMock()
        self.experiment_second_vertex_voltage = MagicMock()
        self.experiment_sweep_rate = MagicMock()
        self.experiment_cycle_number = MagicMock()
        self.experiment_duration = MagicMock()
        self.experiment_averag_number = MagicMock()
        self.experiment_conversion_factor = MagicMock()
        self.experiment_setpoint_gain = MagicMock()
        self.experiment_setpoint_offset = MagicMock()
        self.experiment_shunt_resistor = MagicMock()
        self.experiment_time_step = MagicMock()


# Test for load_folder function
def test_load_folder():
    CV = MockUiCV()
    load_folder(CV)
    assert CV.experiment_file_path.setText.called


# Test for get_AP_parameters function
def test_get_AP_parameters():
    exp = MockUiExperiment()
    exp.experiment_conversion_factor.text.return_value = "1.0"
    exp.experiment_setpoint_gain.text.return_value = "2.0"
    exp.experiment_setpoint_offset.text.return_value = "0.1"
    exp.experiment_shunt_resistor.text.return_value = "0.202"
    exp.experiment_time_step.text.return_value = "0.003"
    exp.experiment_averag_number.text.return_value = "9"

    AP_parameters = get_AP_parameters(exp)
    assert AP_parameters == [1.0, 2.0, 0.1, 0.202, 0.003, 9]


# Test for load_APwindow function
def test_load_APwindow():
    CV = MockUiCV()
    AP_params = sample_AP_params
    AP_window_mock, _ = CV.AP_window()

    load_APwindow(CV, AP_params)

    assert AP_window_mock.experiment_conversion_factor.setText.called
    assert AP_window_mock.experiment_setpoint_gain.setText.called
    assert AP_window_mock.experiment_setpoint_offset.setText.called
    assert AP_window_mock.experiment_shunt_resistor.setText.called
    assert AP_window_mock.experiment_time_step.setText.called
    assert AP_window_mock.experiment_averag_number.setText.called

    # Check if the correct values were set
    assert AP_window_mock.experiment_conversion_factor.setText.call_args[0][
        0
    ] == str(AP_params[0])
    assert AP_window_mock.experiment_setpoint_gain.setText.call_args[0][
        0
    ] == str(AP_params[1])
    assert AP_window_mock.experiment_setpoint_offset.setText.call_args[0][
        0
    ] == str(AP_params[2])
    assert AP_window_mock.experiment_shunt_resistor.setText.call_args[0][
        0
    ] == str(AP_params[3])
    assert AP_window_mock.experiment_time_step.setText.call_args[0][0] == str(
        AP_params[4]
    )
    assert AP_window_mock.experiment_averag_number.setText.call_args[0][
        0
    ] == str(AP_params[5])


# Test for time_converter function
def test_time_converter():
    assert time_converter(3661) == "1:01:01"
    assert time_converter(-1) == "0:00:00"


# Test for CV_data function
def test_CV_data():
    # Test case 1: Normal case
    stp_num = 6
    cv_sv = 0.0
    cv_ftv = 1.0
    cv_stv = 0.0
    cv_sr = 100.0

    times_step_list, steps_list = CV_data(
        stp_num, cv_sv, cv_ftv, cv_stv, cv_sr
    )

    expected_length = stp_num
    assert (
        len(times_step_list) - 1 == expected_length
    ), f"Expected {expected_length} times steps, got {len(times_step_list)}"
    assert (
        len(steps_list) - 1 == expected_length
    ), f"Expected {expected_length} steps, got {len(steps_list)}"

    # Test case 2: Negative voltages
    stp_num = 6
    cv_sv = -1.0
    cv_ftv = 0.0
    cv_stv = -0.5
    cv_sr = 100.0

    times_step_list, steps_list = CV_data(
        stp_num, cv_sv, cv_ftv, cv_stv, cv_sr
    )

    # Check if the function handles negative voltages correctly
    assert (
        len(times_step_list) - 1 == expected_length
    ), f"Expected {expected_length} times steps, got {len(times_step_list)}"
    assert (
        len(steps_list) - 1 == expected_length
    ), f"Expected {expected_length} steps, got {len(steps_list)}"

    # Additional checks on the values in the lists
    assert np.all(
        steps_list >= min(cv_sv, cv_ftv, cv_stv)
    ), "Steps should not be less than the minimum voltage"
    assert np.all(
        steps_list <= max(cv_sv, cv_ftv, cv_stv)
    ), "Steps should not be greater than the maximum voltage"


# Test for preview_CV function
def test_preview_CV():
    exp = MockUiExperiment()
    grid = MagicMock()
    exp.experiment_step_number.text.return_value = "5"
    exp.experiment_start_voltage.text.return_value = "0.0"
    exp.experiment_first_vertex_voltage.text.return_value = "1.0"
    exp.experiment_second_vertex_voltage.text.return_value = "0.0"
    exp.experiment_sweep_rate.text.return_value = "0.1"
    exp.experiment_cycle_number.text.return_value = "3"

    preview_CV(exp, grid)
    assert exp.experiment_duration.setText.called


# Test for save_file function
def test_save_file():
    config_data = {"test_key": "test_value"}
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        config_path_name = temp_file.name
    save_file(config_path_name, config_data, 0)

    with open(config_path_name, "r") as file:
        contents = file.read()
    assert "#General parameters to edit for an experiment" in contents
    os.remove(config_path_name)


# Test for config_writer_CV function
def test_config_writer_CV():
    exp_type = "CV"
    rt = 10
    stp_num = 6
    data_out_name = "test_output"
    data_out_path = tempfile.gettempdir()
    conv_fact = 1.0
    set_gain = 2.0
    set_offset = 0.1
    sr = 0.202
    ts = 0.003
    avg_num = 9
    cv_sv = 0.0
    cv_ftv = 1.0
    cv_stv = 0.0
    cv_sr = 0.1
    cyc_num = 3

    config_writer_CV(
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
        cv_sv,
        cv_ftv,
        cv_stv,
        cv_sr,
        cyc_num,
    )
    config_file_path = os.path.join(
        data_out_path, f"{data_out_name}_{exp_type}_config.yml"
    )
    assert os.path.exists(config_file_path)
    os.remove(config_file_path)


# Test for check function
def test_check():
    assert check("123") is True
    assert check("-123") is True
    assert check("12.3") is True
    assert check("abc") is False
    assert check("") is False


# Test for get_parameters function
def test_get_parameters():
    exp = MockUiExperiment()
    exp.experiment_file_name.text.return_value = "test_output"
    exp.experiment_file_path.text.return_value = tempfile.gettempdir()
    exp.experiment_rest_time.text.return_value = "10"
    exp.experiment_step_number.text.return_value = "5"
    exp.experiment_start_voltage.text.return_value = "0.0"
    exp.experiment_first_vertex_voltage.text.return_value = "1.0"
    exp.experiment_second_vertex_voltage.text.return_value = "0.0"
    exp.experiment_sweep_rate.text.return_value = "0.1"
    exp.experiment_cycle_number.text.return_value = "3"

    AP_parameters = sample_AP_params
    config_params = get_parameters(exp, "CV", AP_parameters)
    assert config_params[0] == "CV"
    assert config_params[3] == "test_output"


# Test for write_to_file_CV function
def test_write_to_file_CV():
    ui = MagicMock()
    CV = MockUiCV()
    CV_window = MagicMock()
    AP_params = sample_AP_params

    write_to_file_CV(ui, CV, CV_window, AP_params)
    assert CV_window.close.called


# Test for CV_window_writer function
def test_CV_window_writer():
    exp = MockUiExperiment()
    config_data = {
        "general_parameters": {
            "data_output_filename": "test_output",
            "data_output_path": tempfile.gettempdir(),
            "rest_time": 10,
            "step_number": 5,
        },
        "cyclic_voltammetry": {
            "start_voltage": 0.0,
            "first_turnover_voltage": 1.0,
            "second_turnover_voltage": 0.0,
            "sweep_rate": 0.1,
            "number_of_cycles": 3,
        },
    }

    CV_window_writer(exp, config_data)
    assert exp.experiment_file_name.setText.called
    assert exp.experiment_file_path.setText.called


# Test for CV_main function
def test_CV_main():
    ui = MagicMock()
    config_data = None  # or provide a sample config_data if needed
    CV = CV_main(ui, config_data)
    assert CV is not None


# Test for plot function
def test_plot():
    x = [0, 1, 2]
    y = [0, 1, 0]
    canvas = plot(x, y)
    assert canvas is not None


if __name__ == "__main__":
    pytest.main()
