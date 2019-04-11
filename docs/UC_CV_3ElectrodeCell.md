Use Case � cyclic voltammetry experiment for three electrode cell
Intended User: Undergraduate Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Cyclic Voltammetry. The instructions in this UC assume that the 
Experimental Setup:

The UC I initially had in mind was for a student that already had a 3-electrode testing cell set up, and they just need instructions for setting up the code. For now, these steps are left out, but I have added some details in the Intended User section above.

Program Setup:
1. User inputs Initial Potential (V vs. open circuit voltage (Eocv)
1. User inputs first turnover potential (V vs. Ref)
1. User inputs second turnover potential (V)
1. User inputs sweep rate (mV/s)
1. User inputs number of times the cycle should repeat
1. User inputs final potential (typically 0 V vs. Eocv same as initial potential)
1. Select potential window (the program will automatically turn off if potential exits this range)
1. User clicks the start button (The potential begins to scan from initial potential to first turnover potential while measuring output current)
1. Once first turnover potential is reached, the code automatically scans the potential from first turnover potential to second turnover potential
1. Once the second turnover potential is reached, the code will control the potential to sweep from second turnover potential to first turnover potential, and from first turnover potential to second turnover potential again (this is one complete cycle, and this will continue for the number of cycles defined by User.
1. sweep to first turnover potential
1. Once first turnover potential is reached, sweep potential to second turnover potential
1. end loop
1. Once each repeat cycle is complete, sweep to the final potential
1. Stop applying a potential and stop measuring current
1. Plot Current (mA) vs. Potential (V vs. Ref)

1. Note: need to export potential and current data to a spreadsheet that will automatically save either during the scanning process or that will be exported after the scan is complete.
