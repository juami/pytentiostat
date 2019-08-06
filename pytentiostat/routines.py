import time
import sys

from pyfirmata import Arduino, util
import matplotlib.pyplot as plt
import serial.tools.list_ports

_BAUD_RATE = 115200

def _load_arduino():
    print("Searching for potentiostat...")
    ports = list(serial.tools.list_ports.comports())
    n_arduinos = 0
    for p in ports:  # Checking for Arduino Unos connected
        if "Arduino Uno" == p.description:
            com = p.device
            n_arduinos += 1
    if n_arduinos > 1:
        sys.exit("More than one Arduino Uno found. Exiting...")
    if n_arduinos == 0:
        sys.exit("No JUAMI potentiostat found. Exiting...")
    return com


def _initialize_arduino(com):
    try:
        board = Arduino(com, baudrate=_BAUD_RATE)  # opens communication to Arduino
        print("Pytentiostat connected {}. Reading configuration file...".format(com))
    except:
        sys.exit("Error. Could not open COM port")
    return board


def startup_routine():
    '''
    Initializes the communication port with the JUAMI potentistat

    The funtion does this that and the other and exits if it isn't happy and
    dings some pins and so on.

    Returns
    -------
    bunch of things.
    com : string
      the name of the port with the potentiostat on it

    '''

    print("Welcome to the JUAMI pytentiostat interface!")
    com = _load_arduino()
    board = _initialize_arduino(com)
    try:
        # FIXME Place holder until config file is finished
        time.sleep(0)
        # config = yaml.safe_load(file)
    except:
        sys.exit("Could not read config file. Exiting...")

    print("Configuration file loaded successfully. Beginning experiment...")

    it = util.Iterator(board)
    it.start()

    # Setup Arduino pins
    a0 = board.get_pin("a:0:i")  # Analog pin 0
    a2 = board.get_pin("a:2:i")  # Analog pin 2
    d9 = board.get_pin("d:9:p")  # Digital pin 9 (PWM)

    return com, board, a0, a2, d9


def closing_routine(board, d9):
    # Prompt
    print("Experiment Complete!")

    # Show Final Data
    plt.show()

    # Reset PWM
    d9.write(0)

    # Close Connection
    board.exit()


if __name__ == "__main__":
    startup_routine()
