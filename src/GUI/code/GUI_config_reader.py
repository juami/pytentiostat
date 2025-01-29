import datetime
import os

import yaml


def parse_config_file(filename):
    """Reads config data from the config file.

    the config file must be called config.yml.

    Parameters
    ----------
    configlocation : str, the path on the filesystem to the config file.

    Returns
    -------
    config_data : dictionary, the configuration data
    """
    with open(filename, "r") as stream:
        config_data = yaml.safe_load(stream)
        return config_data


def get_output_params(config_data, override_ts=None):
    data_out_name = config_data["general_parameters"]["data_output_filename"]
    data_out_path = config_data["general_parameters"]["data_output_path"]
    if data_out_path.lower() == "desktop":
        data_out_path = os.path.join(
            os.path.join(os.path.expanduser("~")), "Desktop"
        )
    ts = datetime.datetime.now().strftime("%H_%M_%S")
    if override_ts:
        ts = override_ts
    out_name_ts = data_out_name + "_" + ts + ".csv"

    return out_name_ts, data_out_path


def get_lsv_params(config_data):
    start_voltage = config_data["linear_sweep_voltammetry"]["start_voltage"]
    end_voltage = config_data["linear_sweep_voltammetry"]["end_voltage"]
    sweep_rate = config_data["linear_sweep_voltammetry"]["sweep_rate"]

    return start_voltage, end_voltage, sweep_rate


def get_ca_params(config_data):
    voltage = config_data["chronoamperometry"]["voltage"]
    time = config_data["chronoamperometry"]["time"]

    return voltage, time


def get_cv_params(config_data):
    start_voltage = config_data["cyclic_voltammetry"]["start_voltage"]
    first_turnover = config_data["cyclic_voltammetry"][
        "first_turnover_voltage"
    ]
    second_turnover = config_data["cyclic_voltammetry"][
        "second_turnover_voltage"
    ]
    sweep_rate = config_data["cyclic_voltammetry"]["sweep_rate"]
    cycle_number = config_data["cyclic_voltammetry"]["number_of_cycles"]

    return (
        start_voltage,
        first_turnover,
        second_turnover,
        sweep_rate,
        cycle_number,
    )


def get_exp_type(config_data):
    exp_type = config_data["general_parameters"]["experiment_type"]

    return exp_type


def get_exp_time(config_data):
    exp_time = config_data["chronoamperometry"]["time"]

    return exp_time


def get_rest(config_data):
    rest_time = config_data["general_parameters"]["rest_time"]

    return rest_time


def get_steps(config_data):
    step_number = config_data["general_parameters"]["step_number"]

    return step_number


def get_adv_params(adv_config_data):
    conversion_factor = adv_config_data["advanced_parameters"][
        "conversion_factor"
    ]
    set_gain = adv_config_data["advanced_parameters"]["setpoint_gain"]
    set_offset = adv_config_data["advanced_parameters"]["setpoint_offset"]
    shunt_resistor = adv_config_data["advanced_parameters"]["shunt_resistor"]
    time_step = adv_config_data["advanced_parameters"]["time_step"]
    average_number = adv_config_data["advanced_parameters"]["average_number"]

    return (
        conversion_factor,
        set_gain,
        set_offset,
        shunt_resistor,
        time_step,
        average_number,
    )


def check_config_inputs(arg):
    """Checks that all the data that should be numerical from that config can
    be represented as a float.

    Parameters
    __________
    arg: unknown
        any argument can be passed.

    Returns
    _______
    is_number: Boolean
        Value is True if the arg is a number, False if not.
    """
    try:
        return isinstance(float(arg), float)
    except:
        return False


if __name__ == "__main__":
    # used for debugging.  Does the function load the configs?
    data = parse_config_file("C:/Users/user/PycharmProjects/pytentiostat/tests/static/config.yml")
    data_out_name = data["general_parameters"]["data_output_filename"]
    print(data_out_name)
