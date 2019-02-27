#!/usr/bin/python

from pyfirmata import Arduino, util
from time import sleep
from pyfirmata import INPUT, OUTPUT, PWM
import serial
import re


# Setting up Arduino board
port = '/dev/tty.usbmodem14201' # if having error of: Can't open port, two reasons: 1. wrong port name. 2.Don't have permison
# Go to Terminal type: sudo chmod 777 tty.usbmodem14201 (Use administrator status to change mode)


board = Arduino(port)

sleep(0.02) # The synchronization between the Arduino board and pyFirmata requires some time. 1 = 1 second


board.digital[9].mode = OUTPUT # Same as pinMode(digitalpin9, OUTPUT)
# Alternative: analog_d9p = board.get_pin('d:9:p')
board.analog[0].mode = INPUT # voltage
board.analog[2].mode = INPUT # current

board.digital[9].frequency = 31372.25
# board.digital[9].mode = PWM


it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
board.analog[2].enable_reporting()


arduino = serial.Serial('/dev/tty.usbmodem14201', 9600) #To find USB devices, go to terminal, type in cd dev, then ls

# listen for the input, exit if nothing received in timeout period
def readPin():
    words = []
    nums = []
    while True:
        line = arduino.readline()
        if len(line) != 0:
            words = re.findall(r'-?\d+.\d\d\d\d', line)
            nums = [float(w) for w in words]
            print nums
            return nums




# Port output testing-------------------------------------------
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




val0 = 0
Voltage = 0
Current = 0
val0V = 0
val2V = 0
val2 = 0.0
val9 = 0
invi = 0

for i in range(0,255):
    board.digital[9].write(i)  # 100 % duty cycle (2.5V analog value)
    for j in range(1,9):
        nums = readPin()
        val0 = val0 + nums[0]#board.analog[0].read()
        val2 = val2 + nums[1]#board.analog[2].read()
        sleep(0.005)

val0 = val0/9
val2 = val2/9
val0 = 511 - val0
val2 = -1.0 * (511 - val2)
val0V = val0 * 5.0
val2V = val2 * 5.0
Current = val2V * 1000.0/(1024.0 * 0.216) # Current from working electrode in uA set by resistor
Voltage = val0V * 1000.0/1024             # Voltage from reference electrode in mV

print Current
print Voltage
