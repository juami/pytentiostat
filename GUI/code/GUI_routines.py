import sys
import serial.tools.list_ports
from pyfirmata import Arduino, util
from functools import partial
from warning_GUI import warning


_BAUD_RATE = 115200

def _load_arduino():
    ports = list(serial.tools.list_ports.comports())
    n_arduinos = 0
    for p in ports:  # Checking for Arduino Unos connected
        if "Arduino Uno" in p.description:
            com = p.device
            n_arduinos += 1
    if n_arduinos > 1:
        com = None  # More than one Arduino Uno found.

    if n_arduinos == 0:
        com = None    # No JUAMI potentiostat found.

    return com


def _initialize_arduino(com):
    try:
        board = Arduino(com,baudrate=_BAUD_RATE)  # opens communication to Arduino
    except:
        sys.exit("Error. Could not open COM port")
    return board


def startup_routine():
    """
    Initializes the communication port with the JUAMI potentistat

    Returns
    -------
    Map of hardware

    com : string, the name of the port with the potentiostat on it

    board : serial communication for board

    a0 : location of analog read pin 0

    a2 : location of analog read pin 2

    d9 : location of digital pwm pin 9

    """
    com = _load_arduino()
    if com:
        board = _initialize_arduino(com)
        it = util.Iterator(board)
        it.start()

        # Setup Arduino pins
        a0 = board.get_pin("a:0:i")
        a2 = board.get_pin("a:2:i")
        d9 = board.get_pin("d:9:p")
        return com, board, a0, a2, d9
    else:
        return com,None,None,None,None



def closing_routine(board, d9): # Disconnect Potentiostat
    # Reset PWM
    d9.write(0.5)

    # Close Connection
    board.exit()

def find_port_main(ui):
    """
    This function is connected with 'Find Potentiostat' button.

    Parameters
    ----------
    ui: the mainwindow object.
        Instance is created in the main.py

    Returns
    -------
    com : string, the name of the port with the potentiostat on it
          Instance is created in the main.py

    board_objects = (board, a0, a2, d9).
                   board : serial communication for board
                   a0 : location of analog read pin 0
                   a2 : location of analog read pin 2
                   d9 : location of digital pwm pin 9
                   Instance is created in the main.py

    """

    com, board, a0, a2, d9 = startup_routine()
    board_objects = (board, a0, a2, d9)
    if com:
        ui.arduino_connection_indicator.setChecked(True)
    if not com:
        warning('Please connect potentiostat!')
    def disconnect_port(ui):
        global com
        closing_routine(board,d9)
        ui.arduino_connection_indicator.setChecked(False)
        com = None
    ui.disconnect_potentiostat_button.clicked.connect(partial(disconnect_port,ui))
    return com,board_objects





