#Standard Libraries
import time
import numpy as np

#Pytentiostat function files
import plotter as plotter

#Constants for every experiment
conversion_factor = 4.798 # To voltage real voltage range
shunt_resistor = 0.202
time_step = 0.003 #s
average_number = 5

exp_type = 'LSV'
start_voltage = -1.5 #V
end_voltage = 1.5 #V
normalized_start = ((start_voltage+2.5)/5) #for PWM
normalized_end = ((end_voltage+2.5)/5)
sweep_rate = 100 #mV/s

time_per_measurement = time_step*2*average_number

voltage_range = abs(end_voltage-start_voltage) #V
time_for_range = voltage_range/(sweep_rate/1000) #s
step_number = int(time_for_range/time_per_measurement)

steps_list = np.linspace(normalized_start, normalized_end, num=step_number)

times = []
voltages = []
currents = []

#Starting up the plot
line = plotter.plot_initializer(exp_type)



def Experiment(board, a0, a2, d9):
    
    start_time = time.time()
    
    if exp_type == 'LSV':
    
        for x in steps_list:
          
          i = 0
          voltage_catcher = 0
          current_catcher = 0
          
          now_time = time.time()
          time_passed = now_time-Start_Time
          times.append(time_passed)
          
          while i < average_number:
              
              time.sleep(time_step)
              d9.write(x) #Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
              time.sleep(time_step)
              pin0value = a0.read() #Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
              pin2value = a2.read()
              
             
              real_voltage = (pin0value-0.5)*-1*conversion_factor
              real_current = ((pin2value-0.5)*-1*conversion_factor)/shunt_resistor
              
              voltage_catcher = voltage_catcher + real_voltage
              current_catcher = current_catcher + real_current
              
              i=i+1
              
          voltage_average = voltage_catcher/average_number
          current_average = current_catcher/average_number
          voltages.append(voltage_average)
          currents.append(current_average)
          collected_data = zip(Times, Voltages, Currents)
          plotter.plot_updater(exp_type, collected_data, line)
          
        return times, voltages, currents
    
    elif exp_type == 'CA':
        
        print('CA is not currently available')
        
    elif exp_type == 'CV':
        
        print('CV is not currently available')
        
    else:
        
        print('Valid experiment type not entered')
