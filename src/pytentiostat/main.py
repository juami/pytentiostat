# Pytentiostat function files
import argparse
import sys

import matplotlib.pyplot as plt

from pytentiostat.config_reader import parse_config_file
from pytentiostat.operator import experiment
from pytentiostat.reporter import save_data_to_file
from pytentiostat.routines import closing_routine, startup_routine
from pytentiostat.version import __version__


def parser():
    parser = argparse.ArgumentParser(
        description="Pytentiostat Command Line Interface.  To use, first plug "
        "in the potentiostat, then run the software by typing"
        "pytentiostat at the command line and follow the prompts."
        "For more information, see the documentation at "
        "juami.github.io/pytentiostat"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the version of pytentiostat and exit",
    )
    args = parser.parse_args()
    return args


class BoardCom:
    def __init__(self):
        self.com, self.board, self.pin_a0, self.pin_a2, self.pin_d9 = (
            startup_routine()
        )


def main():
    args = parser()
    if args.version:
        print(f"{__version__}")
        sys.exit(0)

    try:
        # Initialize Experiment
        board_instance = BoardCom()
        # com, board, a0, a2, d9 = startup_routine()
    except KeyboardInterrupt:
        sys.exit(
            "Connection interrupted by user. Make sure the potentiostat "
            "is plugged in then restart the software.\n"
            "Exiting..."
        )

    board_objects = (
        board_instance.pin_a0,
        board_instance.pin_a2,
        board_instance.pin_d9,
    )
    input("Press enter to load the config file.")
    config_data = parse_config_file()
    while True:
        while True:
            # Run the experiment and get the config_data
            input("Press enter to start the experiment.")
            times, voltages, currents, interrupt = experiment(
                config_data, *board_objects
            )
            if interrupt:
                save = input(
                    "Experiment interrupted. Would you "
                    "like to save the data? [y/n]: "
                )
                if save.lower() == "y":
                    temp_data = zip(times, voltages, currents)
                    save_data_to_file(config_data, temp_data)
                    print("Saved.")
                reconfig = input(
                    "\nIf you want to do a different experiment, edit and "
                    "save the config file then type"
                    ' "new" and press enter.\n'
                    "If you need to reconnect the potentiostat, type "
                    '"reconnect" then press enter.\n'
                    "To close, just press enter. \n"
                )
                if reconfig.lower() == "new":
                    plt.close()
                    config_data = parse_config_file()
                elif reconfig.lower() == "reconnect":
                    plt.close()
                    closing_routine(
                        board_instance.board, board_instance.pin_d9
                    )
                    board_instance.__init__()
                    board_objects = (
                        board_instance.pin_a0,
                        board_instance.pin_a2,
                        board_instance.pin_d9,
                    )
                else:
                    closing_routine(
                        board_instance.board, board_instance.pin_d9
                    )
                    sys.exit(0)
            else:
                break

        # Generate a config_data report
        if not interrupt:
            collected_data = zip(times, voltages, currents)
            save_data_to_file(config_data, collected_data)
            print("Saved.")
        stop = input("\nWould you like to repeat the last experiment? [y/n]: ")
        if stop.lower() != "y":
            break
        else:
            interrupt = False
            plt.close()

    # Wrap things up
    closing_routine(board_instance.board, board_instance.pin_d9)


if __name__ == "__main__":
    main()
