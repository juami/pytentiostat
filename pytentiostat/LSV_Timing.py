# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:03:52 2019

@author: austin
"""

from pyfirmata import Arduino, util
import time
import pandas as pd

StartTime = time.time()    
    
board = Arduino("COM3", baudrate = 57600)
it = util.Iterator(board)
it.start()

#Setup Arduino pins
a0 = board.get_pin('a:0:i') #Analog pin 0 
a2 = board.get_pin('a:2:i') #Analog pin 2
d9 = board.get_pin('d:9:p') #Digital pin 9 (PWM)

MaxStep = 200
TimeStep = 0.02
StepsList = list(range(50,MaxStep))
StartTime = time.time()

dwrites = []
Voltages = []
Currents = []
AvgNum = 1

for x in StepsList:
  
  dval = x/(MaxStep+55)
  i = 0
  Pins=0
  
  while i < AvgNum:
      time.sleep(TimeStep)
      d9.write(dval) #Writes Value Between 0 and 1 (-2.5V to 2.5V) 256 possible
      time.sleep(TimeStep)
      Pin0Value = a0.read() #Reads Value Between 0 and 1 (-2.5V to 2.5V) 1024 possible
      Pins = Pins + Pin0Value
      i=i+1
      
  dwrites.append(dval)
  PinAvg=Pins/AvgNum
  Voltages.append(PinAvg)

Vdata = list(zip(dwrites, Voltages))
Vdf = pd.DataFrame(data = Vdata, columns = ['Relative PWM Wrote', 'Relative Voltage Read'])
Vdf.to_csv("Testing LSV.csv",index=False,header=True)

board.exit()