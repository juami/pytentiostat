# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:03:52 2019

@author: austin
"""

from pyfirmata import Arduino, util
from matplotlib import pyplot as plt
import time
import Plotter as plotter
import Reporter as reporter

    
board = Arduino("COM3", baudrate = 115200)
it = util.Iterator(board)
it.start()

#Setup Arduino pins
a0 = board.get_pin('a:0:i') #Analog pin 0 
a2 = board.get_pin('a:2:i') #Analog pin 2
d9 = board.get_pin('d:9:p') #Digital pin 9 (PWM)

MaxStep = 255
TimeStep = 0.03
MaxTime = TimeStep*MaxStep*10
StepsList = list(range(0,MaxStep))
StartTime = time.time()
Exp_Type = 'LSV'
Times = []
Voltages = []
Currents = []

#Starting up the plot
line = plotter.PlotInitializer(Exp_Type)

for x in StepsList:
  
  d9.write(x/256) #Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
  time.sleep(TimeStep)
  Pin0Value = a0.read() #Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
  Pin2Value = a2.read()
  NowTime = time.time()
  TimePassed = NowTime-StartTime
  Times.append(TimePassed)
  real_voltage = (Pin0Value-0.5)*-1*4.446
  real_current = ((Pin2Value-0.5)*-1*4.446)/0.216
  Voltages.append(real_voltage)
  Currents.append(real_current)
  Times.append(TimePassed)
  zippy = zip(Times, Voltages, Currents)
  plotter.PlotUpdater(Exp_Type, zippy, line)

zippy = zip(Times, Voltages, Currents)
reporter.exporter(zippy)

plt.show()  
board.exit()
#data = pd.DataFrame(list(zip(Times,Currents,Voltages)),columns=['time','current','voltage'])
#data.to_csv('C:/Users/Jeremy/Desktop/JUAMI_lsvouput.csv')