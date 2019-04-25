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
1. Mike types a file name for the sample being tested (file will contain the voltage, current, and time information)
1. User inputs Initial Potential (V vs. open circuit voltage (Eocv)
1. User inputs first turnover potential (V vs. Ref)
1. User inputs second turnover potential (V)
1. User inputs sweep rate (mV/s)
1. User inputs number of times the cycle should repeat
1. User inputs final potential (typically 0 V vs. Eocv same as initial potential)
1. Select potential window (the program will automatically turn off if potential exits this range)
1. User starts the program (hopefully using a start button on the user interface)
1. The program tells the potentiostat to start measuring current
1. The program stores the applied potential, measured current, and time in a spreadsheet
1. The program initiates the first cycle by sweeping potential from initial potential to first turnover potential
1. The program sweeps the potential from first turnover potential to second turnover potential (this completes the first cycle)
1. The program sweeps the potential from the second turnover potential to the first turnover potential
1. The program sweeps the potential from first turnover potential to second turnover potential (this completes the second cycle)
1. The program repeats the previous two steps until the total number of cycles (defined by User) is reached.
1. The program sweeps the potential to the final potential after the last cycle was completed
1. The program stops applying a potential
1. The program stops measuring current
1. The program stops recording the applied potential, measured current, and time in the spreadsheet
1. The program automatically saves the spreadsheet of collected data
1. Pytentiostat plots current (mA) vs. potential (V vs. Ref)

1. Note: need to export potential and current data to a spreadsheet that will automatically save either during the scanning process or that will be exported after the scan is complete.
