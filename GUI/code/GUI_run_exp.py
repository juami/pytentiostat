## Standard libraries
import csv
import os

from GUI_config_reader import parse_config_file
from GUI_operator import experiment

# GUI function
from GUI_plotter import Ui_Plot

## Local libraries
# GUI window
from PySide2.QtGui import QIcon
from warning_GUI import warning


def calculate_time(filename):
    """Calculate the experiment time of the given filename.

    Parameters
    -------
    filename: string
              Instance is created in the GUI_file_operation.py - load_file function

    Returns
    -------
    t: int , calculated experiment time (unit:seconds)
    """
    config_data = parse_config_file(filename)
    if "CA" in filename:
        t = config_data["chronoamperometry"]["time"]
    elif "CV" in filename:
        c = config_data["cyclic_voltammetry"]["number_of_cycles"]
        v1 = abs(
            config_data["cyclic_voltammetry"]["start_voltage"]
            - config_data["cyclic_voltammetry"]["first_turnover_voltage"]
        )
        v2 = abs(
            config_data["cyclic_voltammetry"]["first_turnover_voltage"]
            - config_data["cyclic_voltammetry"]["second_turnover_voltage"]
        )
        v3 = abs(
            config_data["cyclic_voltammetry"]["second_turnover_voltage"]
            - config_data["cyclic_voltammetry"]["start_voltage"]
        )
        r = config_data["cyclic_voltammetry"]["sweep_rate"]
        t = c * (v1 + v2 + v3) / r * 1000
    elif "LSV" in filename:
        v1 = config_data["linear_sweep_voltammetry"]["start_voltage"]
        v2 = config_data["linear_sweep_voltammetry"]["end_voltage"]
        r = config_data["linear_sweep_voltammetry"]["sweep_rate"]
        t = abs(v1 - v2) / r * 1000
    return t


def total_time(ui):
    """Calculate the experiment time of each file in the experiment queue and
    append them to a list.

    Parameters
    -------
    ui: the Ui_Experiment object
        Instance is created in the main.py

    Returns
    -------
    time: list which contains the experiment time of each file in the experiment queue
    """
    time = []
    for index in range(ui.experiment_queue.count()):
        filename = (ui.experiment_queue.item(index)).data(3)
        t = calculate_time(filename)
        time.append(t)
    return time


def set_icon(ui):
    """Initialize all the icon state to be unchecked.

    Parameters
    -------
    ui : the Ui_Experiment object
        Instance is created in the main.py
    """
    for index in range(ui.experiment_queue.count()):
        item = ui.experiment_queue.item(index)
        filename = item.data(3)

        if "CA" in filename:
            icon = QIcon("../pics/icon_ca.ico")
        elif "CV" in filename:
            icon = QIcon("../pics/icon_cv.ico")
        elif "LSV" in filename:
            icon = QIcon("../pics/icon_lsv.ico")
        if icon:
            item.setData(1, icon)
        itemtext = filename.split("/")[-1].strip() + "__#" + str(index + 1)
        item.setData(2, itemtext)


def run_exp(ui, com, board_objects, ini_plot, grid, pr, tr):
    """Start the experiment and live plot on the mainwindow.

    Parameters
    -------
    ui : the Ui_Experiment object
        Instance is created in the main.py

    com : string, the name of the port with the potentiostat on it
          Instance is created in the main.py, and further modified in the main.py- find_port function

    board_objects = (board, a0, a2, d9)
                    board : serial communication for board
                    a0 : location of analog read pin 0
                    a2 : location of analog read pin 2
                    d9 : location of digital pwm pin 9
                    Instance is created in the main.py, and further modified in the main.py- find_port function

    ini_plot : the Ui_Plot object that initialized the live plotting
               Instance is created in the GUI_run_exp.py- run_exp_main function

    grid : QtWidgets.QGridLayout object that initialize the layout for live plot
           Instance is created in the main.py, and further modified in the main.py- start_exp function

    pr : QtWidgets.QProgressBar object , initialize the progress_bar live progress update
         Instance is created in the GUI_run_exp.py- run_exp_main function

    tr : QtWidgets.QLineEdit object, initialize the time_remaining_display for live remaining time update
         Instance is created in the GUI_run_exp.py- run_exp_main function
    """
    icon_false = QIcon("../pics/icon_off.ico")
    icon_true = QIcon("../pics/icon_on.ico")
    if not com:
        warning(
            "Please connect potentiostat!"
        )  # make sure that the user connects potentiostat before measurement
        ui.start_abort_experiment_button.setChecked(False)
        return
    elif ui.experiment_queue.count() == 0:
        warning(
            "Please load a config file! "
        )  # make sure that the config file is loaded before measurement
        ui.start_abort_experiment_button.setChecked(False)
        return
    set_icon(ui)  # Initialize the icon state to be the unchecked.
    for index in range(ui.experiment_queue.count()):
        if ui.stop_experiment_button.isChecked():
            break
        filename = (ui.experiment_queue.item(index)).data(3)
        if not filename.endswith("config.yml"):
            warning("Please load a yml config file!")
            ui.start_abort_experiment_button.setChecked(False)
            return
        icon_done = QIcon("../pics/icon_checked.ico")
        config_data = parse_config_file(filename)
        data_out_name = config_data["general_parameters"][
            "data_output_filename"
        ]
        data_out_path = config_data["general_parameters"]["data_output_path"]
        exp_type = config_data["general_parameters"]["experiment_type"]
        config_path_name = os.path.join(
            data_out_path, data_out_name + "_" + exp_type + ".csv"
        )
        exp_time_list = total_time(ui)
        total_exp_time = sum(exp_time_list)
        if index == 0:
            passed_exp_time = 0
        elif index and index < ui.experiment_queue.count():
            passed_exp_time += exp_time_list[index - 1]

        ini_plot.plot_initialize(config_data)
        grid.addWidget(ini_plot.canvas, 1, 0, 1, 1)
        grid.addWidget(ini_plot.toolbar, 0, 0, 1, 1)

        ui.experiment_status_indicator.setIcon(icon_true)

        if ui.start_abort_experiment_button.isChecked():
            try:
                times, voltages, currents = [], [], []
                time, voltage, current = experiment(
                    config_data,
                    *board_objects,
                    ini_plot,
                    times,
                    voltages,
                    currents,
                    pr,
                    tr,
                    total_exp_time,
                    passed_exp_time
                )
                try:
                    with open(config_path_name, "w", newline="") as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(["Time", "Voltage", "Current"])
                        writer.writerows(zip(time, voltage, current))
                except:
                    warning("Filepath not exist!")
            except:
                warning("Wrong port connected!")
                break

            # once an experiment is finished, set its icon to checked state.
            ui.experiment_queue.item(index).setData(1, icon_done)
        else:
            warning("Are you sure you want to quit?")

    ui.stop_experiment_button.setChecked(False)
    ui.start_abort_experiment_button.setChecked(False)
    ui.experiment_status_indicator.setIcon(icon_false)


def run_exp_main(ui, com, board_objects, grid):
    """The main function of run experiment. Initialize ini_plot,pr,tr and pass
    it to the run_exp function.

    Parameters
    -------
    ui: the Ui_Experiment object
        Instance is created in the main.py

    com : string, the name of the port with the potentiostat on it
          Instance is created in the main.py, and further modified in the main.py- find_port function

    board_objects = (board, a0, a2, d9)
                    board : serial communication for board
                    a0 : location of analog read pin 0
                    a2 : location of analog read pin 2
                    d9 : location of digital pwm pin 9
                    Instance is created in the main.py, and further modified in the main.py- find_port function

    grid : QtWidgets.QGridLayout object that initialize the layout for live plot
           Instance is created in the main.py, and further modified in the main.py- start_exp function
    """
    ini_plot = Ui_Plot()  # Initialize the measurement plot
    pr = ui.progress_bar  # Initiate the progress bar
    tr = ui.time_remaining_display  # Initiate remaining time
    run_exp(ui, com, board_objects, ini_plot, grid, pr, tr)
