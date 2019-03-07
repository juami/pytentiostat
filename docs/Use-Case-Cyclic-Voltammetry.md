Use Case – cyclic voltammetry experiment for three electrode cell

1. Input Initial Potential (V vs. Eocv)
2. Input first turnover potential (V vs. Ref)
3. Input second turnover potential (V)
4. Input sweep rate (mV/s)
5. Input number of times the cycle should repeat
6. define final potential (typically 0 V vs. Eocv same as initial potential)
7. Select potential window (auto turn off if potential exits this range)
8. Start scanning voltage from initial potential to first turnover potential while measuring output current (would be nice if I could have a command that would continue to reach current until the scan is stopped)
9. Once first turnover potential is reached, scan from first turnover potential to second turnover potential
10. Once the second turnover potential is reached, create a loop with a set number cycles equal to the defined number of times the cycle should repeat with the following instructions
11. sweep to first turnover potential
12. Once first turnover potential is reached, sweep potential to second turnover potential
13. end loop
14. Once each repeat cycle is complete, sweep to the final potential
15. Stop applying a potential and stop measuring current
16. Plot Current (mA) vs. Potential (V vs. Ref)

Note: need to export potential and current data to a spreadsheet that will automatically save either during the scanning process or that will be exported after the scan is complete.