#Standard Libraries
import time
import numpy as np

#Pytentiostat function files
import Plotter as plotter

#Constants for every experiment
Conversion_Factor = 4.798 # To voltage real voltage range
Shunt_Resistor = 0.202
TimeStep = 0.003 #s
Average_Number = 5

Exp_Type = 'LSV'
Start_Voltage = -1.5 #V
End_Voltage = 1.5 #V
Normalized_Start = ((Start_Voltage+2.5)/5) #for PWM
Normalized_End = ((End_Voltage+2.5)/5)
Sweep_Rate = 100 #mV/s

Time_Per_Measurement = TimeStep*2*Average_Number

Voltage_Range = abs(End_Voltage-Start_Voltage) #V
Time_For_Range = Voltage_Range/(Sweep_Rate/1000) #s
Step_Number = int(Time_For_Range/Time_Per_Measurement)

StepsList = np.linspace(Normalized_Start, Normalized_End, num=Step_Number)

Times = []
Voltages = []
Currents = []

#Starting up the plot
line = plotter.PlotInitializer(Exp_Type)



def Experiment(board, a0, a2, d9):
    
    Start_Time = time.time()
    
    if Exp_Type == 'LSV':
    
        for x in StepsList:
          
          i = 0
          voltage_catcher = 0
          current_catcher = 0
          
          now_time = time.time()
          time_passed = now_time-Start_Time
          Times.append(time_passed)
          
          while i < Average_Number:
              
              time.sleep(TimeStep)
              d9.write(x) #Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
              time.sleep(TimeStep)
              pin0value = a0.read() #Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
              pin2value = a2.read()
              
             
              real_voltage = (pin0value-0.5)*-1*Conversion_Factor
              real_current = ((pin2value-0.5)*-1*Conversion_Factor)/Shunt_Resistor
              
              voltage_catcher = voltage_catcher + real_voltage
              current_catcher = current_catcher + real_current
              
              i=i+1
              
          voltage_average = voltage_catcher/Average_Number
          current_average = current_catcher/Average_Number
          Voltages.append(voltage_average)
          Currents.append(current_average)
          zippy = zip(Times, Voltages, Currents)
          plotter.PlotUpdater(Exp_Type, zippy, line)
          
        return Times, Voltages, Currents
    
    elif Exp_Type == 'CA':
        
        print('CA is not currently available')
        
    elif Exp_Type == 'CV':
        
        print('CV is not currently available')
        
    else:
        
        print('Valid experiment type not entered')