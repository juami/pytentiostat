# -*- coding: utf-8 -*-

from pyfirmata import Arduino, util
from matplotlib import pyplot as plt
import time
import numpy as np
import pandas as pd
import serial.tools.list_ports

print('Welcome to the JUAMI pytentiostat interface!')
print('Searching for potentiostat...')

ports = list(serial.tools.list_ports.comports())  # get list of serial ports connected
arduinos = 0
for p in ports:  # Checking for Arduino Unos connected
  if 'Arduino Uno' in p.description:
    com = p.device
    arduinos += 1

if arduinos > 1:  # If two Arduino Unos are found, program exits
  print('More than one Arduino Uno found. Exiting...')
  time.sleep(5)
  exit()

if arduinos == 0:  # If no Arduino Uno is found, program exits
  print('No JUAMI potentiostat found. Exiting...')
  time.sleep(5)
  exit()


try:
  board = Arduino(com)  # opens communication to Arduino
except:
  print('Error. Could not open COM port')
  time.sleep(5)
  exit()
print('Potentiostat connected (' + com + '). Reading configuration file...')
try:
  time.sleep(0)  # Place holder until config file is finished
  # config = yaml.load(file)
except:
  print('Could not read file. Exiting...')
  time.sleep(5)
  exit()


print('Configuration file loaded successfully. Beginning experiment...')
'----------------------------------------------------------------------------'
'----------------------------------------------------------------------------'
# User defined variables
quiet_time = 5.0  # specify time for arduino to wait before recording data.
                  # This removes charging current if desired by the user
start_V = 0.74
stop_V = -0.74
sn_rt_V_p_s = 0.1
'-----------------------------------------------------------------------------'
'-----------------------------------------------------------------------------'
it = util.Iterator(board)
it.start()


# Setup Arduino pins
a0 = board.get_pin('a:0:i')  # Set analog pin 0 as input
a2 = board.get_pin('a:2:i')  # Set analog pin 2 as input
d9 = board.get_pin('d:9:p')  # Set digital pin 9 (PWM) as output


# Hard coded variables that the user can't change
min_stp_sz = 1.4/255.0
min_timestep = 0.005


step_num = abs(int((stop_V - start_V)/min_stp_sz))   # the number of steps between
StepList = np.linspace(start_V, stop_V, num=step_num)
TimeStep = abs((stop_V - start_V)/(sn_rt_V_p_s*step_num))
PWM_steplist = []
for t in StepList:
  PWM_steplist.append((t-(-1.0))/(1.0-(-1.0)))  # Mapping voltage value to PWM duty cycle
StartTime = time.time()

Times = []
Voltages = []
Currents = []

plt.show()

axes = plt.gca()
axes.set_xlim(-1,1)
axes.set_ylim(0,1)
line, = axes.plot(Voltages, Currents, 'r-')
#plt.xlabel('Time (s)')
plt.ylabel('current')
plt.xlabel('Voltage read (V)')


d9.write(PWM_steplist[0])
print('Quiet time ' + str(quiet_time) + 's')
time.sleep(quiet_time)

for x in PWM_steplist:
  
  d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
  time.sleep(min_stp_sz)
  Pin0Value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
  Pin2Value = a2.read()
  NowTime = time.time()
  TimePassed = NowTime-StartTime
  Times.append(TimePassed)
  real_voltage = (Pin0Value-0.5)*-1*2.86
  Voltages.append(real_voltage)
  Currents.append(Pin2Value)
  line.set_ydata(Currents)
  line.set_xdata(Voltages)
  plt.draw()
  plt.pause(1e-17)
  time.sleep(TimeStep)

print('LSV complete')
plt.show()  
board.exit()

# Saving data
#data = pd.DataFrame(list(zip(Times,Currents,Voltages)),columns=['time','current','voltage'])
#data.to_csv('JUAMI_lsvouput.csv')