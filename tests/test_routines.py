import mock
import pytest

from pytentiostat.routines import _load_arduino


class Dummy_port():
    def __init__(self, descr):
        self.description = descr
        self.device = "com"


def test_load_arduinos():
    good_port = Dummy_port("Arduino Uno")
    good_port.device = "good com"
    bad_port = Dummy_port("Not Arduino")
    with mock.patch('pytentiostat.routines.serial.tools.list_ports.comports',
                    return_value=[good_port]):
        com = _load_arduino()
        assert com == "good com"
    with pytest.raises(SystemExit):
        with mock.patch('pytentiostat.routines.serial.tools.list_ports.comports',
                        return_value=[bad_port]):
            _load_arduino()
    with pytest.raises(SystemExit):
        _load_arduino()

