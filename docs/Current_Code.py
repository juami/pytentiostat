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

class myArduinoBoard(object):
    def __init__(self,portname = '/dev/tty.usbmodem14201'):
        self.port = portname

    def setup_arduino(self):
        self.board = Arduino(self.port)
        self.arduino = serial.Serial(self.port, 9600)
        sleep(0.02)  # The synchronization between the Arduino board and pyFirmata requires some time. 1 = 1 second
        self.analog_d9p = self.board.get_pin('d:9:p')  # Same as board.digital[9].mode = PWM
        self.board.analog[0].mode = INPUT  # voltage
        self.board.analog[2].mode = INPUT  # current
        self.analog_d9p.frequency = 31372.25
        self.it = util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()
        self.board.analog[2].enable_reporting()

    def readPin(self):
        words = []
        nums = []
        while True:
            line = self.arduino.readline()
            if len(line) != 0:
                words = re.findall(r'-?\d+.\d\d\d\d', line.decode('utf-8'))
                nums = [float(w) for w in words]
                print(nums)
                if (len(nums) == 2):
                    return nums

    def readData(self,x):
        # Plotting array
        ax = []
        ay1 = []  # Define y value for Current
        ay2 = []  # Define y value for Voltage
        CurrentArray = []
        VoltageArray = []
        start = time.time()
        lastHigh = time.time()
        for i in range(0, int(x)):
            last = time.time()
            self.analog_d9p.write(i / 255)  # 100 % duty cycle (2.5V analog value)
            val0 = 0 # Voltage
            val2 = 0 # Current
            nums = self.readPin()
            val2 = nums[1]
            val0 = nums[0]
            CurrentArray.append(val2)
            VoltageArray.append(val0)
            time.sleep(0.001)
            end = time.time()  # clock for the real time plotting
            xl = end - start
            # --------Plotting--------------
            ax.append(round(xl,4))  # real time on x-axis
            ay1.append(round(val2,4))  # assign Current with respect to xl
            ay2.append(round(val0,4))  # assign Voltage with respect to xl
        timeArray = numpy.asarray(ax)
        CurrentArray = numpy.asarray(ay1)
        VoltageArray = numpy.asarray(ay2)
        numpy.savetxt('dataset.csv',numpy.column_stack((timeArray,CurrentArray,VoltageArray)))
        return (ax,ay1,ay2)

    def plotData(self,x):
        # Plotting array
        ax = []
        ay1 = []  # Define y value for Current
        ay2 = []  # Define y value for Voltage
        CurrentArray = []
        VoltageArray = []
        plt.ion()  # Open a plotting window
        start = time.time()
        for i in range(0, int(x)):
            self.analog_d9p.write(i / 255)  # 100 % duty cycle (2.5V analog value)
            nums = self.readPin()
            val2 = nums[1] # Current
            val0 = nums[0] # Voltage
            CurrentArray.append(val2)
            VoltageArray.append(val0)
            time.sleep(0.001)
            end = time.time()  # clock for the real time plotting
            xl = end - start
            # --------Plotting--------------
            ax.append(xl)  # real time on x-axis
            ay1.append(val2)  # assign Current with respect to xl
            ay2.append(val0)  # assign Voltage with respect to xl
            plt.clf()  # clear previous plots

            plt.xlim(xl - 40, xl + 40)  # Set up x range
            plt.ylim(-2500, 2500)  # Set up y range

            plt.plot(ax, ay1, color='blue')
            plt.plot(ax, ay2, color='red')

            plt.xlabel('Time')  # name x-axis
            plt.ylabel('Current/Voltage')  # name y-axis

            plt.pause(0.00001)  # pause for 0.01 second
            plt.savefig('./testloop1.png')  # Save the poltting as a picture
            plt.show()
        plt.pause(10)
        return (ax,ay1,ay2)

if __name__ == '__main__':
    test = myArduinoBoard()
    test.setup_arduino()
    x = input("Please Enter a number:")  # x is the duty cycle of PWM, usually type in 255
    test.readData(x)
    test.plotData(x)
