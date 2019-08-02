from pyfirmata import Arduino, util
from matplotlib import pyplot as plt
import time
import serial.tools.list_ports


def startup_routine():

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
      board = Arduino(com, baudrate = 115200)  # opens communication to Arduino
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
    
    it = util.Iterator(board)
    it.start()

    #Setup Arduino pins
    a0 = board.get_pin('a:0:i') #Analog pin 0 
    a2 = board.get_pin('a:2:i') #Analog pin 2
    d9 = board.get_pin('d:9:p') #Digital pin 9 (PWM)
    
    return com, board, a0, a2, d9

def closing_routine(board, d9):
    
    #Prompt
    print('Experiment Complete')
    
    #Show Final Data
    plt.show()  
    
    #Reset PWM
    d9.write(0)
    
    #Close Connection
    board.exit()

