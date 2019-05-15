Use Case: Running Chronoamperometry for a Two or Three Electrode Cell on the JUAMI Potentiostat through the graphical user interface. Intended User: Undergraduate (UG) Researcher at a University in Africa with Introductory Knowledge of Electrochemistry and Chronoamperometry, and limited experience with Python. The instructions in this UC assume that the student already has a two or three electrode cell set up and ready for testing (working electrode, counter electrode, and (optional) reference electrode are all in proper locations and connected to the potentiostat clips). 

Program Setup:

UG double clicks on the pytentiostat icon on the desktop

The program displays a GUI

UG left clicks on experiment tab on the GUI

The program displays experiment options below the experiment tab

UG left clicks on chronoamperomentery experiment option

The program displays labeled boxes for experimental variables that can be written into. Usable variable ranges are displayed next to boxes. If a range is exceeded with an entered value, the user is notified and the input is deleted.

UG inputs potential to apply (V vs. open circuit voltage (Eocv))

UG inputs length of time to wait before applying potential

UG inputs length of time to apply potential

UG inputs current window (the program will automatically turn off if current exceeds this range)

User starts the program by left clicking on green arrow labeled "Run"

The program prompts the user to choose a destination file to save data to 

UG selects a file path and name that will be used to export the voltage, current, and time information

The program starts the chronoamperometry experiment

The program displays a plot of Current versus Time and the green run arrow changes to a red octagon labeled "stop", which when left clicked, will interrupt the program.

The program starts recording current across cell and time since start of program

The program applies the user-defined potential after waiting for user-defined amount of time for user-defined amount of time

The program stores the applied potential and measured current at each time step into file with user-defined filename

The program stops applying a potential

The program stops measuring current and time since start of program

The program issues a prompt that experminet is complete

UG closes the prompt window.
