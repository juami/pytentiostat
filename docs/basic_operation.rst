.. _basic operation:

Basic Operation Instructions
============================
GUI-based Operation
-------------------

.. rubric:: Experimental Setup

#. Plug the USB cable into the computer and the potentiostat.
#. Attach electrodes from potentiostat as appropriate to the experimental setup (if you are not familiar with how to set
    up an electrochemical experiment, see `setup <experimentalsetup.html>`_).

.. rubric:: Program Setup

#. Navigate to GUI folder and execute main.py.

.. rubric:: Pytentiostat Operation

#. Pypot main window should display at this point.
#. Click button for find potentiostat.
#. In the drop down box the communication port that is connected should be displayed after the program finds the correct
    port.
#. Now an experiment can be created by clicking on the add button
#. Once clicked, a window should pop up to select the type of experiment that you want to run. Click on the appropriate
    experiment type.
#. The experiment choice window should close and a new window should appear that allows you to edit the experiment
    parameters.
#. Once experiment parameters are input, click generate preview to show the time vs. voltage profile to verify that your
    experimental procedure appears correct.
#. Once satisfied, click save experiment file and then save the file as a .yml file.
#. Now you can begin the experiment by pressing the start button beside the start/stop experiment label.
#. Once experiment is complete, click the disconnect potentiostat button.
#. Now the potentiostat is safe to be removed and the program closed.

Command-Line Operation
----------------------

.. rubric:: Experimental Setup

#. Plug the USB cable into the computer and the potentiostat.
#. Attach electrodes from potentiostat as appropriate to the experimental setup (if you are not familiar with how to set
    up an electrochemical experiment, see `setup <experimentalsetup.html>`_).

.. rubric:: Program Setup

#. Edit the example config file to accommodate your experiment parameters and then save the file.
#. Open up a console window (e.g. command prompt, powershell, Windows terminal).
#. Navigate in the console to the directory pytentiostat/pytentiostat.
#. Type the command :code:`python main.py` and press Enter.

.. rubric:: Pytentiostat Operation

#. Pytentiostat will print to console "Welcome to the JUAMI pytentiostat interface!".
#. Then Pytentiostat will prompt "Press enter to connect to a JUAMI potentiostat.".
#. If the USB connection still secure at this point press enter.
#. Pytentiostat will notify "Searching for potentiostat...".
#. Once connected, Pytentiostat prints to console "Pytentiostat connected to COM".
#. Pytentiostat will then ask to load the config file stating: "Press enter to load the config file".
#. If make sure that config.yaml is set and saved then press enter.
#. The Pytentiostat will have final statement before experiment begins: "Press enter to start the experiment".
#. The Pytentiostat will then run the experiment in the config file.
#. Pytentiostat will display a real-time plot of your experiment (the window might be minimized if you are using an IDE
    for python.
#. After running the experiment, pytentiostat saves the data to location specified in the config file.
#. Pytentiostat will then ask if you want to repeat your experiment: "Would you like to repeat the last experiment?
    [y/n]".
#. If pressing :code:`y`, the Pytentiostat will repeat previous four steps. (Warning: experiment starts immediately
    after pressing enter.)
#. If pressing :code:`n`, the Pytentiostat will close and can be thereafter safely disconnected.
