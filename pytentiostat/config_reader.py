import yaml
import datetime
import time
import sys
import os


def parse_config_files(configlocation=""):
    with open(os.path.join(configlocation, "config.yml"), "r") as stream:
        data = yaml.safe_load(stream)

    with open(os.path.join(configlocation, "adv_config.yml"),
              "r") as adv_stream:
        adv_data = yaml.safe_load(adv_stream)

    return data, adv_data


def get_output_params(data):
    data_out_name = data["general_parameters"]["data_output_filename"]
    data_out_path = data["general_parameters"]["data_output_path"]

    default_condition = "N"

    if data_out_path == "default":
        default_condition = "Y"

    currentDT = datetime.datetime.now()
    ts = currentDT.strftime("%H_%M_%S")

    out_name_ts = data_out_name + "_" + ts + ".csv"

    return out_name_ts, data_out_path, default_condition


def get_lsv_params(data):
    start_voltage = data["linear_sweep_voltammetry"]["start_voltage"]
    end_voltage = data["linear_sweep_voltammetry"]["end_voltage"]
    sweep_rate = data["linear_sweep_voltammetry"]["sweep_rate"]

    return start_voltage, end_voltage, sweep_rate


def get_ca_params(data):
    voltage = data["chronoamperometry"]["voltage"]
    time = data["chronoamperometry"]["time"]

    return voltage, time


def get_cv_params(data):
    start_voltage = data["cyclic_voltomoetry"]["start_voltage"]
    first_turnover = data["cyclic_voltomoetry"]["first_turnover_voltage"]
    second_turnover = data["cyclic_voltomoetry"]["second_turnover_voltage"]
    sweep_rate = data["cyclic_voltomoetry"]["sweep_rate"]
    cycle_number = data["cyclic_voltomoetry"]["number_of_cycles"]

    return start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number


def get_exp_type(data):
    exp_type = data["general_parameters"]["experiment_type"]

    return exp_type


def get_exp_time(data):
    exp_time = data["chronoamperometry"]["time"]

    return exp_time


def get_rest(data):
    try:
        rest_time = data["general_parameters"]["rest_time"]
        time.sleep(rest_time)
    except:
        sys.exit("Could not read config file. Exiting...")


def get_adv_params(adv_data):
    conversion_factor = adv_data["conversion_factor"]
    shunt_resistor = adv_data["shunt_resistor"]
    time_step = adv_data["time_step"]
    average_number = adv_data["average_number"]
    time_per_measurement = time_step * average_number
    time_factor = adv_data["time_factor"]

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
    data, adv_data = parse_config_files("pytentiostat/tests/static")
    data_out_name = data["general_parameters"]["data_output_filename"]
    print(data_out_name)
