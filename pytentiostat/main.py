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

#------------- The setup_arduino function from PyFirmata might not be working --------------
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
# --------------------------------------------------------------------------------------------

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


    def LSV(self,minV,maxV,*argv):
        ax = []   # Define X value for Real Time
        ay1 = []  # Define y value for Current
        ay2 = []  # Define y value for Voltage
        CurrentList = []
        VoltageList = []
        plt.ion()  # Open a plotting window
        start = time.time()
        lastHigh = time.time()
        PWM_max = int((maxV + 2.5) * 256 / 5)
        PWM_min = int((minV + 2.5) * 256 / 5)
        plotFlag = argv[0]

        for i in range(128, PWM_max): # Voltage starts from 0V to 2.5V (PWM from 128 to 256)
            last = time.time()
            self.analog_d9p.write(i / 256)
            self.add_plot( CurrentList, VoltageList, ax, ay1, ay2, start, plotFlag)

        while(True): # Voltage from -2.5V to 2.5V (PWM from 0 t0 256), and repeat infinitely
            for i in range(PWM_min, PWM_max):
                last = time.time()
                self.analog_d9p.write(i / 256)
                self.add_plot( CurrentList, VoltageList, ax, ay1, ay2, start, plotFlag)
            plt.show()
            plt.savefig('Linear_Sweep_Voltammetry.png')  # Save the plotting as a picture
            timeArray = numpy.asarray(ax)
            CurrentArray = numpy.asarray(ay1)
            VoltageArray = numpy.asarray(ay2)
            if argv[1]: # if write commend is true, save the data file; if false, do not save
                numpy.savetxt('LSV_dataset.csv', numpy.column_stack((timeArray, CurrentArray, VoltageArray)))
        return timeArray, CurrentArray, VoltageArray


    def CV(self,minV,maxV,*argv):
        ax = []   # Define X value for Real Time
        ay1 = []  # Define y value for Current
        ay2 = []  # Define y value for Voltage
        CurrentList = []
        VoltageList = []
        plt.ion()  # Open a plotting window
        start = time.time()
        lastHigh = time.time()
        plotFlag = argv[0]
        PWM_max = int((maxV + 2.5) * 256 / 5)
        PWM_min = int((minV + 2.5) * 256 / 5)
        print("loop1 starts running")
        while (True):
            for i in range(128,PWM_max): # Voltage starts from 0V to 2.5V (PWM from 128 to 256)
                print("loop1 is running")
                last = time.time()
                self.analog_d9p.write(i / 256)
                self.add_plot(CurrentList, VoltageList, ax, ay1, ay2, start, plotFlag)
            print("loop2 starts running")
            for i in range(PWM_max,PWM_min,-1): # Voltage from 2.5V to -2.5V (PWM from 256 to 0)
                print("loop2 is running")
                last = time.time()
                self.analog_d9p.write(i / 256)
                self.add_plot(CurrentList, VoltageList, ax, ay1, ay2, start, plotFlag)
            print("loop3 starts running")
            for i in range(PWM_min,128): # Voltage from -2.5V to 0V (PWM from 0 to 128)
                print("loop3 is running")
                last = time.time()
                self.analog_d9p.write(i / 256)
                self.add_plot(CurrentList, VoltageList, ax, ay1, ay2, start, plotFlag)
            plt.show()
            plt.savefig('Cyclic_Voltammetry.png')  # Save the plotting as a picture
            timeArray = numpy.asarray(ax)
            CurrentArray = numpy.asarray(ay1)
            VoltageArray = numpy.asarray(ay2)
            if argv[1] :
                numpy.savetxt('CV_dataset.csv', numpy.column_stack((timeArray, CurrentArray, VoltageArray)))
        return timeArray, CurrentArray, VoltageArray

    def add_plot(self,CurrentArray,VoltageArray,ax,ay1,ay2,start,plotFlag):
        '''
        Read real-time data and add data to current and voltage arrays
        :param plotFlag: if plotFlag is true, show plotting; if false, do not show
        '''
        val0 = 0  # Initialize input from pin that will read Voltage as integer
        val2 = 0  # Initialize input from pin that will read Current as integer
        nums = self.readPin()
        val2 = nums[1]
        val0 = nums[0]
        CurrentArray.append(val2)
        VoltageArray.append(val0)
        time.sleep(0.001)
        end = time.time()  # clock for the real time plotting
        xl = end - start
        ax.append(round(xl, 4))  # real time on x-axis
        ay1.append(round(val2, 4))  # assign Current with respect to xl
        ay2.append(round(val0, 4))  # assign Voltage with respect to xl
        if plotFlag:
            plt.clf()  # clear previous plots
            plt.xlim(xl - 40, xl + 40)  # Set up x range
            plt.ylim(-2500, 2500)  # Set up y range
            plt.plot(ax, ay1, color='blue')
            plt.plot(ax, ay2, color='red')
            plt.xlabel('Time')  # name x-axis
            plt.ylabel('Current/Voltage')  # name y-axis
            plt.pause(0.00001)  # pause for 0.01 second