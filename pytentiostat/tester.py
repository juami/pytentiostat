# Standard Libraries
import time
import numpy as np

# Pytentiostat function files
from plotter import plot_initializer, plot_updater
import config_reader as cr

# Constants for every experiment
conversion_factor, shunt_resistor, time_step, average_number, time_per_measurement = cr.get_adv_params()

# This will be loaded from config
exp_type = cr.get_exp_type()

if exp_type == 'LSV':
    
    start_voltage, end_voltage, sweep_rate = cr.get_lsv_params()
    normalized_start = (start_voltage + 2.5) / 5  # for PWM
    normalized_end = (end_voltage + 2.5) / 5

    voltage_range = abs(end_voltage - start_voltage)  # V
    time_for_range = voltage_range / (sweep_rate / 1000)  # s
    step_number = int(time_for_range / time_per_measurement)

    steps_list = np.linspace(normalized_start, normalized_end, num=step_number)

elif exp_type == 'CA':
    
    voltage, time_for_range = cr.get_ca_params()
    normalized_voltage = (voltage + 2.5) / 5
    time_for_range = 15  # s
    step_number = int(time_for_range / time_per_measurement)

    steps_list = [normalized_voltage] * step_number

elif exp_type == 'CV':

    start_voltage, first_turnover, second_turnover, sweep_rate, cycle_number = cr.get_cv_params()
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

    first_steps_list = np.linspace(normalized_start, norm_first_turnover, num=first_step_number)
    second_steps_list = np.linspace(norm_first_turnover, norm_second_turnover, num=second_step_number)
    third_steps_list = np.linspace(norm_second_turnover, normalized_start, num=third_step_number)

times = []
voltages = []
currents = []

# Starting up the plot
line = plot_initializer()


def experiment(board, a0, a2, d9):
    start_time = time.time()

    if exp_type == 'LSV':

        for x in steps_list:

            i = 0
            voltage_catcher = 0
            current_catcher = 0

            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)

            while i < average_number:
                time.sleep(time_step)
                d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
                time.sleep(time_step)
                pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
                pin2value = a2.read()

                real_voltage = (pin0value - 0.5) * -1 * conversion_factor
                real_current = ((pin2value - 0.5) * -1 * conversion_factor) / shunt_resistor

                voltage_catcher = voltage_catcher + real_voltage
                current_catcher = current_catcher + real_current

                i = i + 1

            voltage_average = voltage_catcher / average_number
            current_average = current_catcher / average_number
            voltages.append(voltage_average)
            currents.append(current_average)
            collected_data = zip(times, voltages, currents)
            plot_updater(collected_data, line)

        return times, voltages, currents

    elif exp_type == 'CA':

        for x in steps_list:

            i = 0
            voltage_catcher = 0
            current_catcher = 0

            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)

            while i < average_number:
                time.sleep(time_step)
                d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
                time.sleep(time_step)
                pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
                pin2value = a2.read()

                real_voltage = (pin0value - 0.5) * -1 * conversion_factor
                real_current = ((pin2value - 0.5) * -1 * conversion_factor) / shunt_resistor

                voltage_catcher = voltage_catcher + real_voltage
                current_catcher = current_catcher + real_current

                i = i + 1

            voltage_average = voltage_catcher / average_number
            current_average = current_catcher / average_number
            voltages.append(voltage_average)
            currents.append(current_average)
            collected_data = zip(times, voltages, currents)
            plot_updater(collected_data, line)

        return times, voltages, currents

    elif exp_type == 'CV':
        
        for x in first_steps_list:
    
            i = 0
            voltage_catcher = 0
            current_catcher = 0
    
            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)
    
            while i < average_number:
                time.sleep(time_step)
                d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
                time.sleep(time_step)
                pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
                pin2value = a2.read()
    
                real_voltage = (pin0value - 0.5) * -1 * conversion_factor
                real_current = ((pin2value - 0.5) * -1 * conversion_factor) / shunt_resistor
    
                voltage_catcher = voltage_catcher + real_voltage
                current_catcher = current_catcher + real_current
    
                i = i + 1
    
            voltage_average = voltage_catcher / average_number
            current_average = current_catcher / average_number
            voltages.append(voltage_average)
            currents.append(current_average)
            collected_data = zip(times, voltages, currents)
            plot_updater(collected_data, line)
    
        for x in second_steps_list:
    
            i = 0
            voltage_catcher = 0
            current_catcher = 0
    
            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)
    
            while i < average_number:
                time.sleep(time_step)
                d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
                time.sleep(time_step)
                pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
                pin2value = a2.read()
    
                real_voltage = (pin0value - 0.5) * -1 * conversion_factor
                real_current = ((pin2value - 0.5) * -1 * conversion_factor) / shunt_resistor
    
                voltage_catcher = voltage_catcher + real_voltage
                current_catcher = current_catcher + real_current
    
                i = i + 1
    
            voltage_average = voltage_catcher / average_number
            current_average = current_catcher / average_number
            voltages.append(voltage_average)
            currents.append(current_average)
            collected_data = zip(times, voltages, currents)
            plot_updater(collected_data, line)
    
        for x in third_steps_list:
    
            i = 0
            voltage_catcher = 0
            current_catcher = 0
    
            now_time = time.time()
            time_passed = now_time - start_time
            times.append(time_passed)
    
            while i < average_number:
                time.sleep(time_step)
                d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
                time.sleep(time_step)
                pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
                pin2value = a2.read()
    
                real_voltage = (pin0value - 0.5) * -1 * conversion_factor
                real_current = ((pin2value - 0.5) * -1 * conversion_factor) / shunt_resistor
    
                voltage_catcher = voltage_catcher + real_voltage
                current_catcher = current_catcher + real_current
    
                i = i + 1
    
            voltage_average = voltage_catcher / average_number
            current_average = current_catcher / average_number
            voltages.append(voltage_average)
            currents.append(current_average)
            collected_data = zip(times, voltages, currents)
            plot_updater(collected_data, line)

        return times, voltages, currents

    else:

        print('Valid experiment type not entered')
