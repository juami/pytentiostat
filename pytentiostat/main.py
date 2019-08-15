#Pytentiostat function files
from config_reader import parse_config_files
from reporter import save_data_to_file
from tester import experiment
from routines import startup_routine, closing_routine

data, adv_data = parse_config_files()

#Initialize Experiment
com, board, a0, a2, d9 = startup_routine()

#Run the experiment and get the data
times, voltages, currents = experiment(data, adv_data, board, a0, a2, d9)

#Generate a data report
collected_data = zip(times, voltages, currents)
save_data_to_file(data, collected_data)

#Wrap things up
closing_routine(board, d9)
