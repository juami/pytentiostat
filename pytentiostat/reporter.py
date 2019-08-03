import pandas as pd


def save_data_to_file(data, filename="Place_Holder.csv"):
    # These will be imported from config
    export_file_destination = "Place/holder/path"

    list_data = list(data)
    df = pd.DataFrame(data=list_data,
                      columns=['Time(s)', 'Voltage(V)', 'Current(mA)'])
    with open(filename, mode='w', newline='\n') as f:
        df.to_csv(f, index=False, header=True)

    # Uncomment after config updated
    # shutil.move(filename, export_file_destination)


if __name__ == "__main__":
    save_data_to_file([[1, 1, 1], [2, 2, 2]], filename="searchme.txt")
    o = open("Place_Holder.csv", "r")
    print(o.read())
