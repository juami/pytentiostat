# Pytentiostat function files
from pytentiostat.config_reader import parse_config_file
from pytentiostat.reporter import save_data_to_file
from pytentiostat.tester import experiment
from pytentiostat.routines import startup_routine, closing_routine

config_data = parse_config_file()


class BoardCom:
    def __init__(self):
        self.com, self.board, self.pin_a0, self.pin_a2, self.pin_d9 = startup_routine()

    def configure_board(self):
        self.com, self.board, self.pin_a0, self.pin_a2, self.pin_d9 = startup_routine()


# Initialize Experiment
board_instance = BoardCom()
#com, board, a0, a2, d9 = startup_routine()

# Run the experiment and get the config_data
board_objects = (board_instance.board, board_instance.pin_a0, board_instance.pin_a2, board_instance.pin_d9)
times, voltages, currents = experiment(config_data, *board_objects)

# Generate a config_data report
collected_data = zip(times, voltages, currents)
save_data_to_file(config_data, collected_data)

# Wrap things up
closing_routine(board_instance.board, board_instance.pin_d9)
