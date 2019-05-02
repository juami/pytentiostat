#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
from pyfirmata import Arduino, util
import time
from time import sleep
from pyfirmata import INPUT, OUTPUT, PWM
import serial
import re
import matplotlib.pyplot as plt


# ----Setting up Arduino board--------

port = '/dev/tty.usbmodem14201'# Find proper USB port on your laptop
# if having error of: Can't open port, two reasons: 1. wrong port name. 2.Don't have permison
# Go to Terminal type: sudo chmod 777 tty.usbmodem14201 (Use administrator status to change mode)
# To find USB devices, go to terminal, type in cd dev, then ls

board = Arduino(port)
arduino = serial.Serial('/dev/tty.usbmodem14201', 9600)
sleep(0.02)  # The synchronization between the Arduino board and pyFirmata requires some time. 1 = 1 second

analog_d9p = board.get_pin('d:9:p') # Same as board.digital[9].mode = PWM
board.analog[0].mode = INPUT  # voltage
board.analog[2].mode = INPUT  # current

analog_d9p.frequency = 31372.25

it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
board.analog[2].enable_reporting()



# -------Port output testing-------------------------------------------
# len=6
# for i in range(0,len):
#     board.analog[i].mode = INPUT  # voltage
#     board.analog[i].enable_reporting()
# # board.digital[9].write(0) # 100 % duty cycle (2.5V analog value)
# # data = board.digital[9].read()
# sleep(1)
#
# while(1):
#     # board.digital[9].write(1)  # 100 % duty cycle (2.5V analog value)
#     # print sard.readline()
#     # print type(board.analog[0].read())
#     dataList = [1,2,3,4,5,6]
#     for i in range(0,len):
#         dataList[i]=board.analog[i].read()
#         # print board.analog[i].read()
#     print dataList

# -------------------------------------------------------------------






# ----Defining reading function--------
val0 = 0
Voltage = 0
Current = 0
val0V = 0
val2V = 0
val2 = 0.0
val9 = 0
invi = 0
CurrentArray = []
VoltageArray = []

# Plotting array
ax = []
ay1 = []  # Define y value for Current
ay2 = []  # Define y value for Voltage
plt.ion()  # Open a plotting window


x=input("Please Enter a number:") # x is the duty cycle of PWM, usually type in 255

mypwm = numpy.arange(0,1,0.004,dtype=float)

def readPin():
    words = []
    nums = []
    while True:
        line = arduino.readline()
        if len(line) != 0:
            words = re.findall(r'-?\d+.\d\d\d\d', line.decode('utf-8'))
            nums = [float(w) for w in words]
            print (nums)
            if(len(nums)==2):
                return nums



# --------Reading from Arduino board--------------

start = time.time()
lastHigh = time.time()
for i in range(0, int(x)):
    last = time.time()
    analog_d9p.write(i / 255)  # 100 % duty cycle (2.5V analog value)
    val0=0
    val2=0

# Average to smooth signal-------
    # for j in range(1, 9):
    #     nums = readPin()
    #     val0 = val0 + nums[0]  # board.analog[0].read()
    #     val2 = val2 + nums[1]  # board.analog[2].read()
    #     # print(val2)
    #     sleep(0.001)
    # #print('val0: '+str(val0))
    # #print('val2' +str(val2))
    # val0 = val0 / 9
    # val2 = val2 / 9
#---------------------------------

    nums = readPin()
    val2 =nums[1]
    val0 =nums[0]

    CurrentArray.append(val2)
    VoltageArray.append(val0)
    time.sleep(0.001)

#Calculations to get real currents and voltages-------------
    # val0 = 511 - val0
    # val2 = -1.0 * (511 - val2)
    # val0V = val0 * 5.0
    # val2V = val2 * 5.0
    # Current = val2V * 1000.0 / (1024.0 * 0.216)  # Current from working electrode in uA set by resistor
    # Voltage = val0V * 1000.0 / 1024  # Voltage from reference electrode in mV
    #
    # CurrentArray.append(Current)
    # VoltageArray.append(Voltage)
    # print('current'+str(Current))
    # print('voltage' + str(Voltage))

#------------------------------------------------------
    end = time.time()#clock for the real time plotting
    xl = end - start

#--------Plotting--------------
    ax.append(xl)  # real time on x-axis
    ay1.append(val2)  # assign Current with respect to xl
    ay2.append(val0)  # assign Current with respect to xl
    plt.clf()                  # clear previous plots

    plt.xlim(xl-40,xl+40)# Set up x range
    plt.ylim(-2500,2500)# Set up y range

    plt.plot(ax,ay1,color='blue')
    plt.plot(ax,ay2,color='red')

    plt.xlabel('Time') # name x-axis
    plt.ylabel('Current/Voltage') # name y-axis

    plt.pause(0.00001)  # pause for 0.01 second
    plt.savefig('./testloop1.png')# Save the poltting as a picture
    plt.show()


plt.pause(10)
