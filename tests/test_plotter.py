from pytentiostat.plotter import plot_initializer, plot_updater
import pytentiostat.config_reader as cr
import os
import mock

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def test_plot_initializer():
    confdir = os.path.join(THIS_DIR, 'static/')
    config_data = cr.parse_config_file(confdir)
    with mock.patch("my.module.plt.show") as show_patch:
        line = plot_initializer(config_data)
        assert show_patch.called
        xlow, xhigh = line.get_xlim()
        print (xlow)
        ylow, yhigh = line.get_ylim()
        assert xlow == -2.5
        assert xhigh == 2.5
        assert ylow == -2.5
        assert yhigh == 2.5
        xlabel = line.xaxis.get_label()
        ylabel = line.yaxis.get_label()
        assert xlabel == "Voltage (V)"
        assert ylabel == "Current (mA)"

def test_plot_updater():
    confdir = os.path.join(THIS_DIR, 'static/')
    config_data = cr.parse_config_file(confdir)
    with mock.patch("my.module.plt.show") as show_patch:
        line = plot_initializer(config_data)
        data = (0, 0, 0)
        plot_updater(config_data, data, line)
        assert show_patch.called
        xlow, xhigh = line.get_xlim()
        print(xlow)
        ylow, yhigh = line.get_ylim()
        assert xlow == -2.5
        assert xhigh == 2.5
        assert ylow == -2.5
        assert yhigh == 2.5
        xlabel = line.xaxis.get_label()
        ylabel = line.yaxis.get_label()
        assert xlabel == "Voltage (V)"
        assert ylabel == "Current (mA)"