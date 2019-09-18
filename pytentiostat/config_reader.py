import yaml
import datetime
import time
import sys
import os


def parse_config_file(configlocation=None):
    """
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

    """
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
    """
    Obtains output filename and output filepath from config file data

    Parameters
    ----------
    config_data : dict
        the configuration data
        
    override_ts : Unique string to add after output filename in stringe. Optional.
        If not specified will add a time stamp hours, minutes, and seconds the experiment
        was conducted at as a unique identifier.

    Returns
    -------
    out_name_ts : str
        the output filename with unique identifier.
        
    data_out_path : str
        the path to which the output file will be written to.

    """
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
    """
    Obtains the parameters for a linear sweep voltammetry experiment

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    start_voltage : float
        The voltage to start the sweep at in volts.
        
    end_voltage : float
        The voltage to end the sweep at in volts.
        
    sweep_rate : float
        The rate at which the experiment is performed in millivolts per second.

    """
    start_voltage = config_data["linear_sweep_voltammetry"]["start_voltage"]
    end_voltage = config_data["linear_sweep_voltammetry"]["end_voltage"]
    sweep_rate = config_data["linear_sweep_voltammetry"]["sweep_rate"]

    return start_voltage, end_voltage, sweep_rate


def get_ca_params(config_data):
    """
    Obtains the parameters for a chronoamperometry experiment

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    voltage : float
        The voltage which will be held at in volts.
        
    time: float
        How long the voltage will be held in seconds.

    """
    voltage = config_data["chronoamperometry"]["voltage"]
    time = config_data["chronoamperometry"]["time"]

    return voltage, time


def get_cv_params(config_data):
    """
    Obtains the parameters for a cyclic voltammetry experiment

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    start_voltage : float
        The voltage to start the experiment at in volts.
        
    first_turnover : float
        The voltage at which the voltage sweep will first change directions in volts.
        
    second_turnover: float
        the second voltage at which the voltage sweep will change directions in volts.
        
    sweep_rate : float
        The rate at which the experiment is performed in mV/s.
        
    cycle_number: int
        How many times to perform this cycle.

    """
    start_voltage = config_data["cyclic_voltammetry"]["start_voltage"]
    first_turnover = config_data["cyclic_voltammetry"]["first_turnover_voltage"]
    second_turnover = config_data["cyclic_voltammetry"]["second_turnover_voltage"]
    sweep_rate = config_data["cyclic_voltammetry"]["sweep_rate"]
    cycle_number = config_data["cyclic_voltammetry"]["number_of_cycles"]

    return start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number


def get_exp_type(config_data):
    """
    Obtains the type of experiment

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    exp_type : str
        The type of experiment to be run

    """
    exp_type = config_data["general_parameters"]["experiment_type"]

    return exp_type


def get_exp_time(config_data):
    """
    Obtains the how long the experiment is to be run for the chronoamperometry case

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    exp_time : float
        How long the experiment will be run in seconds.

    """
    exp_time = config_data["chronoamperometry"]["time"]

    return exp_time


def get_rest(config_data):
    """
    Obtains how long to hold before experiment starts

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    rest_time : float
        How long the starting voltage will be held in seconds.

    """
    rest_time = config_data["general_parameters"]["rest_time"]

    return rest_time
    
def get_steps(config_data):
    """
    Obtains how many points will be measured during experiment

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    step_number : int
        How many points will be measured during the experiment

    """
    step_number = config_data["general_parameters"]["step_number"]
    
    return step_number


def get_adv_params(adv_config_data):
    """
    Obtains parameters that shouldn't be altered by beginning users largely related to calibration.

    Parameters
    ----------
    config_data : dict
        the configuration data

    Returns
    -------
    conversion_factor : float
        Value to convert output number to real voltage measured.
    setpoint_adjuster: float
        Value to shift the starting scheduled voltage to match the input voltage.
    shunt_resistor: float
        Value to adjust for internal resistance largely set by shunt resistor to measure current passed.
    time_step: float
        Minimum time to execute read/write cycle.
    average_number: int
        Number of times the measurement at each point will be performed.

    """
    conversion_factor = adv_config_data["advanced_parameters"]["conversion_factor"]
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
    """
    Checks that all the data that should be numerical from that config
    can be represented as a float.

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
    data = parse_config_file("pytentiostat/tests/static")
    data_out_name = data["general_parameters"]["data_output_filename"]
    print(data_out_name)
