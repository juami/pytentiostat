Use Case: Linear Sweep Voltammetry on the JUAMI Potentiostat

Intended User: Undergraduate Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Voltammetry. The instructions in this UC assume that the student already has an electrochemical cell set up and ready for testing (working electrode, counter electrode, and possibly reference electrode are all in a proper beaker).
As a test case - Mike will perform this use case as someone with knowledge of electrochemistry but little knowledge of Python.

**This version uses a config file**

**Experimental Setup:**
1. Mike plugs the USB cable into the computer and the potentiostat
1. Mike attaches the red wire to the working electrode (material of interest)
1. Mike attaches the black clip to the counter electrode
1. Mike attaches the white clip to the reference electrode if he is using one, or he attaches it to the counter electrode for a two electrode test

**Program Setup:**
1. Mike opens the *Pytentiostat_LSV template* config file from the docs/config-files directory in a text editor
1. Mike saves the file to a new name in the working directory
1. Mike opens the *Getting started - LSV* file for experiment setup instructions
1. Mike replaces all "<?>" placeholders in the Pytentiostat_LSV template with values specific to the experiment being run
1. Mike saves the file
1. Mike runs the python code

**Pytentiostat Operations**
1. Pytentiostat creates an text file with the file name specified in the config file
1. Pytentiostat records the user defined parameters in the file
1. Pytentiostat tells the potentiostat to start measuring current
1. Pytentiostat starts storing the applied potential, measured current, and time in the file while simultaneously plotting measured current vs. potential on the screen
1. Pytentiostat initiates the potential sweep from initial potential to final potential
1. Pytentiostat stops applying a potential
1. Pytentiostat stops measuring current
1. Pytentiostat stops recording the applied potential, measured current, and time in the spreadsheet
1. Pytentiostat automatically saves the spreadsheet of collected data

**If Mike realizes that there was a mistake in the inputs or the experiment is not running properly:**
1. Mike presses Ctrl-C to stop the program
1. Pytentiostat stops applying the potential waveform (which removes any bias to the cell)
1. Pytentiostat stops measuring current
1. Pytentiostat stops recording the applied potential, measured current, and time in the spreadsheet
1. Pytentiostat automatically saves the spreadsheet of collected data

