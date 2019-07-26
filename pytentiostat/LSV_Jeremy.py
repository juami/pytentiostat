# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:03:52 2019

@author: austin
"""

from pyfirmata import Arduino, util
from matplotlib import pyplot as plt
import time
import pandas as pd

    
board = Arduino("COM3")
it = util.Iterator(board)
it.start()

#Setup Arduino pins
a0 = board.get_pin('a:0:i') #Analog pin 0 
a2 = board.get_pin('a:2:i') #Analog pin 2
d9 = board.get_pin('d:9:p') #Digital pin 9 (PWM)

MaxStep = 255
TimeStep = 0.015
MaxTime = TimeStep*MaxStep*10
StepsList = list(range(0,MaxStep))
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

for x in StepsList:
  
  d9.write(x/MaxStep) #Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
  time.sleep(TimeStep)
  Pin0Value = a0.read() #Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
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

plt.show()  
board.exit()
#data = pd.DataFrame(list(zip(Times,Currents,Voltages)),columns=['time','current','voltage'])
#data.to_csv('JUAMI_lsvouput.csv')