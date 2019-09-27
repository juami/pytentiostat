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
    
@pytest.mark.parametrize(
    "input,expected_name,expected_path",
    [
        ({"general_parameters": {"data_output_filename": 1.1, "data_output_path": 2.2}}, "1.1", "2.2"),
        ({"general_parameters": {"data_output_filename": "my_data", "data_output_path": 2.2}}, "my_data", "2.2"),
        ({"general_parameters": {"data_output_filename": 1.1, "data_output_path": "desktop"}}, "1.1", "Desktop")
    ],
)
def test_get_out_params(input, expected_name, expected_path, tmpdir):
    out_name, out_path = get_output_params(input)
    split_out_name = out_name.split("_")
    check_out_name = ""
    for x in split_out_name[-3]:
        check_out_name = check_out_name + x
    split_out_path = out_path.split("_")
    assert check_out_name[0] == expected_name
    assert out_name[-3:] == "csv"
    if (expected_path != "Desktop"):
        assert split_out_path[0] == expected_path
    else: 
        split_out_path = out_path.split("/")
        assert split_out_path[-1] == expected_path
    tmpdict = {"general_parameters": {"data_output_filename": expected_name, "data_output_path": tmpdir}}
    tmp_out_path = get_output_params(tmpdict)[1]
    check_tmp_out_path = tmp_out_path.split("_")
    assert check_tmp_out_path[0] == tmpdir
    
