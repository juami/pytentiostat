import yaml
import os
import pytest

from pytentiostat.config_reader import parse_config_file, get_adv_params, get_output_params

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def test_parse_config_file():
    confdir = os.path.join(THIS_DIR, 'static/')
    config_data = parse_config_file(confdir)
    assert isinstance(config_data, dict)
    with pytest.raises(SystemExit) as pytest_exit_object:
        config_data = parse_config_file("Not_Real_Directory")
        assert pytest_exit_object.type == SystemExit 
        assert pytest_exit_object.value.code == 42  
        assert pytest_exit_object.sys.stdout.getline().strip() == "Directory containing config file, {}, not found. Exiting...".format("Not_Real_Directory")
    with pytest.raises(SystemExit) as pytest_exit_object:
        config_data = parse_config_file(THIS_DIR)
        assert pytest_exit_object.type == SystemExit 
        assert pytest_exit_object.value.code == 42  
        assert pytest_exit_object.sys.stdout.getline().strip() == "No file named config.yml found in config directory {}. Exiting...".format(THIS_DIR)

def test_get_output_params():
    test_config = {"general_parameters": {"data_output_filename": 1.1, "data_output_path": 2.2}}
    out_name, out_path = get_output_params(test_config)
    check_out_name = out_name.split("_")
    assert check_out_name[0] == "1.1"
    check_out_path = out_path.split("_")
    assert check_out_path[0] == "2.2"
    assert out_name[-3:] == "csv"
        
    
