import pandas as pd
import os
from pytentiostat.config_reader import get_output_params


def save_data_to_file(config_data, data, override_outpath=None, override_ts=None):
    """
    Saves measured config_data to a csv file

    Parameters
    ----------
    data : array
        the config_data that will be saved
    filename : string
        the name of the file to save. Optional. Defaults to Place_Holder.csv

    Returns
    -------
        nothing
    """

    filename, export_path = get_output_params(
        config_data, override_ts=override_ts)
    if override_outpath:
        export_path = override_outpath
    list_data = list(data)
    df = pd.DataFrame(data=list_data,
                      columns=["Time(s)", "Voltage(V)", "Current(mA)"])
    with open(os.path.join(export_path, filename), mode="w", newline="\n") as f:
        df.to_csv(f, index=False, header=True)


if __name__ == "__main__":
    # used for debugging.  Does the function write the right file?
    #
    config_data = {"general_parameters": {"experiment_type": None, "rest_time": None,
                                          "step_number": None, "data_output_filename": None,
                                          "data_output_path": None},
                   "linear_sweep_voltammetry": {"start_voltage": None, "end_voltage": None,
                                                "sweep_rate": None},
                   "cyclic_voltammetry": {"start_voltage": None, "first_turnover_voltage":
                                          None, "second_turnover_voltage": None, "sweep_rate":
                                          None,
                                          "number_of_cycles": None},
                   "chronoamperometry": {"voltage": None, "time": None},
                   "advanced_parameters": {"conversion_factor": None, "setpoint_gain": None,
                                           "setpoint_offset": None, "shunt_resistor": None,
                                           "time_step": None, "average_number": None}}

    filename, export_destination = get_output_params(
        config_data)

    save_data_to_file(config_data, [[1, 1, 1], [2, 2, 2]])
    o = open(filename, "r")
    print(o.read())
