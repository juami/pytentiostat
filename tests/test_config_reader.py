import yaml
import os

from pytentiostat.config_reader import parse_config_files, get_adv_params

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def test_parse_config_files():

    confdir = os.path.join(THIS_DIR, 'static/')
    config_data, adv_config_data = parse_config_files(confdir)
    expected_average_number = adv_config_data["average_number"]
    Int_check = is_instance(expected_average_number, int)
    assert Int_check == True
