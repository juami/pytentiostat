import json
from main import ProgramSetup as PS
#from DataHandeling import DataHandeling as DH



if __name__ == '__main__':
    test = PS()
    test.setup_arduino()
    with open('config.json') as json_data_file:
        configdata = json.load(json_data_file)
    ExperimentType = configdata['Experiment']['Type']
    x = configdata[str(ExperimentType)]['Max_Vol']

    PlotCommand = configdata['Plot']['Type']

    WriteCommand = configdata['Write']['Type']

    test.DataProcess(x,'plot','write')
