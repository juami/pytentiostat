import os

import pytest

from pytentiostat.config_reader import parse_config_file

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def test_parse_config_files():
    confdir = os.path.join(THIS_DIR, "static/")
    config_data = parse_config_file(confdir)
    assert isinstance(config_data, dict)
    with pytest.raises(SystemExit) as pytest_exit_object:
        parse_config_file("Not_Real_Directory")
        assert pytest_exit_object.type == SystemExit
        assert pytest_exit_object.value.code == 42
        assert pytest_exit_object.sys.stdout.getline().strip() == (
            "Directory containing config file, {}, " "not found. " "Exiting..."
        ).format("Not_Real_Directory")
    with pytest.raises(SystemExit) as pytest_exit_object:
        parse_config_file(THIS_DIR)
        assert pytest_exit_object.type == SystemExit
        assert pytest_exit_object.value.code == 42
        assert pytest_exit_object.sys.stdout.getline().strip() == (
            "No file named config.yml found in config "
            "directory {}. Exiting..."
        ).format(THIS_DIR)
