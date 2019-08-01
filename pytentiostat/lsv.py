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
start_voltage = 0.74
stop_voltage = -0.74
scan_rate_volt_per_s = 0.1
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


step_num = abs(int((stop_voltage - start_voltage)/min_stp_sz))   # the number of steps between
steplist = np.linspace(start_voltage, stop_voltage, num=step_num)
timestep = abs((stop_voltage - start_voltage)/(scan_rate_volt_per_s*step_num))
pwm_steplist = []
for t in steplist:
  pwm_steplist.append((t-(-1.0))/(1.0-(-1.0)))  # Mapping voltage value to PWM duty cycle
starttime = time.time()

time_list = []
voltage_list = []
current_list = []

plt.show()

axes = plt.gca()
axes.set_xlim(-1,1)
axes.set_ylim(0,1)
line, = axes.plot(voltages, currents, 'r-')
#plt.xlabel('Time (s)')
plt.ylabel('current')
plt.xlabel('Voltage read (V)')


d9.write(pwm_steplist[0])
print('Quiet time ' + str(quiet_time) + 's')
time.sleep(quiet_time)

for x in pwm_steplist:
  
  d9.write(x)  # Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
  time.sleep(min_stp_sz)
  pin0value = a0.read()  # Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
  pin2value = a2.read()
  nowtime = time.time()
  timepassed = nowtime-starttime
  time_list.append(timepassed)
  real_voltage = (pin0value-0.5)*-1*2.86
  voltage_list.append(real_voltage)
  current_list.append(pin2value)
  line.set_ydata(current_list)
  line.set_xdata(voltage_list)
  plt.draw()
  plt.pause(1e-17)
  time.sleep(timestep)

print('LSV complete')
plt.show()  
board.exit()

# Saving data
#data = pd.DataFrame(list(zip(time_list,current_list,voltage_list)),columns=['time','current','voltage'])
#data.to_csv('filename here')
