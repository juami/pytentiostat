import yaml
import datetime
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
                print("Config loaded.\n")
                param_checker(config_data)
                return config_data
                
    except FileNotFoundError:
        sys.exit("Directory containing config file, {}, not found. Exiting...".format(configlocation))
        
def param_checker(config_data):
    """
    Checks the parameters in the config file.

    If finds a parameter that is incorrect, will prompt user what is incorrect.
    Parameters
    ----------
    config_data : dict
        Dictionary containing the data for parameters in the config file.

    Returns
    -------
    None

    """
    #Obtain all the parameters in parsable way
    average_number = config_data["advanced_parameters"]["average_number"]
    conversion_factor = config_data["advanced_parameters"]["conversion_factor"]
    cv_start_voltage = config_data["cyclic_voltammetry"]["start_voltage"]
    cv_sweep_rate = config_data["cyclic_voltammetry"]["sweep_rate"]
    cycle_number = config_data["cyclic_voltammetry"]["number_of_cycles"]
    data_out_name = config_data["general_parameters"]["data_output_filename"]
    data_out_path = config_data["general_parameters"]["data_output_path"]
    end_voltage = config_data["linear_sweep_voltammetry"]["end_voltage"]
    exp_time = config_data["chronoamperometry"]["time"]
    exp_type = config_data["general_parameters"]["experiment_type"]
    lsv_start_voltage = config_data["linear_sweep_voltammetry"]["start_voltage"]
    first_turnover = config_data["cyclic_voltammetry"]["first_turnover_voltage"]
    lsv_sweep_rate = config_data["linear_sweep_voltammetry"]["sweep_rate"]
    rest_time = config_data["general_parameters"]["rest_time"]
    second_turnover = config_data["cyclic_voltammetry"]["second_turnover_voltage"]
    set_gain = config_data["advanced_parameters"]["setpoint_gain"]
    set_offset = config_data["advanced_parameters"]["setpoint_offset"]
    shunt_resistor = config_data["advanced_parameters"]["shunt_resistor"]
    step_number = config_data["general_parameters"]["step_number"]
    time_step = config_data["advanced_parameters"]["time_step"]
    voltage = config_data["chronoamperometry"]["voltage"]
    
    #Check if every variable is of the correct type
    for i in [data_out_name, data_out_path]:
        bool = isinstance(i, str)
        if bool == False:
            sys.exit("Warning! \nThe value ", i, " in config.yml is not a string. \nExiting...")
                      
    
    for i in [average_number, cycle_number, step_number]:
        bool = isinstance(i, int)
        if bool == False:
            sys.exit("Warning! \nThe value ", i, " in config.yml is not an integer. \nExiting...")
                
    for i in [conversion_factor, cv_start_voltage, cv_sweep_rate, end_voltage, 
              exp_time, first_turnover, lsv_start_voltage, lsv_sweep_rate, rest_time, 
              second_turnover, set_gain, set_offset, shunt_resistor, time_step,
              voltage]:
        bool = isinstance(i, float)
        if bool == False:
            bool = isinstance(i, int)
        if bool == False:
            sys.exit("Warning! \nThe value ", i, " in config.yml is not a number. \nExiting...")
    
    for i in [rest_time, step_number, lsv_sweep_rate, cv_sweep_rate,
             cycle_number, exp_time, conversion_factor, set_gain,
             shunt_resistor, time_step, average_number]:
        if i<=0:
                sys.exit("Warning! \nThe value ", i, " needs to be changed to a value >= 0. \nExiting...")
            
    #Check if an available experiment is selected
    exp_types = ['LSV', 'CV', 'CA']
    if exp_type not in  exp_types:
        sys.exit("Warning! \n",exp_type," in config.yml is not a valid experiment type. \nExiting...")
        
    #Check if within experimental limitations
    voltage_ub = 2.2
    voltage_lb = -2.2
    time_step_lb = 0.003
    time_per_step = time_step*average_number
    
    if exp_type == 'LSV':
        voltage_range = abs(end_voltage-lsv_start_voltage)
        time_for_range = voltage_range / (lsv_sweep_rate / 1000)
    elif exp_type == 'CV':
        first_voltage_range = abs(cv_start_voltage - first_turnover)  
        second_voltage_range = abs(first_turnover - second_turnover)  
        third_voltage_range = abs(second_turnover - cv_start_voltage)
        voltage_range = first_voltage_range+second_voltage_range+third_voltage_range
        time_for_range = voltage_range / (cv_sweep_rate / 1000)
    elif exp_type == 'CA':
        time_for_range = exp_time
    
    if time_for_range == 0:
        sys.exit("Warning! \nTime for given experiment = 0. \nExiting...")
    
    lag_tolerance = 2    
    print(time_for_range, time_per_step)
    step_number_ub = int(1/(lag_tolerance*time_per_step/time_for_range))
    
    for i in [cv_start_voltage, first_turnover, second_turnover,
              lsv_start_voltage, end_voltage, voltage]:
        if i<voltage_lb or i>voltage_ub:
            sys.exit("Warning! \nVoltages in config.yml should be < ",voltage_ub,
                  " and > ", voltage_lb,". \nExiting...")
    if time_step < time_step_lb:
        sys.exit("Warning! \nTime step must be >=",time_step_lb,". \nExiting...")
    if step_number > step_number_ub:
        sys.exit("Warning! \nStep number must be <=",step_number_ub,
              " given the other input parameters. \nExiting...")      

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
    start_voltage = config_data["cyclic_voltammetry"]["start_voltage"]
    first_turnover = config_data["cyclic_voltammetry"]["first_turnover_voltage"]
    second_turnover = config_data["cyclic_voltammetry"]["second_turnover_voltage"]
    sweep_rate = config_data["cyclic_voltammetry"]["sweep_rate"]
    cycle_number = config_data["cyclic_voltammetry"]["number_of_cycles"]

    return start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number


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
    data = parse_config_file()
    
