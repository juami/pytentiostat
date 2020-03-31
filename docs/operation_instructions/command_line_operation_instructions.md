### Experimental Setup:
1. Plug the USB cable into the computer and the potentiostat.
1. Attach electrodes from potentiostat as appropriate to the experimental setup.

### Program Setup:
1. Copy the example config file to an easy to navigate to directory.
1. Edit this file to accomodate your experiment parameters.
1. Open up a console window (e. g. command prompt).
1. Navigate in the console to the directory with the config file.
1. Type the command pytentiostat.

### Pytentiostat Operation:
1. Pytentiostat should print to console "Welcome to the JUAMI pytentiostat interface!".
1. Then Pyentiostat should prompt "Press enter to connect to a JUAMI potentiostat.".
1. If USB connection still secure at this point press enter.
1. Pytentiostat will notify "Searching for potentiostat...".
1. Once connected, Pyentiostat prints to console "Pytentiostat connected to COM".
1. Pytentiostat will then ask to load the config file stating: "Press enter to load the config file".
1. If config file in current working directory press enter here.
1. The Pytentiostat will have final statement before experiment begins: "Press enter to start the experiment".
1. The Pytentiostat will then run the experiment in the config file.
1. Pyentiostat will display a plot of real-time of your experiment.
1. After running experiment, pytentiostat saves the data to location specified in the config file.
1. The Pytentiostat will then ask if you want to repeat your experiment: "Would you like to repeat the last experiment? [y/n]".
1. If pressing y, the Pytentiostat will repeat previous four steps.
1. If pressing n the Pytentiostat will close and can be thereafter safely disconnected.