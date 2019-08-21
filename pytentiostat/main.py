# Pytentiostat function files
from pytentiostat.config_reader import parse_config_file
from pytentiostat.reporter import save_data_to_file
from pytentiostat.tester import experiment
from pytentiostat.routines import startup_routine, closing_routine

config_data = parse_config_file()

# Initialize Experiment
com, board, a0, a2, d9 = startup_routine()

# Run the experiment and get the config_data
times, voltages, currents = experiment(config_data, board, a0, a2, d9)

# Generate a config_data report
collected_data = zip(times, voltages, currents)
save_data_to_file(config_data, collected_data)

# Wrap things up
closing_routine(board, d9)
