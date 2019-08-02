#Pytentiostat function files
import reporter as reporter
import tester as tester
import routines as routines

#Initialize Experiment
com, board, a0, a2, d9 = routines.startup_routine()

#Run the experiment and get the data
times, voltages, currents = tester.experiment(board, a0, a2, d9)

#Generate a data report
collected_data = zip(times, voltages, currents)
reporter.save_data_to_file(collected_data)

#Wrap things up
routines.closing_routine(board, d9)
