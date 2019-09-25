# Pytentiostat function files
from pytentiostat.config_reader import parse_config_file
from pytentiostat.reporter import save_data_to_file
from pytentiostat.tester import experiment
from pytentiostat.routines import startup_routine, closing_routine
import sys



class BoardCom:
    def __init__(self):
        self.com, self.board, self.pin_a0, self.pin_a2, self.pin_d9 = startup_routine()

    def configure_board(self):
        self.com, self.board, self.pin_a0, self.pin_a2, self.pin_d9 = startup_routine()


config_data = parse_config_file()

try:
    # Initialize Experiment
    board_instance = BoardCom()
    # com, board, a0, a2, d9 = startup_routine()
except KeyboardInterrupt:
    sys.exit("Stopped. Make any changes and then restart the software.\nExiting...")

board_objects = (board_instance.pin_a0, board_instance.pin_a2, board_instance.pin_d9)

reconfig = None

while True:
    try:
        # Run the experiment and get the config_data
        times, voltages, currents = experiment(config_data, *board_objects)
    except KeyboardInterrupt:
        reconfig = input("Experiment stopped. To restart the same experiment, press Enter. \n"
                         "If you want to do a different experiment, type \"New\"\n"
                         "If you need to reconnect the poteniostat, type \"Reconnect\"")
        if reconfig == "":
            reconfig = None
            continue
        if reconfig.lower() == "new":
            config_data = parse_config_file()
            reconfig = None
            continue
        if reconfig.lower() == "reconnect":
            board_instance.configure_board()
            reconfig = None
            continue
        if reconfig == None:
            break


try:
    # Generate a config_data report
    collected_data = zip(times, voltages, currents)
    save_data_to_file(config_data, collected_data)
except KeyboardInterrupt:
    sys.exit("Interrupted")

# Wrap things up
closing_routine(board_instance.board, board_instance.pin_d9)
