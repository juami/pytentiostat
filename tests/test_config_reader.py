import yaml
import os
import pytest

from pytentiostat.config_reader import parse_config_file, get_adv_params, get_output_params

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
MOCK_CONFIG = {"general_parameters":{"data_output_filename":"Data"}, "general_parameters":{"data_output_path":"Desktop"}}

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
    with patch.dict(MOCK_CONFIG, {"general_parameters":{"data_output_filename":1.1}, "general_parameters":{"data_output_path":2.2}})
        out_name, out_path = get_output_params(MOCK_CONFIG)
        assert out_name == "1.1"
        assert out_path == "2.2"
        check_extension = out_name.split(".")
        assert check_extension[1] == "csv"
        
    
