import matplotlib.pyplot as plt
import pytentiostat.config_reader


def plot_initializer(config_data):
    exp_type = pytentiostat.config_reader.get_exp_type(config_data)
    exp_duration = pytentiostat.config_reader.get_exp_duration(config_data)

    times = []
    voltages = []
    currents = []

    # Let's start and setup initial plot parameters
    plt.show()
    axes = plt.gca()
    axes.set_xlim(-2.5, 2.5)
    axes.set_ylim(-2.5, 2.5)

    # This is just for testing
    if exp_type == "CA":
        axes.set_xlim(0, 2 * exp_duration)

    # Let's switch commands based on experiment run
    if exp_type == "LSV":
        line, = axes.plot(voltages, currents, "r-")
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (mA)")
        return line

    elif exp_type == "CA":
        line, = axes.plot(times, currents, "r-")
        plt.xlabel("Time (s)")
        plt.ylabel("Current (mA)")
        return line

    elif exp_type == "CV":
        line, = axes.plot(voltages, currents, "r-")
        plt.xlabel("Voltage (V)")
        plt.ylabel("Current (mA)")
        return line


def plot_updater(config_data, data, line):
    exp_type = pytentiostat.config_reader.get_exp_type(config_data)

    # Let's first unzip and collect Data
    listy = list(data)
    times, voltages, currents = zip(*listy)

    # Let's switch commands based on experiment run
    if exp_type == "LSV":
        line.set_xdata(voltages)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)

    elif exp_type == "CA":
        line.set_xdata(times)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)

    if exp_type == "CV":
        line.set_xdata(voltages)
        line.set_ydata(currents)
        plt.draw()
        plt.pause(1e-17)
