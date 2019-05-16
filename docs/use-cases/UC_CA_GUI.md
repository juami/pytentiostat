Use Case: Running Chronoamperometry for a Two or Three Electrode Cell on the JUAMI Potentiostat through the graphical user interface. Intended User: Undergraduate (UG) Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Chronoamperometry, and limited experience with Python. The instructions in this UC assume that the student already has a two or three electrode cell set up and ready for testing (working electrode, counter electrode, and (optional) reference electrode are all in proper locations and connected to the potentiostat clips). 

### Program Setup ###

1. UG double clicks on the pytentiostat icon on the desktop.
1. The program displays a GUI.
1. UG left clicks on experiment tab on the GUI.
1. The program displays experiment options below the experiment tab.
1. UG left clicks on chronoamperomentery experiment option.
1. The program displays labeled boxes for experimental variables that can be written into. Usable variable ranges are displayed next to boxes. If a range is exceeded with an entered value, the user is notified and the input is deleted.
1. UG inputs potential to apply (V vs. open circuit voltage (Eocv).
1. UG inputs length of time to wait before applying potential.
1. UG inputs length of time to apply potential.
1. UG inputs current window (the program will automatically turn off if current exceeds this range).
1. User starts the program by left clicking on green arrow labeled "Run".
1. The program prompts the user to choose a destination file to save data to.
1. UG selects a file path and name that will be used to export the voltage, current, and time information.
1. The program starts the chronoamperometry experiment.
1. The program displays a plot of Current versus Time and the green run arrow changes to a red octagon labeled "stop", which when left clicked, will interrupt the program.
1. The program starts recording current across cell and time since start of program.
1. The program applies the user-defined potential after waiting for user-defined amount of time for user-defined amount of time.
1. The program stores the applied potential and measured current at each time step into file with user-defined filename.
1. The program stops applying a potential.
1. The program stops measuring current and time since start of program.
1. The program issues a prompt that experminet is complete.
1. UG closes the prompt window.
