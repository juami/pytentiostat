import pandas as pd
import os
from pytentiostat.config_reader import get_output_params


def save_data_to_file(config_data, data):
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

    filename, export_destination, default_condition = get_output_params(
        config_data)

    list_data = list(data)
    df = pd.DataFrame(data=list_data,
                      columns=["Time(s)", "Voltage(V)", "Current(mA)"])

    export_path = export_destination

    if default_condition == "Y":
        export_path = os.path.join(os.path.join(os.environ["USERPROFILE"]),
                                   "Desktop")

    with open(os.path.join(export_path, filename), mode="w", newline="\n") as f:
        df.to_csv(f, index=False, header=True)


if __name__ == "__main__":
    # used for debugging.  Does the function write the right file?
    #

    filename, export_destination, default_condition = get_output_params(
        config_data)

    save_data_to_file(config_data, [[1, 1, 1], [2, 2, 2]], filename=filename)
    o = open(filename, "r")
    print(o.read())
