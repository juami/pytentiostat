#Pytentiostat function files
import Reporter as reporter
import Tester as tester
import Routines as routines

#Initialize Experiment
com, board, a0, a2, d9 = routines.StartupRoutine()

#Run the experiment and get the data
Times, Voltages, Currents = tester.Experiment(board, a0, a2, d9)

#Generate a data report
zippy = zip(Times, Voltages, Currents)
reporter.exporter(zippy)

#Wrap things up
routines.ClosingRoutine(board, d9)
