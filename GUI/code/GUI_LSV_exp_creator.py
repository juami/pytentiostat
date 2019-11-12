import yaml,os,datetime
import numpy as np
from functools import partial
from PyQt5.QtWidgets import QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from warning_GUI import warning

## PartI: load output filepath
def load_folder(LSV):
    """
    This function is connect with'Output Filepath' to load the folder window for the LSV config file to be saved.

    Parameters
    ------
    LSV: the Ui_LSV object

    """
    LSV.experiment_file_path.setText(LSV.load_folder_name())  # CA.load_folder_name() returns folder path name

## PartII: Save AP parameters
def get_AP_parameters(exp):
    """
     This function is connect with'Advanced Parameter' button.

     Parameters
     ------
     exp: the Ui_Experiment object

     Return
     ------
     AP_parameters: list contains all the advanced parameters

     """
    conv_fact = float(exp.experiment_conversion_factor.text())
    set_gain = float(exp.experiment_setpoint_gain.text())
    set_offset = float(exp.experiment_setpoint_offset.text())
    sr = float(exp.experiment_shunt_resistor.text())
    ts = float(exp.experiment_time_step.text())
    avg_num = int(exp.experiment_averag_number.text())
    AP_parameters = [conv_fact, set_gain, set_offset, sr, ts,avg_num]
    return AP_parameters

def load_APwindow(LSV,AP_params):
    """
    This function is connected to 'Advanced Parameters' button to load the advanced parameters window.

    Parameters
    ------
    LSV: the Ui_LSV object
    AP_parameters: list contains all the advanced parameters

    """
    AP,AP_window = LSV.AP_window()
    def change_params():
        """
        This function is connected to 'Save' button to save changed parameters.

        """
        AP_params[0:7] = get_AP_parameters(AP)
        if warning('The file has been saved. Do you want to exit the window?'):
            AP_window.close()
    AP.save_experiment_file_button.clicked.connect(change_params)


## PartIII Preview
def time_converter(time):
    """
    This function is to convert time to hour:minute:second.

    Parameters
    ------
    time: integer, time in seconds

    """
    if time> 0:
        time = time
    else:
        time = 0
    return str(datetime.timedelta(seconds=round(time,0)))

def plot(x,y):
    """
    This function is to plot the preview.

    Parameters
    ------
    x:list
    y:list

    Return
    ------
    canvas: the 'matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg' object

    """
    fig = Figure(figsize=(10, 7.5))
    fig.set_facecolor((1,1,1))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111,position=[0.2, 0.18, 0.76, 0.79])
    ax.clear()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.plot(x, y,'ro')
    ax.set_facecolor((1,1,1))
    return canvas

def preview_LSV(exp,grid):
    """
    This function is to show the preview and the experiment type.

    Parameters
    ------
    exp: the Ui_experiment object
    grid: QGridLayout object

    """
    stp_num = int(exp.experiment_step_number.text())
    lsv_sv = float(exp.experiment_start_voltage.text())
    lsv_ev = float(exp.experiment_end_voltage.text())
    lsv_sr = float(exp.experiment_sweep_rate.text())
    voltage_range = abs(lsv_ev - lsv_sv)  # V
    time_for_range = voltage_range / (lsv_sr / 1000)  # s
    steps_list = np.linspace(lsv_sv, lsv_ev, num=stp_num + 1)
    times_step_list = np.linspace(0, time_for_range, num=stp_num + 1)
    while grid.count() > 0:
        item = grid.takeAt(0)
        w = item.widget()
        if w:
            w.deleteLater()
    grid.addWidget(plot(times_step_list, steps_list))
    exp.experiment_duration.setText(time_converter((times_step_list[-1])))

## PartIV Save config file
def save_file(config_path_name,config_data,line_skipper):
    """
    This function is to save the input parameters as a yml file in the defined path.

    Parameters
    ------
    config_path_name: string which represents the path file
    config_data: dictionary which contains the input experiment parameters
    line_skipper:int, a specified line number

    """
    with open(config_path_name, "w") as yaml_file:
        yaml.dump(config_data, yaml_file, default_flow_style=False, sort_keys=False)

    f = open(config_path_name, "r")
    contents = f.readlines()
    f.close()

    contents.insert(0, '#General parameters to edit for an experiment \n')
    contents.insert(20 - line_skipper, '\n')
    contents.insert(21 - line_skipper, '#Only advanced users should edit advanced parameters \n')

    f = open(config_path_name, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def config_writer_LSV(exp_type, rt, stp_num, data_out_name, data_out_path,conv_fact, set_gain, set_offset, sr, ts, avg_num,
                      lsv_sv, lsv_ev, lsv_sr,):

    config_path_name = os.path.join(data_out_path, data_out_name + "_" + exp_type + "_config.yml")

    line_skipper = 9

    config_data = {'general_parameters': {'experiment_type': exp_type,
                                          'rest_time': rt,
                                          'step_number': stp_num,
                                          'data_output_filename': data_out_name,
                                          'data_output_path': data_out_path},
                   'linear_sweep_voltammetry': {'start_voltage': lsv_sv,
                                                'end_voltage': lsv_ev,
                                                'sweep_rate': lsv_sr},
                   'advanced_parameters': {'conversion_factor': conv_fact,
                                           'setpoint_gain': set_gain,
                                           'setpoint_offset': set_offset,
                                           'shunt_resistor': sr,
                                           'time_step': ts,
                                           'average_number': avg_num}}

    save_file(config_path_name,config_data,line_skipper)

def check(x):
    """
    This function is to check if input x is a valid number

    Parameters
    ------
    x : string

    Return
    ------
    boolean: True if x is a valid number, else False

    """
    if '-' in x:
        x = x.lstrip('-')
    if '.' in x:
        x = x.replace('.','0',1)
    return x.isnumeric()

def get_parameters(exp,exp_type,AP_parameters):
    """
    This function is to get all the parameters from the window

    Parameters
    ------
    exp : the Ui_Experiment object

    exp_type: string, experiment type

    AP_parameters: list that contains the advanced parameters

    Return
    ------
    config_params: list that contain all the experiment parameters

    """
    data_out_name = exp.experiment_file_name.text()
    data_out_path = exp.experiment_file_path.text()
    rt = exp.experiment_rest_time.text()
    stp_num = exp.experiment_step_number.text()
    if check(stp_num) and check(rt):
        move_on = True
        stp_num = int(stp_num)
        rt = int(rt)
    else:
        move_on = False
        warning('Please input all the parameters with the correct data type.')

    config_params = [exp_type, rt, stp_num, data_out_name, data_out_path] + AP_parameters

    lsv_sv = exp.experiment_start_voltage.text()
    lsv_ev = exp.experiment_end_voltage.text()
    lsv_sr = exp.experiment_sweep_rate.text()
    if check(lsv_sv) and check(lsv_ev) and check(lsv_sr):
        lsv_sv = float(lsv_sv)
        lsv_ev = float(lsv_ev)
        lsv_sr = float(lsv_sr)
    elif move_on:
        warning('Please make sure all the experiment parameters are either integer or float.')
    data = [lsv_sv, lsv_ev, lsv_sr]
    config_params += data

    return config_params

def write_to_file_LSV(LSV,LSV_window,AP_params):
    """
    This function is connect to save file button.

    Parameters
    ------
    LSV : the Ui_LSV object

    LSV_window: the LSV QMainWindow object

    AP_parameters: list that contains the advanced parameters

    """
    config_params = get_parameters(LSV, 'LSV', AP_params)
    config_writer_LSV(*config_params)
    if warning('The file has been saved. Do you want to exit the window?'):
        LSV_window.close()

def LSV_window_writer(exp,config_data):
    """
    This function is connect to Edit_file function in the GUI_file_operation.

    Parameters
    ------
    exp : the Ui_Experiment object

    config_data: dictionary which contains the input experiment parameters

    """
    exp_type = config_data["general_parameters"]["experiment_type"]
    data_out_name = config_data["general_parameters"]["data_output_filename"]
    data_out_path = config_data["general_parameters"]["data_output_path"]
    rest_time = config_data["general_parameters"]["rest_time"]
    step_number = config_data["general_parameters"]["step_number"]

    exp.experiment_file_name.setText(str(data_out_name))
    exp.experiment_file_path.setText(str(data_out_path))
    exp.experiment_rest_time.setText(str(rest_time))
    exp.experiment_step_number.setText(str(step_number))

    exp.experiment_start_voltage.setText(str(config_data["linear_sweep_voltammetry"]["start_voltage"]))
    exp.experiment_end_voltage.setText(str(config_data["linear_sweep_voltammetry"]["end_voltage"]))
    exp.experiment_sweep_rate.setText(str(config_data["linear_sweep_voltammetry"]["sweep_rate"]))

## PartV: Main
def LSV_main(ui):
    """
    This function is connect to 'CA' button in the Experiment Type window

    Parameters
    ------
    ui : the Ui_Mainwindow object

    Return
    ------
    CA: the Ui_ca object

    """

    LSV,LSV_window = ui.show_LSVwindow()
    grid = QGridLayout()
    LSV.plot_area.setLayout(grid)
    AP_params = [4.798, 1.03, 0, 0.202, 0.003, 9]

    LSV.select_output_filepath_button.clicked.connect(partial(load_folder,LSV))
    LSV.advanced_parameters_button.clicked.connect(partial(load_APwindow,LSV,AP_params))
    LSV.generate_preview_button.clicked.connect(partial(preview_LSV, LSV, grid))
    LSV.save_experiment_file_button.clicked.connect(partial(write_to_file_LSV,LSV,LSV_window,AP_params))
    return LSV
