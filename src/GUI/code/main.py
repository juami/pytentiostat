# Standard libraries
import sys
from functools import partial

from app_setup import create_app
from GUI_file_operation import add_exp, edit_file, load_file, remove_file

# GUI function
from GUI_routines import _load_arduino, disconnect_port_main, find_port_main
from GUI_run_exp import run_exp_main

# Local libraries
# GUI window
from mainwindow_GUI import Ui_MainWindow
from PySide6.QtWidgets import QGridLayout, QMainWindow


class AppState:
    """Holds mutable state shared between GUI callbacks."""

    def __init__(self):
        self.com = None
        self.board_objects = (None, None, None, None)
        self.board = None
        self.d9 = None


def find_port(ui, state):
    """Find and connect to the potentiostat."""
    state.com, state.board_objects = find_port_main(ui)
    state.board, state.d9 = state.board_objects[0], state.board_objects[3]


def disconnect_port(ui, state):
    """Disconnect from the potentiostat."""
    state.com = None
    disconnect_port_main(ui, state.board, state.d9)


def start_exp(ui, state, grid_layout):
    """Start the experiment."""
    run_exp_main(ui, state.com, state.board_objects, grid_layout)


def main():
    """Entry point for the GUI application."""
    app = create_app(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    state = AppState()

    # 'Find Potentiostat'
    _load_arduino(ui)
    ui.find_potentiostat_button.clicked.connect(partial(find_port, ui, state))

    # 'Disconnect Potentiostat'
    ui.disconnect_potentiostat_button.clicked.connect(
        partial(disconnect_port, ui, state)
    )

    # 'Add'
    ui.add_experiment_button.clicked.connect(partial(add_exp, ui))

    # 'Load'
    ui.load_experiment_button.clicked.connect(partial(load_file, ui))

    # 'Edit'
    ui.edit_experiment_button.clicked.connect(partial(edit_file, ui))

    # 'Delete'
    ui.remove_experiment_button.clicked.connect(partial(remove_file, ui))

    # 'Start/Abort Experiment'
    grid = QGridLayout()  # set up the layout for live plot
    ui.plot_area.setLayout(grid)
    ui.start_abort_experiment_button.clicked.connect(
        partial(start_exp, ui, state, grid)
    )

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
