from matplotlib import pyplot as plt

def plot_initializer(experiment_type):

    times = []
    voltages = []
    currents = []

    #Let's start and setup initial plot parameters
    plt.show()
    axes = plt.gca()
    axes.set_xlim(-2.5, 2.5)
    axes.set_ylim(-2.5, 2.5)

    #Let's switch commands based on experiment run
    if experiment_type == 'LSV':
        line, = axes.plot(voltages, currents, 'r-')
        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (mA)')
        return line

    elif experiment_type == 'CA':
        line, = axes.plot(times, currents, 'r-')
        plt.xlabel('Time (s)')
        plt.ylabel('Current (mA)')
        return line

    elif experiment_type == 'CV':
        line, = axes.plot(voltages, currents, 'r-')
        plt.xlabel('Voltage (V)')
        plt.ylabel('Current (mA)')
        return line

def plot_updater(experiment_type, data, line):

    #Let's first unzip and collect Data
    listy=list(data)
    times, voltages, currents = zip(*listy)

    #Let's switch commands based on experiment run
    if experiment_type == 'LSV':
        line.set_xdata(voltages)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)

    elif experiment_type == 'CA':
        line.set_xdata(times)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)

    if experiment_type == 'CV':
        line.set_xdata(voltages)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)
