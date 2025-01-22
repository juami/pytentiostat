import mock
import pytest

from pytentiostat.routines import _initialize_arduino, _load_arduino


class Dummy_port:
    def __init__(self):
        self.description = "default"
        self.device = "com"


class Dummy_arduino:
    def __init__(self):
        self.name = None


def test_load_arduino():
    good_port = Dummy_port()
    good_port.description = "Arduino Uno"
    good_port.device = "good com"
    bad_port = Dummy_port()
    bad_port.description = "Not Arduino"
    with mock.patch(
        "pytentiostat.routines.serial.tools.list_ports.comports",
        return_value=[good_port],
    ):
        com = _load_arduino()
        assert com == "good com"
    with pytest.raises(SystemExit):
        with mock.patch(
            "pytentiostat.routines.serial.tools.list_ports.comports",
            return_value=[bad_port],
        ):
            _load_arduino()
    with pytest.raises(SystemExit):
        _load_arduino()


def test_initialize_arduino():
    da = Dummy_arduino()
    da.name = "good_arduino"

    with pytest.raises(RuntimeError):
        _initialize_arduino("bad_port")
    with mock.patch(
        "pytentiostat.routines.Arduino",
        return_value=da,
    ):
        ard = _initialize_arduino("good_port")
        assert ard.name == "good_arduino"
