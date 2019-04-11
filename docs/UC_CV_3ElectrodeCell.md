Use Case: Running Cyclic Voltammetry for a Three Electrode Cell on the JUAMI Potentiostat
Intended User: Undergraduate Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Cyclic Voltammetry. The instructions in this UC assume that the student already has a three electrode cell set up and ready for testing (working electrode, counter electrode, and reference electrode are all in a proper beaker and connected to the potentiostat clips).
Experimental Setup:

The UC I initially had in mind was for a student that already had a 3-electrode testing cell set up, and they just need instructions for setting up the code. For now, these steps are left out, but I have added some details in the Intended User section above.

Program Setup:
1. User defines a file name that will be used to export the voltage, current, and time information.
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
