# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:30:15 2019

@author: Austin
"""

import pandas as pd
import shutil 

def exporter(Data):
    
    #These will be imported from config
    Filename = "Place_Holder.csv"
    Export_File_Destination = "Place/holder/path"
    
    listdata = list(Data)
    DF = pd.DataFrame(data = listdata, columns = ['Time(s)', 'Voltage(V)', 'Current(mA)'])
    DF.to_csv(Filename,index=False,header=True)
    
    #Uncomment after config updated
    #shutil.move(Filename, Export_File_Destination)
    
    
    