## Standard Libraries
import datetime
import time

import numpy as np

## Local library
# GUI_function
import src.GUI.code.GUI_config_reader as cr


def start_exp(d9, normalized_start, data):
    """Initializes the writing pin and gets the current time before the
    experiment starts.

    Parameters
    ----------
    d9: pyFirmata/Arduino object , object that represents the digital pin 9 on the Arduino.
        Instance is created in GUI_routines.py- startup_routine().

    normalized_start: float , Number from 0 to 1 that sets the duty cycle of pin 9 before the experiment starts

    Returns
    ------
    start_time: float , Starting time of the experiment
    """

    d9.write(normalized_start)
    rest_time = cr.get_rest(data)
    time.sleep(rest_time)
    start_time = time.time()

    return start_time


def read_write(
    start_time,
    d9,
    a0,
    a2,
    step_number,
    steps_list,
    current_exp_time,
    average,
    time_step,
    cf,
    sr,
    ini_plot,
    times,
    voltages,
    currents,
    pr,
    tr,
    total_exp_time,
    passed_exp_time,
    cycle_number,
):
    """Writes voltages to pin 9 using d9, reads voltages from pin 0 and 2 using
    a0 and a2, and calculates current from the voltage on a2.

    Parameters (passed from GUI_operator - experiment function)
    __________
    start_time : float , Time the experiment starts.
                 Instance is created in the GUI_operator.py- experiment function

    d9 : pyFirmata/Arduino object , object used to write the voltage with PWM on pin 9.
        Instance is created in GUI_routines.py- startup_routine().

    a0 : pyFirmata/Arduino object , object used to read the voltage from pin a0.
        Instance is created in GUI_routines.py- startup_routine().

    a2 : pyFirmata/Arduino object , object used to read the voltage from pin a2.
       Instance is created in GUI_routines.py- startup_routine().

    steps_list : list , List that contains the voltages that should be written in LSV and CV experiments.
                Instance is created in the GUI_operator.py- experiment function

    current_exp_time : int , time of the current experiment, units : seconds.
                       Instance is created in the GUI_operator.py- experiment function

    average : int , Number of times the readings are averaged before being recorded.
                   Instance is created in the GUI_operator.py- experiment function

    time_step : float , Time to wait between points.
               Instance is created in the GUI_operator.py- experiment function

    cf : float , Conversion factor to correct the current and voltage readings.
        Instance is created in the GUI_operator.py- experiment function

    sr : float , Shunt resistor used to correct the current reading.
         Instance is created in the GUI_operator.py- experiment function

    ini_plot : Ui_Plot object ,initialized the live plot.
             Instance is created in the GUI_run_exp.py- run_exp_main function

    times : list , List of floats containing the time each data point was recorded at
           Instance is created in the GUI_run_exp.py- run_exp function

    voltages : list , List of floats containing the corrected voltages at each data point
              Instance is created in the GUI_run_exp.py- run_exp function

    currents : list , List of floats containing the corrected currents at each data point
              Instance is created in the GUI_run_exp.py- run_exp function

    pr : QtWidgets.QProgressBar object , initialize the progress_bar live progress update
         Instance is created in the GUI_run_exp.py- run_exp_main function

    tr : QtWidgets.QLineEdit object, initialize the time_remaining_display for live remaining time update
        Instance is created in the GUI_run_exp.py- run_exp_main function

    total_exp_time : int , the total time of all experiments in the queue, units : seconds.
                     Instance is created in the GUI_run_exp.py- run_exp function

    passed_exp_time : int , the total time of all experiments that have been finished, units : seconds.
                      Instance is created in the GUI_run_exp.py- run_exp function

    cycle_number : int ,cycle number for CV experiment, for other experiments, cycle_number = 1

    Returns
    -------
    times: list , List of floats containing the time each data point was recorded at

    voltages: list , List of floats containing the corrected voltages at each data point

    currents: list , List of floats containing the corrected currents at each data point
    """

    starting_time = time.time()
    ending_time = starting_time + current_exp_time
    times_list = np.linspace(
        starting_time, ending_time, num=(step_number + 1) * cycle_number
    )
    times_diff_list = [x - starting_time for x in times_list]
    times_diff_list.append(0)
    t = 1
    while cycle_number:
        for x in steps_list:
            # update time
            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)

            i = 0
            voltage_catcher = 0
            current_catcher = 0

            while i < average:
                d9.write(
                    x
                )  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
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
            currents.append(-1 * current_average)
            collected_data = (times, voltages, currents)

            ###############   update the plot, progress bar and remaining time   ###############
            ini_plot.plot_updater(collected_data)
            pr.setValue((times[-1] + passed_exp_time) / total_exp_time * 100)

            if total_exp_time - passed_exp_time - times[-1] > 0:
                rtime = round(
                    total_exp_time - passed_exp_time - times[-1], 0
                )  # rtime = remaining time
            else:
                rtime = 0  # if rtime < 0 ,set it to 0

            tr.setText(str(datetime.timedelta(seconds=rtime)))
            ###############     ###############    ###############
            rel_time = 0

            while rel_time < times_diff_list[t]:
                time.sleep(time_step)
                now_time = time.time()
                rel_time = now_time - start_time

            t = t + 1
        cycle_number -= 1
    return times, voltages, currents


def experiment(
    config_data,
    board,
    a0,
    a2,
    d9,
    ini_plot,
    times,
    voltages,
    currents,
    pr,
    tr,
    total_exp_time,
    passed_exp_time,
):
    """Determines which experiment to run and applies the appropriate voltages
    to perform the experiment based on the inputs from the config file. Plots
    the data for and returns the data as lists to be saved.

    Parameters
    ----------
    config_data : dictionary, containing data read from the config file
                 Instance is created in the GUI_run_exp.py - run_exp function

    board: pyFirmata/Arduino object , Serial object used to communicate to the Arduino
           Instance is created in GUI_routines.py- startup_routine().

    d9 : pyFirmata/Arduino object , object used to write the voltage with PWM on pin 9.
        Instance is created in GUI_routines.py- startup_routine().

    a0 : pyFirmata/Arduino object , object used to read the voltage from pin a0.
        Instance is created in GUI_routines.py- startup_routine().

    a2 : pyFirmata/Arduino object , object used to read the voltage from pin a2.
        Instance is created in GUI_routines.py- startup_routine().

    ini_plot : Ui_Plot object ,initialized the live plot.
              Instance is created in the GUI_run_exp.py- run_exp_main function

    times: list , List of floats containing the time each data point was recorded at
           Instance is created in the GUI_run_exp.py - run_exp function

    voltages : list , List of floats containing the corrected voltages at each data point
              Instance is created in the GUI_run_exp.py - run_exp function

    currents : list , List of floats containing the corrected currents at each data point
               Instance is created in the GUI_run_exp.py - run_exp function

    pr : QtWidgets.QProgressBar object , initialize the progress_bar live progress update
         Instance is created in the GUI_run_exp.py- run_exp_main function

    tr : QtWidgets.QLineEdit object, initialize the time_remaining_display for live remaining time update
         Instance is created in the GUI_run_exp.py- run_exp_main function

    total_exp_time : int , the total time of all experiments in the queue, units : seconds.
                     Instance is created in the GUI_run_exp.py- run_exp function

    passed_exp_time : int ,record the total time of all the experiments that have been finished, units : seconds.
                      Instance is created in the GUI_run_exp.py- run_exp function

    Returns
    -------
    times : list , List of floats containing the time each data point was recorded at

    voltages : list , List of floats containing the corrected voltages at each data point

    currents : list , List of floats containing the corrected currents at each data point
    """

    # Constants for every experiment
    (
        conversion_factor,
        set_gain,
        set_offset,
        shunt_resistor,
        time_step,
        average_number,
    ) = cr.get_adv_params(config_data)
    step_number = cr.get_steps(config_data)
    exp_type = cr.get_exp_type(config_data)

    if exp_type == "LSV":

        start_voltage, end_voltage, sweep_rate = cr.get_lsv_params(config_data)
        normalized_start = (start_voltage + 2.5) / 5  # for PWM
        normalized_end = (end_voltage + 2.5) / 5

        voltage_range = abs(end_voltage - start_voltage)  # V
        current_exp_time = voltage_range * 1000 / (sweep_rate)  # s
        steps_list = (
            np.linspace(normalized_start, normalized_end, num=step_number + 1)
            * set_gain
            + set_offset
        )
        cycle_number = 1
        start_time = start_exp(d9, normalized_start, config_data)

    elif exp_type == "CA":

        voltage, current_exp_time = cr.get_ca_params(config_data)
        normalized_voltage = (voltage + 2.5) / 5
        steps_list = (
            np.linspace(
                normalized_voltage, normalized_voltage, step_number + 1
            )
            * set_gain
            + set_offset
        )
        cycle_number = 1
        start_time = start_exp(d9, normalized_voltage, config_data)

    elif exp_type == "CV":

        (
            start_voltage,
            first_turnover,
            second_turnover,
            sweep_rate,
            cycle_number,
        ) = cr.get_cv_params(config_data)
        normalized_start = (start_voltage + 2.5) / 5
        norm_first_turnover = (first_turnover + 2.5) / 5
        norm_second_turnover = (second_turnover + 2.5) / 5

        first_voltage_range = abs(first_turnover - start_voltage)  # V
        second_voltage_range = abs(second_turnover - first_turnover)  # V
        third_voltage_range = abs(start_voltage - second_turnover)  # V
        fall = (
            first_voltage_range + second_voltage_range + third_voltage_range
        )  # V
        f1 = first_voltage_range / fall
        num1 = int(f1 * step_number)
        f2 = second_voltage_range / fall
        num2 = int(f2 * step_number)
        num3 = step_number - num1 - num2 + 1

        first_steps_list = (
            np.linspace(
                normalized_start, norm_first_turnover, num=num1, endpoint=False
            )
            * set_gain
            + set_offset
        )
        second_steps_list = (
            np.linspace(
                norm_first_turnover,
                norm_second_turnover,
                num=num2,
                endpoint=False,
            )
            * set_gain
            + set_offset
        )
        third_steps_list = (
            np.linspace(norm_second_turnover, normalized_start, num=num3)
            * set_gain
            + set_offset
        )
        steps_list = np.concatenate(
            (first_steps_list, second_steps_list, third_steps_list), axis=None
        )
        current_exp_time = fall / sweep_rate * 1000 * cycle_number
        start_time = start_exp(d9, normalized_start, config_data)

    # Call the read_write function to record and plot data
    pin_objects = (d9, a0, a2)

    read_write(
        start_time,
        *pin_objects,
        step_number,
        steps_list,
        current_exp_time,
        average_number,
        time_step,
        conversion_factor,
        shunt_resistor,
        ini_plot,
        times,
        voltages,
        currents,
        pr,
        tr,
        total_exp_time,
        passed_exp_time,
        cycle_number
    )

    return times, voltages, currents
