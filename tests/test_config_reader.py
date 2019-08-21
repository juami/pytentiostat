import yaml
import os

from pytentiostat.config_reader import parse_config_file, get_adv_params

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def test_parse_config_files():
    confdir = os.path.join(THIS_DIR, 'static/')
    config_data = parse_config_file(confdir)
    assert isinstance(config_data, dict)
