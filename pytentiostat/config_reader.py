import yaml
import datetime
import time
import sys
import os


def parse_config_file(configlocation=None):
    '''
    Reads config data from the config file

    the config file must be called config.yml.

    Parameters
    ----------
    configlocation : str
        the path on the filesystem to the config file.  Optional.  If not
        specified pytentiostat looks in the current directory for the
        config files.

    Returns
    -------
    config_data : dict
        the configuration data

    '''
    if not configlocation:
        configlocation = "./"
    try:
        files_in_configlocation = os.listdir(configlocation)
        config_check = "Not Found"
        for i in files_in_configlocation:
            if (i == "config.yml"):
                config_check = "Found"
        if (config_check != "Found"):
            sys.exit("No file named config.yml found in config directory {}. Exiting...".format(configlocation))
        else:
            with open(os.path.join(configlocation, "config.yml"), "r") as stream:
                config_data = yaml.safe_load(stream)
                return config_data
    except FileNotFoundError:
        sys.exit("Directory containing config file, {}, not found. Exiting...".format(configlocation))

def get_output_params(config_data, override_ts=None):
    data_out_name = config_data["general_parameters"]["data_output_filename"]
    data_out_path = config_data["general_parameters"]["data_output_path"]
    if data_out_path.lower() == "desktop":
        data_out_path = os.path.join(os.path.join(os.path.expanduser("~")),
                                   "Desktop")
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
    start_voltage = config_data["cyclic_voltomoetry"]["start_voltage"]
    first_turnover = config_data["cyclic_voltomoetry"]["first_turnover_voltage"]
    second_turnover = config_data["cyclic_voltomoetry"]["second_turnover_voltage"]
    sweep_rate = config_data["cyclic_voltomoetry"]["sweep_rate"]
    cycle_number = config_data["cyclic_voltomoetry"]["number_of_cycles"]

    return start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number


def get_exp_type(config_data):
    exp_type = config_data["general_parameters"]["experiment_type"]

    return exp_type


def get_exp_time(config_data):
    exp_time = config_data["chronoamperometry"]["time"]

    return exp_time


def get_rest(config_data):
    try:
        rest_time = config_data["general_parameters"]["rest_time"]
        time.sleep(rest_time)
    except:
        sys.exit("Could not read config file. Exiting...")


def get_adv_params(adv_config_data):
    conversion_factor = adv_config_data["advanced_parameters"]["conversion_factor"]
    shunt_resistor = adv_config_data["advanced_parameters"]["shunt_resistor"]
    time_step = adv_config_data["advanced_parameters"]["time_step"]
    average_number = adv_config_data["advanced_parameters"]["average_number"]
    time_per_measurement = time_step * average_number
    time_factor = adv_config_data["advanced_parameters"]["time_factor"]

    return (
        conversion_factor,
        shunt_resistor,
        time_step,
        average_number,
        time_per_measurement,
        time_factor,
    )


if __name__ == "__main__":
    # used for debugging.  Does the function load the configs?
    data = parse_config_files("pytentiostat/tests/static")
    data_out_name = data["general_parameters"]["data_output_filename"]
    print(data_out_name)
