import pandas as pd
import shutil 

def exporter(Data):
    
    #These will be imported from config
    Filename = "Place_Holder.csv"
    Export_File_Destination = "Place/holder/path"
    
    listdata = list(Data)
    dF = pd.DataFrame(data = listdata, columns = ['Time(s)', 'Voltage(V)', 'Current(mA)'])
    dF.to_csv(Filename,index=False,header=True)
    
    #Uncomment after config updated
    #shutil.move(Filename, Export_File_Destination)
    
