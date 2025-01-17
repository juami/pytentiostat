# Standard libraries
import sys
from PySide2.QtWidgets import QApplication,QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
#Local library
#GUI_function
import GUI_config_reader as cr

class Ui_Plot(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Plot'
        self.left = 328
        self.top = 10
        self.width = 1000
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def plot_initialize(self,config_data):
        """
        Initialize the plot

        Parameters(passed from GUI_operator.py read_write function)
        ----------
        config_data : dictionary, containing data read from the config file
                      Instance is created in the GUI_run_exp.py - run_exp function


        """
        # Constants for every experiment
        self.fig = Figure(figsize=(10,7.5))
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111,position=[0.12, 0.13, 0.85, 0.85])
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("border: 0 px ;\n")

        self.ax.clear()     # discards the old graph

        self.ax.set_xlim(-3, 3)     # set the start range
        self.ax.set_ylim(-3, 3)

        self.exp_type = cr.get_exp_type(config_data)

        if self.exp_type == "CA":
            self.exp_time = cr.get_exp_time(config_data)
            self.ax.set_xlim(0, 2 * self.exp_time)
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Current (mA)")
            self.lines ,= self.ax.plot([], [],'r')

        elif self.exp_type == "LSV" or self.exp_type == "CV":
            self.ax.set_xlabel("Voltage (V)")
            self.ax.set_ylabel("Current (mA)")
            self.lines, = self.ax.plot([], [], 'r')

    def plot_updater(self,data):
        """
        Update the plot.

        Parameters (passed from GUI_operator.py read_write function)
        ----------
        data : tuple , (times, voltages, currents) , live data during measurement
              Instance is created in the GUI_operator.py - read_write function

        """
        times, voltages, currents = list(data)
        edge = 0.1

        if self.exp_type == "CA":
           self.lines.set_xdata(times)
           self.lines.set_ydata(currents)
           self.ax.set_xlim(-edge, max(times)+edge)
           self.ax.set_ylim(min(currents)-edge, max(currents)+edge)
           self.canvas.draw()
           self.canvas.flush_events()

        elif self.exp_type == "LSV" or self.exp_type == "CV":
           self.lines.set_xdata(voltages)
           self.lines.set_ydata(currents)
           self.ax.set_xlim(min(voltages)-edge, max(voltages)+edge)
           self.ax.set_ylim(min(currents)-edge, max(currents)+edge)

           self.canvas.draw()
           self.canvas.flush_events()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Plot()
    sys.exit(app.exec_())