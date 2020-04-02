Basic Operation Instructions
=================
GUI-based Operation
---------------------------

.. rubric:: Experimental Setup

#. Plug the USB cable into the computer and the potentiostat.
#. Attach electrodes from potentiostat as appropriate to the experimental setup.

.. rubric:: Program Setup

#. Navigate to GUI folder and execute main.py.

.. rubric:: Pytentiostat Operation

#. Pypot main window should display at this point.
#. Click button for find potentiostat.
#. In the drop down box the communication port that it is connected should be displayed after the program finds the correct port.
#. Now an experiment can be created by clicking on the add button
#. Once clicked, a window should pop up to select the type of experiment that you want to run. Click on the appropriate experiment type.
#. The experiment choice window should close and a new window should appear that allows you to edit the experiment parameters.
#. Once experiment parameters input, click generate preview to show the time vs. voltage profile to verify that your experimental procedure appears correct.
#. Once satisfied, click save experiment file and then save the file as a .yml file.
#. Now you can begin the experiment by pressing the start button beside the start/stop experiment label.
#. Once experiment is complete, click disconnect the disconnect potentiostat button.
#. Now the potentiostat is safe to be removed and the program closed.

Command-Line Operation
---------------------------

.. rubric:: Experimental Setup

#. Plug the USB cable into the computer and the potentiostat.
#. Attach electrodes from potentiostat as appropriate to the experimental setup.

.. rubric:: Program Setup

#. Copy the example config file to an easy to navigate to directory.
#. Edit this file to accomodate your experiment parameters.
#. Open up a console window (e. g. command prompt).
#. Navigate in the console to the directory with the config file.
#. Type the command pytentiostat.

.. rubric:: Pytentiostat Operation

#. Pytentiostat should print to console "Welcome to the JUAMI pytentiostat interface!".
#. Then Pyentiostat should prompt "Press enter to connect to a JUAMI potentiostat.".
#. If USB connection still secure at this point press enter.
#. Pytentiostat will notify "Searching for potentiostat...".
#. Once connected, Pyentiostat prints to console "Pytentiostat connected to COM".
#. Pytentiostat will then ask to load the config file stating: "Press enter to load the config file".
#. If config file in current working directory press enter here.
#. The Pytentiostat will have final statement before experiment begins: "Press enter to start the experiment".
#. The Pytentiostat will then run the experiment in the config file.
#. Pyentiostat will display a plot of real-time of your experiment.
#. After running experiment, pytentiostat saves the data to location specified in the config file.
#. The Pytentiostat will then ask if you want to repeat your experiment: "Would you like to repeat the last experiment? [y/n]".
#. If pressing y, the Pytentiostat will repeat previous four steps.
#. If pressing n the Pytentiostat will close and can be thereafter safely disconnected.
