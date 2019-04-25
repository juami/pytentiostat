Use Case: Cyclic Voltammetry on the JUAMI Potentiostat
Intended User: Undergraduate Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Cyclic Voltammetry. The instructions in this UC assume that the student already has an electrochemical cell set up and ready for testing (working electrode, counter electrode, and possibly reference electrode are all in a proper beaker).
As a test case - Mike will perform these instructions as someone with knowledge of electrochemistry but little knowledge of Python.

Experimental Setup:

1. Mike plugs the USB cable into the computer and the potentiostat
1. Mike attaches the red wire to the working electrode (material of interest)
1. Mike attaches the black clip to the counter electrode
1. Mike attaches the white clip to the reference electrode if he is using one, or he attaches it to the counter electrode for a two electrode test

Program Setup:
1. Mike opens the Pytentiostat script (the script is incomplete and requires filling in of user-defined information)
1. Mike types a file name for the sample being tested next to 'file name' on line # (file will contain the voltage, current, and time information)
1. Mike inputs Initial Potential on line # (V vs. open circuit voltage (Eocv))
1. Mike inputs first turnover potential (V vs. Ref) on line #
1. Mike inputs second turnover potential (V) on line #
1. Mike inputs sweep rate (mV/s) on line #
1. Mike inputs number of times the cycle should repeat on line #
1. Mike inputs final potential on line # (typically 0 V vs. Eocv same as initial potential)
1. Mike types the lower limiting safety potential on line # (the program will automatically turn off if potential exits this range)
1. Mike types the upper limiting safety potential on line #
1. Mike clicks run to start the Pytentiostat script

Pytentiostat Operations
1. Pytentiostat creates the file with the specified file name
1. Pytentiostat records the user defined parameters in the file
1. Pytentiostat tells the potentiostat to start measuring current
1. Pytentiostat starts storing the applied potential, measured current, and time in the file while simultaneously plotting measured current vs. potential on the screen
1. Pytentiostat initiates the first cycle by sweeping potential from initial potential to first turnover potential
1. Pytentiostat sweeps the potential from first turnover potential to second turnover potential (this completes the first cycle)
1. Pytentiostat sweeps the potential from the second turnover potential to the first turnover potential
1. Pytentiostat sweeps the potential from first turnover potential to second turnover potential (this completes the second cycle)
1. Pytentiostat repeats the previous two steps until the total number of cycles (defined by User) is reached.
1. Pytentiostat sweeps the potential to the final potential after the last cycle was completed
1. Pytentiostat stops applying a potential
1. Pytentiostat stops measuring current
1. Pytentiostat stops recording the applied potential, measured current, and time in the spreadsheet
1. Pytentiostat automatically saves the spreadsheet of collected data
1. Pytentiostat plots current (mA) vs. potential (V vs. Ref)