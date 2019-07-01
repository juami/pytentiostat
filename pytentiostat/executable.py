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
    x = config[str(ExperimentType)]['max_voltage']

    PlotCommand = config['plot']['Type']

    WriteCommand = config['write']['Type']

    test.DataProcess(x,PlotCommand,WriteCommand)
