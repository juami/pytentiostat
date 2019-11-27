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
    average_number = {'name': 'average_number', 'value': config_data["advanced_parameters"]["average_number"]}
    conversion_factor = {'name': 'conversion_factor', 'value': config_data["advanced_parameters"]["conversion_factor"]}
    cv_start_voltage = {'name': 'start_voltage', 'value': config_data["cyclic_voltammetry"]["start_voltage"]}
    cv_sweep_rate = {'name': 'sweep_rate', 'value': config_data["cyclic_voltammetry"]["sweep_rate"]}
    cycle_number = {'name': 'number_of_cycles', 'value': config_data["cyclic_voltammetry"]["number_of_cycles"]}
    data_out_name = {'name': 'data_output_filename', 'value': config_data["general_parameters"]["data_output_filename"]}
    data_out_path = {'name': 'data_output_path', 'value': config_data["general_parameters"]["data_output_path"]}
    end_voltage = {'name': 'end_voltage', 'value': config_data["linear_sweep_voltammetry"]["end_voltage"]}
    exp_time = {'name': 'time', 'value': config_data["chronoamperometry"]["time"]}
    exp_type = {'name': 'experiment_type', 'value': config_data["general_parameters"]["experiment_type"]}
    lsv_start_voltage = {'name': 'start_voltage', 'value': config_data["linear_sweep_voltammetry"]["start_voltage"]}
    first_turnover = {'name': 'first_turnover_voltage', 'value': config_data["cyclic_voltammetry"]["first_turnover_voltage"]}
    lsv_sweep_rate = {'name': 'sweep_rate', 'value': config_data["linear_sweep_voltammetry"]["sweep_rate"]}
    rest_time = {'name': 'rest_time', 'value': config_data["general_parameters"]["rest_time"]}
    second_turnover = {'name': 'second_turnover_voltage', 'value': config_data["cyclic_voltammetry"]["second_turnover_voltage"]}
    set_gain = {'name': 'setpoint_gain', 'value': config_data["advanced_parameters"]["setpoint_gain"]}
    set_offset = {'name': 'setpoint_offset', 'value': config_data["advanced_parameters"]["setpoint_offset"]}
    shunt_resistor = {'name': 'shunt_resistor', 'value': config_data["advanced_parameters"]["shunt_resistor"]}
    step_number = {'name': 'step_number', 'value': config_data["general_parameters"]["step_number"]}
    time_step = {'name': 'time_step', 'value': config_data["advanced_parameters"]["time_step"]}
    voltage = {'name': 'voltage', 'value': config_data["chronoamperometry"]["voltage"]}
    
    for i in [data_out_name, data_out_path]:
        val = i['value']
        if isinstance(val, str) == False:
            sys.exit("""Warning! \nThe value {value} for {name} in config.yml is not valid.
                     \nPlease enter a new value for {name} avoiding unusual characters. 
                     \nExiting...""".format(**i))
                      
    
    for i in [average_number, cycle_number, step_number]:
        val = i['value']
        if isinstance(val, int) == False:
            sys.exit("""Warning! \nThe value {value} for {name} in config.yml is not valid.
                     \nPlease change the entry to a positive integer. 
                     \nExiting...""".format(**i))
                
    for i in [conversion_factor, cv_start_voltage, cv_sweep_rate, end_voltage, 
              exp_time, first_turnover, lsv_start_voltage, lsv_sweep_rate, rest_time, 
              second_turnover, set_gain, set_offset, shunt_resistor, time_step,
              voltage]:
        val = i['value']
        if isinstance(val, (float, int)) == False:
            sys.exit("""Warning! \nThe value {value} for {name} in config.yml is not valid.
                     \nPlease change the entry to a number.
                     \nExiting...""".format(**i))
    
    for i in [rest_time, step_number, lsv_sweep_rate, cv_sweep_rate,
             cycle_number, exp_time, conversion_factor, set_gain,
             shunt_resistor, time_step, average_number]:
        val = i['value']
        if val<=0:
             sys.exit("""Warning! \nThe value {value} for {name} in config.yml is not valid.
                      \nPlease change the entry to a value greater than or equal to zero.
                      \nExiting...""".format(**i))
            
    exp_types = ['LSV', 'CV', 'CA']
    val = exp_type['value']
    if val not in  exp_types:
        sys.exit("""Warning! \nThe entry {value} for {name} is not valid. 
                 \nPlease change the entry to CA, CV, or LSV.
                 \nExiting...""".format(**exp_type))
        
    voltage_ub = 2.2
    voltage_lb = -2.2
    time_step_lb = 0.003
    time_per_step = time_step['value']*average_number['value']
    
    if exp_type['value'] == 'LSV':
        voltage_range = abs(end_voltage['value']-lsv_start_voltage['value'])
        time_for_range = voltage_range / (lsv_sweep_rate['value'] / 1000)
    elif exp_type['value'] == 'CV':
        first_voltage_range = abs(cv_start_voltage['value'] - first_turnover['value'])  
        second_voltage_range = abs(first_turnover['value'] - second_turnover['value'])  
        third_voltage_range = abs(second_turnover['value'] - cv_start_voltage['value'])
        voltage_range = first_voltage_range+second_voltage_range+third_voltage_range
        time_for_range = voltage_range / (cv_sweep_rate['value'] / 1000)
    elif exp_type['value'] == 'CA':
        time_for_range = exp_time['value']
    
    if time_for_range == 0:
        sys.exit("""Warning! \nThe total time for range in config.yml in not valid.
                 \nPlease enter a new value greater than 0 and try again.
                 \nExiting...""".format(str(time_for_range)))
    
    lag_tolerance = 2    
    step_number_ub = int(1/(lag_tolerance*time_per_step/time_for_range))
    
    for i in [cv_start_voltage, first_turnover, second_turnover,
              lsv_start_voltage, end_voltage, voltage]:
        val = i['value']
        if val<voltage_lb or val>voltage_ub:
            sys.exit("""Warning! \nVoltages in config.yml should be < {} and > {}.
                     \n Please change value for {name} to value between the bounds.
                     \nExiting...""".format(str(voltage_ub), str(voltage_lb), **i))
    if time_step['value'] < time_step_lb:
        sys.exit("""Warning! \nTime step value in config.yml must be >= {}.
                 \nPlease change the time step value to be greater than this.
                 \nExiting...""".format(str(time_step_lb)))
    if step_number['value'] > step_number_ub:
        sys.exit("""Warning! \nStep number must be <= {} given the other input parameters.
                 \nPlease change the step number in config.yml to be less than this.
                 \nExiting...""".format(str(step_number_ub)))       

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
    ----------
    arg: unknown
        any argument can be passed.

    Returns
    -------
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
    
