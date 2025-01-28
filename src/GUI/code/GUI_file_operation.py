## Standard libraries
from functools import partial

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidgetItem

# GUI_function
from src.GUI.code.GUI_CA_exp_creator import CA_main, CA_window_writer
from src.GUI.code.GUI_config_reader import parse_config_file
from src.GUI.code.GUI_CV_exp_creator import CV_main, CV_window_writer
from src.GUI.code.GUI_LSV_exp_creator import LSV_main, LSV_window_writer

## Local libraries
# GUI window
from src.GUI.code.warning_GUI import warning


def add_exp(ui):
    """Initializes the 'Experiment Type' window and connect buttons to
    CA,CV,LSV windows.

    Parameters
    ------
    ui: the Ui_mainwindow object
        Instance is created in the main.py
    """
    exp = ui.show_exp()
    exp.ca_button.clicked.connect(partial(CA_main, ui))
    exp.cv_button.clicked.connect(partial(CV_main, ui))
    exp.lsv_button.clicked.connect(partial(LSV_main, ui))


def load_file(ui):
    """Initializes the 'Load config file' window. Once loaded, the filename
    will show up in the experiment queue window.

    Parameters
    ------
    ui: the Ui_mainwindow object
        Instance is created in the main.py
    """
    filename = ui.load_config()  # ui.load_config() returns config file name
    if filename:
        filename_parse = filename.split("/")[-1].strip()
        item = QListWidgetItem()
        icon = None
        if "CA" in filename:
            icon = QIcon("../pics/icon_ca.ico")
        elif "CV" in filename:
            icon = QIcon("../pics/icon_cv.ico")
        elif "LSV" in filename:
            icon = QIcon("../pics/icon_lsv.ico")
        if icon:
            item.setData(1, icon)
        item.setData(2, filename_parse)
        item.setData(3, filename)
        ui.experiment_queue.addItem(item)


def edit_file(ui):
    """Initializes the 'Edit config file' window.

    Parameters
    ------
    ui: the Ui_mainwindow object
        Instance is created in the main.py
    """

    if ui.experiment_queue.currentItem():
        filename = ui.experiment_queue.currentItem().data(3)
        config_data = parse_config_file(filename)
    else:
        warning(
            "Do you want to edit a existing config file? If so, please load it!"
        )
        return

    exp = None
    if "CA" in filename:
        exp = CA_main(ui, config_data)
        CA_window_writer(exp, config_data)
    elif "CV" in filename:
        exp = CV_main(ui, config_data)
        CV_window_writer(exp, config_data)
    elif "LSV" in filename:
        exp = LSV_main(ui, config_data)
        LSV_window_writer(exp, config_data)
    if exp is None:
        warning("Please rename the file with experiment type: CA/CV/LSV!")

    ui.experiment_queue.clearSelection()


def remove_file(ui):
    """Remove the highlighted config file.

    Parameters
    ------
    ui: the Ui_mainwindow object
    Instance is created in the main.py
    """
    items = ui.experiment_queue.selectedItems()
    for item in items:
        ui.experiment_queue.takeItem(ui.experiment_queue.row(item))
