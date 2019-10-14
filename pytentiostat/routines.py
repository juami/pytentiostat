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
        if "Arduino Uno" in p.description:
            com = p.device
            n_arduinos += 1
    if n_arduinos > 1:
        sys.exit("More than one Arduino Uno found. Exiting...")
    if n_arduinos == 0:
        sys.exit("No JUAMI potentiostat found. Exiting...")
    return com


def _initialize_arduino(com):
    try:
        board = Arduino(com,
                        baudrate=_BAUD_RATE)  # opens communication to Arduino
        print("Pytentiostat connected {}. Reading configuration file...".format(
            com))
    except:
        sys.exit("Error. Could not open COM port")
    return board


def startup_routine():
    """
    Initializes the communication port with the JUAMI potentistat

    Returns
    -------
    Map of hardware
    com : string
      the name of the port with the potentiostat on it
    board : serial communication for board
    a0 : location of analog read pin 0
    a2 : location of analog read pin 2
    d9 : location of digital pwm pin 9

    """

    print("Welcome to the JUAMI pytentiostat interface!")
    connect = input("Press enter to connect to a JUAMI potentiostat.")
    com = _load_arduino()
    board = _initialize_arduino(com)

    it = util.Iterator(board)
    it.start()

    # Setup Arduino pins
    a0 = board.get_pin("a:0:i")
    a2 = board.get_pin("a:2:i")
    d9 = board.get_pin("d:9:p")

    return com, board, a0, a2, d9


def closing_routine(board, d9):
    # Prompt
    print("Experiment Complete!")

    # Reset PWM

    d9.write(0.5)

    # Close Connection
    board.exit()

    # Show Final Data
    plt.show()


def verify_input(string):
    while True:
        if string == "":
            break
        elif string.lower() == "new":
            break
        elif string.lower() == "reconnect":
            break
        else:
            string = input("Invalid input.\n To restart the same experiment, press Enter. \n"
                           "If you want to do a different experiment, edit and save the config file then type"
                           " \"new\" and press enter\n"
                           "If you need to reconnect the poteniostat, type \"Reconnect\" \n")
    return string
