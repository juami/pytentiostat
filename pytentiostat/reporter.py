import pandas as pd
import shutil 

def save_data_to_file(data):
    
    #These will be imported from config
    filename = "Place_Holder.csv"
    export_file_destination = "Place/holder/path"
    
    list_data = list(data)
    df = pd.DataFrame(data = list_data, columns = ['Time(s)', 'Voltage(V)', 'Current(mA)'])
    df.to_csv(filename,index=False,header=True)
    
    #Uncomment after config updated
    #shutil.move(Filename, Export_File_Destination)
    
