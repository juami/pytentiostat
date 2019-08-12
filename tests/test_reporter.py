import os
import pytest

from pytentiostat.reporter import save_data_to_file
from pytentiostat.config_reader import get_output_params


@pytest.mark.parametrize(
    "input,expected",
    [
        ([[1, 0, 0]], "Time(s),Voltage(V),Current(mA)\n1,0,0\n"),
        ([[1, 0, 0], [2, 0, 0]],
         "Time(s),Voltage(V),Current(mA)\n1,0,0\n2,0,0\n"),
        ([[1, 0, "None"]], "Time(s),Voltage(V),Current(mA)\n1,0,None\n")
    ],
)
def test_save_data_to_file(input, expected, tmpdir):
    file = os.path.join(tmpdir, "testfile.txt")
    save_data_to_file(input, filename=file)
    with open(file, "r") as f:
        actual = f.read()
    assert expected == actual
