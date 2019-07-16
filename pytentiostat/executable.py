# This is what you want to execute
import json
from main import ProgramSetup as PS
#from DataHandeling import DataHandeling as DH



if __name__ == '__main__':
    test = PS()
    test.setup_arduino()
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)
    ExperimentType = config['Experiment']['Type']
    max_v = config[str(ExperimentType)]['max_voltage']
    min_v = config[str(ExperimentType)]['min_voltage']

    PlotCommand = config['plot']['Type']

    WriteCommand = config['write']['Type']

    if(ExperimentType=="LSV"):
        test.LSV(min_v,max_v,PlotCommand,WriteCommand)
    elif(ExperimentType == "CV"):
        test.CV(min_v,max_v,PlotCommand,WriteCommand)