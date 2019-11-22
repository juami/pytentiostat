## Standard libraries
import sys
from functools import partial
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout
## Local libraries
# GUI window
from mainwindow_GUI import Ui_MainWindow
# GUI function
from GUI_routines import find_port_main,disconnect_port_main,_load_arduino
from GUI_file_operation import add_exp,load_file,edit_file,delete_file
from GUI_run_exp import run_exp_main


# load the main window
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
com = None  # initialize the parameters,if potentiostat is not connected, com, board objects will be None
board_objects=(None,None,None,None)  # board_objects = (board, a0, a2, d9)
board,d9 = board_objects[0],board_objects[3]

# 'Find Potentiostat'
def find_port():
    global com,board_objects,board,d9
    com, board_objects = find_port_main(ui)
    board, d9 = board_objects[0], board_objects[3]
_load_arduino(ui)
ui.find_potentiostat_button.clicked.connect(find_port)

def disconnect_port():
    global com,board,d9
    com = None
    disconnect_port_main(ui,board,d9)
ui.disconnect_potentiostat_button.clicked.connect(disconnect_port)

# 'Add'
ui.add_experiment_button.clicked.connect(partial(add_exp,ui))

# 'Load'
ui.load_experiment_button.clicked.connect(partial(load_file,ui))

# 'Edit'
ui.edit_experiment_button.clicked.connect((partial(edit_file,ui)))

#'Delete'
ui.delete_experiment_button.clicked.connect(partial(delete_file,ui))

#'Start/Abort Experiment'
grid = QGridLayout()   # set up the layout for live plot
ui.plot_area.setLayout(grid)
def start_exp(grid):
    run_exp_main(ui,com,board_objects,grid)
ui.start_abort_experiment_button.clicked.connect(partial(start_exp,grid))

sys.exit(app.exec_())


