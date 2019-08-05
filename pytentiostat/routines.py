import time
import sys

from pyfirmata import Arduino, util
import matplotlib.pyplot as plt
import serial.tools.list_ports


def _load_arduino():
    print('Searching for potentiostat...')
    ports = list(serial.tools.list_ports.comports())
    n_arduinos = 0
    for p in ports:  # Checking for Arduino Unos connected
        if 'Arduino Uno' in p.description:
            com = p.device
            n_arduinos += 1

    if n_arduinos > 1:
        sys.exit('More than one Arduino Uno found. Exiting...')

    if n_arduinos == 0:
        sys.exit('No JUAMI potentiostat found. Exiting...')

    return com


def startup_routine():
    print('Welcome to the JUAMI pytentiostat interface!')

    com = _load_arduino()
    try:
        board = Arduino(com, baudrate=115200)  # opens communication to Arduino
        print(
            'Potentiostat connected {}. Reading configuration file...'.format(com))
    except:
        print('Error. Could not open COM port')
        time.sleep(5)
        sys.exit('Could not read config file. Exiting...')
    try:
        time.sleep(0)  # Place holder until config file is finished
        # config = yaml.safe_load(file)
    except:
        sys.exit('Could not read config file. Exiting...')

    print('Configuration file loaded successfully. Beginning experiment...')

    it = util.Iterator(board)
    it.start()

    # Setup Arduino pins
    a0 = board.get_pin('a:0:i')  # Analog pin 0
    a2 = board.get_pin('a:2:i')  # Analog pin 2
    d9 = board.get_pin('d:9:p')  # Digital pin 9 (PWM)

    return com, board, a0, a2, d9


def closing_routine(board, d9):
    # Prompt
    print('Experiment Complete!')

    # Show Final Data
    plt.show()

    # Reset PWM
    d9.write(0)

    # Close Connection
    board.exit()


if __name__ == "__main__":
    startup_routine()
