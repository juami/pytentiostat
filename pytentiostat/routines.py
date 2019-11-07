import sys

from pyfirmata import Arduino, util
import matplotlib.pyplot as plt
import serial.tools.list_ports

_BAUD_RATE = 115200


def _load_arduino():
    """
    Creates a list of all the active serial ports and then checks how many arduino unos are connected
    If only one is found, it's COM port is returned. If any other number is found, the corresponding
    error message is printed and the program exits.

    Returns
    -------
    com: string
        the COM port the arduino is connected to.
    """
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
    """
    Creates board object with Arduino(). If the connection fails it prints an error message and exits.
    Parameters
    ----------
    com: string
        the COM port that the potentiostat is connected to.

    Returns
    -------
    nothing
    """
    try:
        board = Arduino(com,
                        baudrate=_BAUD_RATE)  # opens communication to Arduino
        print("Pytentiostat connected to {}.\n".format(
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
    """
    Called after experiment is finished. Function brings the potential back to 0 V and closes the board object.

    Parameters
    ----------
    board: board object for communication
    d9: pin object for digital pin 9

    Returns
    -------
    nothing
    """
    # Prompt
    print("Experiment Complete! Closing...")

    # Reset PWM

    d9.write(0.5)

    # Close Connection
    board.exit()

    # Show Final Data
    plt.show()
