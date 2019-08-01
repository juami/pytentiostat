from matplotlib import pyplot as plt

def PlotInitializer(Experiment_Type):

    Times = []
    Voltages = []
    Currents = []

    #Let's start and setup initial plot parameters
    plt.show()
    axes = plt.gca()
    axes.set_xlim(-2.5, 2.5)
    axes.set_ylim(-2.5, 2.5)

    #Let's switch commands based on experiment run
    if Experiment_Type == 'LSV':
        line, = axes.plot(Voltages, Currents, 'r-')
        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (mA)')
        return line

    elif Experiment_Type == 'CA':
        line, = axes.plot(Times, Currents, 'r-')
        plt.xlabel('Time (s)')
        plt.ylabel('Current (mA)')
        return line

    elif Experiment_Type == 'CV':
        line, = axes.plot(Voltages, Currents, 'r-')
        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (mA)')
        return line

def PlotUpdater(Experiment_Type, Data, line):

    #Let's first unzip and collect Data
    listy=list(Data)
    Times, Voltages, Currents = zip(*listy)

    #Let's switch commands based on experiment run
    if Experiment_Type == 'LSV':
        line.set_xdata(Voltages)
        line.set_ydata(Currents)
        plt.draw()
        plt.pause(1e-17)

    elif Experiment_Type == 'CA':
        line.set_xdata(Times)
        line.set_ydata(Currents)
        plt.draw()
        plt.pause(1e-17)

    if Experiment_Type == 'CV':
        line.set_xdata(Voltages)
        line.set_ydata(Currents)
        plt.draw()
        plt.pause(1e-17)
