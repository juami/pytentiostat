import sys
import serial.tools.list_ports
from pyfirmata import Arduino, util
from PySide2.QtGui import QIcon
from warning_GUI import warning


_BAUD_RATE = 115200

def _load_arduino(ui):
    """
    Load all the communication ports in the mainWindow

    Parameters
    ----------
    ui: the mainwindow object.
        Instance is created in the main.py

    Returns
    -------

    ports : list, the name of all the ports
    """
    n_arduinos = 0
    ports = []
    for p in list(serial.tools.list_ports.comports()):  # Checking for Arduino Unos connected
#        if "Arduino Uno" in p.description:
        ports.append(p.device)
        n_arduinos += 1

    for port in ports:
        ui.arduino_connection_name.addItem(port)

    return ports


def _initialize_arduino(com):
    try:
        board = Arduino(com,baudrate=_BAUD_RATE)  # opens communication to Arduino
    except:
        sys.exit("Error. Could not open COM port")
    return board


def startup_routine(ui):
    """
    Initializes the communication port with the JUAMI potentistat

    Parameters
    ----------
    ui: the mainwindow object.
        Instance is created in the main.py

    Returns
    -------
    Map of hardware

    com : string, the name of the port with the potentiostat on it

    board : serial communication for board

    a0 : location of analog read pin 0

    a2 : location of analog read pin 2

    d9 : location of digital pwm pin 9

    """
    com = ui.arduino_connection_name.currentText()
    curr_ports = []
    for p in list(serial.tools.list_ports.comports()):  # Checking if com still connected
        curr_ports.append(p.device)
    if com :
        if com in curr_ports:
            board = _initialize_arduino(com)
            it = util.Iterator(board)
            it.start()

            # Setup Arduino pins
            a0 = board.get_pin("a:0:i")
            a2 = board.get_pin("a:2:i")
            d9 = board.get_pin("d:9:p")
            return com, board, a0, a2, d9
        else:
            warning('Current port not connected!')
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

    com, board, a0, a2, d9 = startup_routine(ui)
    board_objects = (board, a0, a2, d9)
    icon_true = QIcon("../pics/icon_connected.ico")
    if com and board:
        ui.arduino_connection_indicator.setIcon(icon_true)
    if not com:
        warning('Please connect potentiostat!')
    return com, board_objects

def disconnect_port_main(ui,board,d9):
    closing_routine(board,d9)
    icon_false = QIcon("../pics/icon_disconnected.ico")
    ui.arduino_connection_indicator.setIcon(icon_false)













