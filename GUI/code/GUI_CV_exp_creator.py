import yaml,os,datetime
import numpy as np
from functools import partial
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QGridLayout, QListWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from warning_GUI import warning

# PartI: load output filepath
def load_folder(CV):
    """
    This function is connect with'Output Filepath' to load the folder window for the CV config file to be saved.

    Parameters
    ------
    CV : the Ui_CV object

    """
    CV.experiment_file_path.setText(CV.load_folder_name())  # CA.load_folder_name() returns folder path name

# PartII: Save AP parameters
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

def load_APwindow(CV,AP_params):
    """
    This function is connected to 'Advanced Parameters' button to load the advanced parameters window.

    Parameters
    ------
    CV: the Ui_CV object
    AP_parameters: list contains all the advanced parameters

    """
    AP,AP_window = CV.AP_window()
    AP.experiment_conversion_factor.setText(str(AP_params[0]))
    AP.experiment_setpoint_gain.setText(str(AP_params[1]))
    AP.experiment_setpoint_offset.setText(str(AP_params[2]))
    AP.experiment_shunt_resistor.setText(str(AP_params[3]))
    AP.experiment_time_step.setText(str(AP_params[4]))
    AP.experiment_averag_number.setText(str(AP_params[5]))

    def change_params():
        """
        This function is connected to 'Save' button to save changed parameters.

        """
        AP_params[0:7] = get_AP_parameters(AP)
        if warning('The file has been saved. Do you want to exit the window?'):
            AP_window.close()
    AP.save_experiment_file_button.clicked.connect(change_params)


# PartIII Preview
def time_converter(time):
    """
    This function is to convert time to hour:minute:second.

    Parameters
    ------
    time : integer, time in seconds

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
    x :list
    y :list

    Return
    ------
    canvas : the 'matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg' object

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

def CV_data(stp_num, cv_sv, cv_ftv, cv_stv, cv_sr):
    """
    This function is to calculate the times_step_list, steps_list for CV preview

    Parameters
    ------
    stp_num : int, step numbers
    cv_sv : float,start voltage
    cv_ftv :float,first turnover voltage
    cv_stv :float,second turnover voltage
    cv_sr : float: sweep rate

    """
    first_voltage_range = abs(cv_ftv - cv_sv)  # V
    second_voltage_range = abs(cv_stv - cv_ftv)  # V
    third_voltage_range = abs(cv_sv - cv_stv)  # V

    first_time_range = first_voltage_range / (cv_sr / 1000)  # s
    second_time_range = second_voltage_range / (cv_sr / 1000)  # s
    third_time_range = third_voltage_range / (cv_sr / 1000)  # s
    fall = (first_voltage_range + second_voltage_range + third_voltage_range)  # V

    if fall == 0:
        fall += 1
    f1 = first_voltage_range / fall
    num1 = int(f1 * stp_num)
    f2 = second_voltage_range / fall
    num2 = int(f2 * stp_num)
    num3 = stp_num - num1 - num2 + 1
    first_steps_list = np.linspace(cv_sv, cv_ftv, num=num1, endpoint=False)
    second_steps_list = np.linspace(cv_ftv, cv_stv, num=num2, endpoint=False)
    third_steps_list = np.linspace(cv_stv, cv_sv, num=num3)
    steps_list = np.concatenate((first_steps_list, second_steps_list, third_steps_list))

    first_times_steps = np.linspace(0, first_time_range, num=num1, endpoint=False)
    second_times_steps = np.linspace(first_time_range, first_time_range + second_time_range, num=num2,
                                     endpoint=False)
    third_times_steps = np.linspace(first_time_range + second_time_range,
                                    first_time_range + second_time_range + third_time_range, num=num3)
    times_step_list = np.concatenate((first_times_steps, second_times_steps, third_times_steps))

    return times_step_list, steps_list

def preview_CV(exp, grid):
    """
    This function is to show the preview and the experiment type.

    Parameters
    ------
    exp : the Ui_experiment object
    grid : QGridLayout object

    """
    stp_num = exp.experiment_step_number.text()
    cv_sv = exp.experiment_start_voltage.text()
    cv_ftv = exp.experiment_first_vertex_voltage.text()
    cv_stv = exp.experiment_second_vertex_voltage.text()
    cv_sr = exp.experiment_sweep_rate.text()
    cyc_num = exp.experiment_cycle_number.text()
    if check(stp_num) and check(cv_sv) and check(cv_ftv) and check(cv_stv) and check(cv_sr) and check(cyc_num):
        stp_num = int(stp_num)
        cv_sv = float(cv_sv)
        cv_ftv = float(cv_ftv)
        cv_stv = float(cv_stv)
        cv_sr = float(cv_sr)
        cyc_num = int(cyc_num)
    else:
        warning('Please make sure all the experiment parameters are either integer or float.')
        return
    x, y = CV_data(stp_num, cv_sv, cv_ftv, cv_stv, cv_sr)
    while grid.count() > 0:
        item = grid.takeAt(0)
        w = item.widget()
        if w:
            w.deleteLater()
    grid.addWidget(plot(x, y))
    exp.experiment_duration.setText(time_converter((x[-1] * cyc_num)))


# PartIV Save config file
def save_file(config_path_name,config_data,line_skipper):
    """
    This function is to save the input parameters as a yml file in the defined path.

    Parameters
    ------
    config_path_name : string which represents the path file
    config_data : dictionary which contains the input experiment parameters
    line_skipper :int, a specified line number

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


def config_writer_CV(exp_type, rt, stp_num, data_out_name, data_out_path,conv_fact,set_gain,set_offset,sr,ts,avg_num,
                     cv_sv, cv_ftv,cv_stv,cv_sr,cyc_num):

    config_path_name = os.path.join(data_out_path, data_out_name+"_"+exp_type+"_config.yml")

    line_skipper = 7
    config_data = {'general_parameters': {'experiment_type': exp_type,
                                          'rest_time': rt,
                                          'step_number': stp_num,
                                          'data_output_filename': data_out_name,
                                          'data_output_path': data_out_path},
                   'cyclic_voltammetry': {'start_voltage': cv_sv,
                                          'first_turnover_voltage': cv_ftv,
                                          'second_turnover_voltage': cv_stv,
                                          'sweep_rate': cv_sr,
                                          'number_of_cycles': cyc_num},
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
    boolean : True if x is a valid number, else False

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
    cv_sv = exp.experiment_start_voltage.text()
    cv_ftv = exp.experiment_first_vertex_voltage.text()
    cv_stv = exp.experiment_second_vertex_voltage.text()
    cv_sr = exp.experiment_sweep_rate.text()
    cyc_num = exp.experiment_cycle_number.text()
    if check(cv_sv) and check(cv_ftv) and check(cv_stv) and check(cv_sr) and check(cyc_num):
        cv_sv = float(cv_sv)
        cv_ftv = float(cv_ftv)
        cv_stv = float(cv_stv)
        cv_sr = float(cv_sr)
        cyc_num = int(cyc_num)
    elif move_on:
        warning('Please make sure all the experiment parameters are either integer or float.')
    data = [cv_sv, cv_ftv, cv_stv, cv_sr, cyc_num]
    config_params += data

    return config_params

def write_to_file_CV(ui,CV,CV_window,AP_params):
    """
    This function is connect to save file button.

    Parameters
    ------
    CV : the Ui_CV object

    CV_window: the CV QMainWindow object

    AP_parameters: list that contains the advanced parameters

    """
    config_params = get_parameters(CV,'CV',AP_params)
    data_out_name = config_params[3]
    data_out_path = config_params[4]
    filename_list = os.listdir(data_out_path)
    config_writer_CV(*config_params)
    filename = os.path.join(data_out_path, data_out_name + "_CV_config.yml")
    filename_parse = filename.split('/')[-1].strip()
    # list all the filename in the experiment queue, stored in queue_filename
    queue_filename = []
    for x in range(ui.experiment_queue.count()):
        queue_filename.append(ui.experiment_queue.item(x).data(2).split('.yml')[0]+'.yml')

    if filename_parse in filename_list:
        if warning('The filename exists. Do you want to overwrite it?'):
            CV_window.close()
            if filename_parse not in queue_filename:
                item = QListWidgetItem()
                icon = QIcon("../pics/icon_cv.ico")
                item.setData(1, icon)
                item.setData(2, filename_parse)
                item.setData(3, filename)
                ui.experiment_queue.addItem(item)
                return
            else:
                return
        else:
            return
    if warning('The file is saved. Do you want to exit the window?'):
        CV_window.close()
        item = QListWidgetItem()
        icon = QIcon("../pics/icon_cv.ico")
        item.setData(1, icon)
        item.setData(2, filename_parse)
        item.setData(3, filename)
        ui.experiment_queue.addItem(item)

def CV_window_writer(exp,config_data):
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

    exp.experiment_start_voltage.setText(str(config_data["cyclic_voltammetry"]["start_voltage"]))
    exp.experiment_first_vertex_voltage.setText(str(config_data["cyclic_voltammetry"]["first_turnover_voltage"]))
    exp.experiment_second_vertex_voltage.setText(str(config_data["cyclic_voltammetry"]["second_turnover_voltage"]))
    exp.experiment_sweep_rate.setText(str(config_data["cyclic_voltammetry"]["sweep_rate"]))
    exp.experiment_cycle_number.setText(str(config_data["cyclic_voltammetry"]["number_of_cycles"]))


# PartV: Main
def CV_main(ui,config_data=None):
    """
    This function is connect to 'CA' button in the Experiment Type window

    Parameters
    ------
    ui : the Ui_Mainwindow object

    Return
    ------
    CA: the Ui_ca object

    """

    CV,CV_window = ui.show_CVwindow()
    grid = QGridLayout()
    CV.plot_area.setLayout(grid)
    AP_params = [4.798,1.03,0,0.202,0.003,9]
    if config_data:
        AP_params[0] = config_data["advanced_parameters"]["conversion_factor"]
        AP_params[1] = config_data["advanced_parameters"]["setpoint_gain"]
        AP_params[2] = config_data["advanced_parameters"]["setpoint_offset"]
        AP_params[3] = config_data["advanced_parameters"]["shunt_resistor"]
        AP_params[4] = config_data["advanced_parameters"]["time_step"]
        AP_params[5] = config_data["advanced_parameters"]["average_number"]

    CV.select_output_filepath_button.clicked.connect(partial(load_folder,CV))
    CV.advanced_parameters_button.clicked.connect(partial(load_APwindow,CV,AP_params))
    CV.generate_preview_button.clicked.connect(partial(preview_CV,CV,grid))
    CV.save_experiment_file_button.clicked.connect(partial(write_to_file_CV,ui,CV,CV_window,AP_params))

    return CV


