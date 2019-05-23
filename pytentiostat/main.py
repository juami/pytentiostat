#This file is where all the fuctions are defined
#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import time
import serial
import re
import json

from time import sleep
from matplotlib import pyplot as plt
from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM

# Declearing golbal variables
analogpin0 = 0
analogpin2 = 2
PWM9 = 'd:9:p'
PWMfrequency = 31372.25

class ProgramSetup(object):
    def __init__(self,portname = '/dev/tty.usbmodem14201'):
        self.port = portname

    def setup_arduino(self):
        self.board = Arduino(self.port)
        self.arduino = serial.Serial(self.port, 9600)
        sleep(0.02)  # The synchronization between the Arduino board and pyFirmata requires some time. 1 = 1 second
        self.analog_d9p = self.board.get_pin(PWM9)  # Same as board.digital[9].mode = PWM
        self.board.analog[analogpin0].mode = INPUT  # voltage
        self.board.analog[analogpin2].mode = INPUT  # current
        self.analog_d9p.frequency = PWMfrequency
        self.it = util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()
        self.board.analog[2].enable_reporting()

    def readPin(self):
        words = []
        nums = []
        while True:
            line = None
            while line is None:
                try:
                    line = self.arduino.readline()
                except:
                    pass
            if len(line) != 0:
                words = re.findall(r'-?\d+.\d\d\d\d', line.decode('utf-8'))
                nums = [float(w) for w in words]
                print(nums)
                if (len(nums) == 2):
                    return nums


    def DataProcess(self,x,*argv):
        ax = []   # Define X value for Real Time
        ay1 = []  # Define y value for Current
        ay2 = []  # Define y value for Voltage
        CurrentArray = []
        VoltageArray = []
        plt.ion()  # Open a plotting window
        start = time.time()
        lastHigh = time.time()
        for i in range(0, int(x)):
            last = time.time()
            self.analog_d9p.write(i / 255)  # 100 % duty cycle (2.5V analog value)
            val0 = 0 # Initialize input from pin that will read Voltage as integer
            val2 = 0 # Initialize input from pin that will read Current as integer
            nums = self.readPin()
            val2 = nums[1]
            val0 = nums[0]
            CurrentArray.append(val2)
            VoltageArray.append(val0)
            time.sleep(0.001)
            end = time.time()  # clock for the real time plotting
            xl = end - start
            ax.append(round(xl,4))  # real time on x-axis
            ay1.append(round(val2,4))  # assign Current with respect to xl
            ay2.append(round(val0,4))  # assign Voltage with respect to xl
            if argv[0] == 'plot':
                plt.clf()  # clear previous plots
                plt.xlim(xl - 40, xl + 40)  # Set up x range
                plt.ylim(-2500, 2500)  # Set up y range
                plt.plot(ax, ay1, color='blue')
                plt.plot(ax, ay2, color='red')
                plt.xlabel('Time')  # name x-axis
                plt.ylabel('Current/Voltage')  # name y-axis
                plt.pause(0.00001)  # pause for 0.01 second
        plt.show()
        plt.savefig('testloop1.png')  # Save the poltting as a picture
        timeArray = numpy.asarray(ax)
        CurrentArray = numpy.asarray(ay1)
        VoltageArray = numpy.asarray(ay2)
        if argv[1] == 'write':
            numpy.savetxt('dataset.csv', numpy.column_stack((timeArray, CurrentArray, VoltageArray)))
        return timeArray, CurrentArray, VoltageArray
