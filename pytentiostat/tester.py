# Standard Libraries
import time
import sys
import numpy as np

# Pytentiostat function files
from pytentiostat.plotter import plot_initializer, plot_updater
import pytentiostat.config_reader as cr

# Global lists for config_data to be used by functions
times = []
voltages = []
currents = []


def start_exp(d9, normalized_start, data):
    """
    Initializes the writing pin and gets the current time before the experiment
    starts

    Parameters
    __________
    d9: pyFirmata/Arduino object
        object that represents the digital pin 9 on the Arduino. Instance
        created in routines.py, startup_routine().
    normalized_start: float
        Number from 0 to 1 that sets the duty cycle of pin 9 before the
        experiment starts

    Returns
    _______
    start_time: float
        Starting time of the experiment

    """
    d9.write(normalized_start)
    cr.get_rest(data)
    start_time = time.time()

    return start_time


def read_write(
    start_time, d9, a0, a2, steps_list, average, line, time_step, cf, sr, config_data
):
    """
    Writes voltages to pin 9 using d9, reads voltages from pin 0 and 2 using a0
    and a2, and calculates current from the voltage on a2.

    Parameters
    __________
    start_time: float
        Time the experiment starts
    d9: pyFirmata/Arduino object
        object used to write the voltage with PWM on pin 9.
    a0: pyFirmata/Arduino object
        object used to read the voltage from pin a0.
    a2: pyFirmata/Arduino object
        object used to read the voltage from pin a2.
    steps_list: list
        List that contains the voltages that should be written in LSV
        and CV experiments
    average: int
        Number of times the readings are averaged before being recorded.
    line: pyplot object
        Determines the axes labels in the plot. Created in plotter.py,
        plot_initializer().
    time_step: float
        Time to wait between points
    cf: float
        Conversion factor to correct the current and voltage readings
    sr: float
        Shunt resistor used to correct the current reading
    data: dict
        Dictionary that contains the data read from the config file.

    Returns
    _______
    nothing

    """

    for x in steps_list:

        # update time
        now_time = time.time()
        time_passed = now_time - start_time
        times.append(time_passed)

        i = 0
        voltage_catcher = 0
        current_catcher = 0

        while i < average:
            d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
            time.sleep(time_step)
            pin0value = (
                a0.read()
            )  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
            pin2value = a2.read()

            real_voltage = (pin0value - 0.5) * -1 * cf
            real_current = ((pin2value - 0.5) * -1 * cf) / sr

            voltage_catcher = voltage_catcher + real_voltage
            current_catcher = current_catcher + real_current

            i = i + 1

        voltage_average = voltage_catcher / average
        current_average = current_catcher / average
        voltages.append(voltage_average)
        currents.append(current_average)
        collected_data = zip(times, voltages, currents)
        plot_updater(config_data, collected_data, line)


def experiment(config_data, board, a0, a2, d9):
    """
    Determines which experiment to run and applies the appropriate voltages
    to perform the experiment based on the inputs from the config file. Plots
    the data for and returns the data as lists to be saved.

    data: dict
        Dictionary containing data read from the config file
    adv_data: dict
        Dictionary containing data read from the config file
    board: pyFirmata/Arduino object
        Serial object used to communicate to the Arduino
    a0: pyFirmata/Arduino object
        object used to read the voltage from pin a0.
    a2: pyFirmata/Arduino object
        object used to read the voltage from pin a2.
    d9: pyFirmata/Arduino object
        object used to write the voltage with PWM from pin 9.

    Returns
    _______
    times: list
        List of floats containing the time each data point was recorded at
    voltages: list
        List of floats containing the corrected voltages at each data point
    currents: list
        List of floats containing the corrected currents at each data point

    """
    # Constants for every experiment
    conversion_factor, setpoint_adjuster, shunt_resistor, time_step, average_number, time_factor = cr.get_adv_params(
        config_data
    )

    # Check the values in adv_config.yml
    for i in [conversion_factor, setpoint_adjuster, shunt_resistor, time_step, average_number, time_factor]:
        if not cr.check_config_inputs(i):
            print("\x1b[0;31;0m" + "Error! \nThe value ", i, " in adv.config.yml is not a number" + "\x1b[0m")
            sys.exit()
    time_per_measurement = time_step * average_number
    # This will be loaded from config
    exp_type = cr.get_exp_type(config_data)

    if exp_type == "LSV":

        start_voltage, end_voltage, sweep_rate = cr.get_lsv_params(config_data)
        # Check the values from config.yml
        for i in [start_voltage, end_voltage, sweep_rate]:
            if not cr.check_config_inputs(i):
                print("\x1b[0;31;0m" + "Error! \nThe value ", i, " in config.yml is not a number" + "\x1b[0m")
                sys.exit()
        sweep_rate = sweep_rate * time_factor
        normalized_start = (start_voltage + 2.5) / 5  # for PWM
        normalized_end = (end_voltage + 2.5) / 5

        voltage_range = abs(end_voltage - start_voltage)  # V
        time_for_range = voltage_range / (sweep_rate / 1000)  # s
        step_number = int(time_for_range / time_per_measurement)

        steps_list = np.linspace(normalized_start, normalized_end, num=step_number)*setpoint_adjuster

    elif exp_type == "CA":

        voltage, time_for_range = cr.get_ca_params(config_data)
        # Check the values from config.yml
        for i in [voltage, time_for_range]:
            if not cr.check_config_inputs(i):
                print("\x1b[0;31;0m" + "Error! \nThe value ", i, " in config.yml is not a number" + "\x1b[0m")
                sys.exit()
        normalized_voltage = (voltage + 2.5) / 5
        time_for_range = time_for_range / time_factor
        step_number = int(time_for_range / time_per_measurement)

        steps_list = np.linspace(normalized_voltage, normalized_voltage, step_number)*setpoint_adjuster

    elif exp_type == "CV":

        start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number = cr.get_cv_params(
            config_data
        )
        # Check the values from config.yml
        for i in [start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number]:
            if not cr.check_config_inputs(i):
                print("\x1b[0;31;0m" + "Error! \nThe value ", i, " in config.yml is not a number" + "\x1b[0m")
                sys.exit()
        sweep_rate = sweep_rate * time_factor
        normalized_start = (start_voltage + 2.5) / 5
        norm_first_turnover = (first_turnover + 2.5) / 5
        norm_second_turnover = (second_turnover + 2.5) / 5

        first_voltage_range = abs(first_turnover - start_voltage)  # V
        second_voltage_range = abs(second_turnover - start_voltage)  # V
        third_voltage_range = abs(start_voltage - second_turnover)  # V

        first_time_range = first_voltage_range / (sweep_rate / 1000)  # s
        second_time_range = second_voltage_range / (sweep_rate / 1000)  # s
        third_time_range = third_voltage_range / (sweep_rate / 1000)  # s

        first_step_number = int(first_time_range / time_per_measurement)
        second_step_number = int(second_time_range / time_per_measurement)
        third_step_number = int(third_time_range / time_per_measurement)

        first_steps_list = np.linspace(
            normalized_start, norm_first_turnover, num=first_step_number
        )*setpoint_adjuster
        second_steps_list = np.linspace(
            norm_first_turnover, norm_second_turnover, num=second_step_number
        )*setpoint_adjuster
        third_steps_list = np.linspace(
            norm_second_turnover, normalized_start, num=third_step_number
        )*setpoint_adjuster
    else:
        sys.exit("Error! \nThe experiment_type field in config.yml is not an accepted value")


    # Starting up the plot
    line = plot_initializer(config_data)

    # Main experiment part

    if exp_type == "LSV":

        start_time = start_exp(d9, normalized_start, config_data)

        read_write(
            start_time,
            d9,
            a0,
            a2,
            steps_list,
            average_number,
            line,
            time_step,
            conversion_factor,
            shunt_resistor,
            config_data,
        )

        return times, voltages, currents

    elif exp_type == "CA":

        start_time = start_exp(d9, normalized_voltage, config_data)

        read_write(
            start_time,
            d9,
            a0,
            a2,
            steps_list,
            average_number,
            line,
            time_step,
            conversion_factor,
            shunt_resistor,
            config_data,
        )

        return times, voltages, currents

    elif exp_type == "CV":

        start_time = start_exp(d9, normalized_start, config_data)

        read_write(
            start_time,
            d9,
            a0,
            a2,
            first_steps_list,
            average_number,
            line,
            time_step,
            conversion_factor,
            shunt_resistor,
            config_data,
        )
        read_write(
            start_time,
            d9,
            a0,
            a2,
            second_steps_list,
            average_number,
            line,
            time_step,
            conversion_factor,
            shunt_resistor,
            config_data,
        )
        read_write(
            start_time,
            d9,
            a0,
            a2,
            third_steps_list,
            average_number,
            line,
            time_step,
            conversion_factor,
            shunt_resistor,
            config_data,
        )

        return times, voltages, currents
