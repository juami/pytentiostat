import unittest
from unittest.mock import MagicMock

import src.GUI.code.GUI_config_reader as cr
from src.GUI.code.GUI_plotter import Ui_Plot


class TestUiPlot(unittest.TestCase):

    def setUp(self):
        """Set up the test case."""
        self.plot = Ui_Plot()
        self.plot.canvas = MagicMock()  # Mock the canvas to avoid GUI rendering
        self.plot.ax = MagicMock()  # Mock the axes to avoid actual plotting

    def test_plot_initialize_CA(self):
        """Test the plot_initialize method for CA experiment type."""
        # Mock the config data and the functions from GUI_config_reader
        config_data = {'exp_type': 'CA', 'exp_time': 5}
        cr.get_exp_type = MagicMock(return_value='CA')
        cr.get_exp_time = MagicMock(return_value=5)

        self.plot.plot_initialize(config_data)

        # Check if the axes limits are set correctly
        self.plot.ax.set_xlim.assert_called_with(0, 10)  # 2 * exp_time
        self.plot.ax.set_xlabel.assert_called_with("Time (s)")
        self.plot.ax.set_ylabel.assert_called_with("Current (mA)")

    def test_plot_initialize_LSV(self):
        """Test the plot_initialize method for LSV experiment type."""
        # Mock the config data and the functions from GUI_config_reader
        config_data = {'exp_type': 'LSV'}
        cr.get_exp_type = MagicMock(return_value='LSV')

        self.plot.plot_initialize(config_data)

        # Check if the axes labels are set correctly
        self.plot.ax.set_xlabel.assert_called_with("Voltage (V)")
        self.plot.ax.set_ylabel.assert_called_with("Current (mA)")

    def test_plot_updater_CA(self):
        """Test the plot_updater method for CA experiment type."""
        self.plot.exp_type = 'CA'
        self.plot.lines = MagicMock()  # Mock the line object

        # Sample data for testing
        data = ([0, 1, 2, 3, 4, 5], [], [0, 1, 0, -1, 0, 1])
        self.plot.plot_updater(data)

        # Check if the line data is updated correctly
        self.plot.lines.set_xdata.assert_called_with([0, 1, 2, 3, 4, 5])
        self.plot.lines.set_ydata.assert_called_with([0, 1, 0, -1, 0, 1])
        self.plot.ax.set_xlim.assert_called()  # Check if xlim was set
        self.plot.ax.set_ylim.assert_called()  # Check if ylim was set

    def test_plot_updater_LSV(self):
        """Test the plot_updater method for LSV experiment type."""
        self.plot.exp_type = 'LSV'
        self.plot.lines = MagicMock()  # Mock the line object

        # Sample data for testing
        data = ([], [0, 1, 2, 3, 4, 5], [0, 1, 0, -1, 0, 1])
        self.plot.plot_updater(data)

        # Check if the line data is updated correctly
        self.plot.lines.set_xdata.assert_called_with([0, 1, 2, 3, 4, 5])
        self.plot.lines.set_ydata.assert_called_with([0, 1, 0, -1, 0, 1])
        self.plot.ax.set_xlim.assert_called()  # Check if xlim was set
        self.plot.ax.set_ylim.assert_called()  # Check if ylim was set


if __name__ == '__main__':
    unittest.main()
