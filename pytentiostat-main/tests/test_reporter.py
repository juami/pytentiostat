import datetime
import os

import pytest

from pytentiostat.config_reader import parse_config_file
from pytentiostat.reporter import save_data_to_file

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.mark.parametrize(
    "input,expected",
    [
        ([[1, 0, 0]], "Time(s),Voltage(V),Current(mA)\n1,0,0\n"),
        (
            [[1, 0, 0], [2, 0, 0]],
            "Time(s),Voltage(V),Current(mA)\n1,0,0\n2,0,0\n",
        ),
        ([[1, 0, "None"]], "Time(s),Voltage(V),Current(mA)\n1,0,None\n"),
    ],
)
def test_save_data_to_file(input, expected, tmpdir):
    ts = datetime.datetime.now().strftime("%H_%M_%S")
    out_name_ts = "testfile" + "_" + ts + ".csv"
    file = tmpdir.join(out_name_ts)
    confdir = os.path.join(THIS_DIR, "static/")
    config_data = parse_config_file(confdir)
    save_data_to_file(
        config_data, input, override_outpath=tmpdir, override_ts=ts
    )
    with open(file, "r") as f:
        actual = f.read()
    assert expected == actual
