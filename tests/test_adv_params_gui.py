import sys
from unittest.mock import MagicMock

import pytest
from PySide6.QtWidgets import QApplication

from src.GUI.code.Adv_params_GUI import Ui_Adv_Params


@pytest.fixture
def app(qtbot):
    """Create a QApplication instance for testing."""
    app = QApplication(sys.argv)
    yield app
    app.quit()


@pytest.fixture
def ui(app):
    """Create an instance of the UI for testing."""
    main_window = MagicMock()
    ui = Ui_Adv_Params()
    ui.setupUi(main_window)
    return ui, main_window


def test_ui_initialization(ui):
    """Test the initialization of the UI components."""
    ui, main_window = ui

    # Check if the main window is set up correctly
    assert main_window.objectName() == "Adv_Params"
    assert main_window.windowTitle() == "Adv Params"


def test_labels(ui):
    """Test the labels in the UI."""
    ui, main_window = ui

    # Check the text of the labels
    assert ui.experiment_conversion_factor_label.text() == "Conversion Factor"
    assert ui.experiment_averag_number_label.text() == "Average Number"
    assert ui.experiment_shunt_resistor_label.text() == "Shunt Resistor /mohm"
    assert ui.advanced_parameters_label.text() == "Advanced Parameters"
    assert ui.experiment_time_step_label.text() == "Time Step /s"
    assert ui.experiment_setpoint_gain_label.text() == "Setpoint Gain"
    assert ui.experiment_setpoint_offset_label.text() == "Setpoint Offset"


def test_line_edit_initialization(ui):
    """Test the initialization of line edit fields."""
    ui, main_window = ui

    # Check if the line edits are initialized correctly
    assert (
        ui.experiment_conversion_factor.objectName()
        == "experiment_conversion_factor"
    )
    assert (
        ui.experiment_setpoint_gain.objectName() == "experiment_setpoint_gain"
    )
    assert (
        ui.experiment_setpoint_offset.objectName()
        == "experiment_setpoint_offset"
    )
    assert (
        ui.experiment_shunt_resistor.objectName()
        == "experiment_shunt_resistor"
    )
    assert ui.experiment_time_step.objectName() == "experiment_time_step"
    assert (
        ui.experiment_averag_number.objectName() == "experiment_average_number"
    )


def test_button_initialization(ui):
    """Test the initialization of buttons."""
    ui, main_window = ui

    # Check if the save button is initialized correctly
    assert (
        ui.save_experiment_file_button.objectName()
        == "save_experiment_file_button"
    )
    assert ui.save_experiment_file_button.text() == "Save "


def test_line_edit_properties(ui):
    """Test the properties of line edit fields."""
    ui, main_window = ui

    assert ui.experiment_conversion_factor.isAcceptDrops() is False
    assert ui.experiment_conversion_factor.alignment() == 0x0004  # AlignCenter
    assert ui.experiment_setpoint_gain.isAcceptDrops() is False
    assert ui.experiment_setpoint_offset.isAcceptDrops() is False
    assert ui.experiment_shunt_resistor.isAcceptDrops() is False
    assert ui.experiment_time_step.isAcceptDrops() is False
    assert ui.experiment_averag_number.isAcceptDrops() is False


def test_label_font_properties(ui):
    """Test the font properties of labels."""
    ui, main_window = ui

    # Check if the labels have the correct font properties
    assert ui.experiment_conversion_factor_label.font().bold() is True
    assert ui.experiment_averag_number_label.font().bold() is True
    assert ui.experiment_shunt_resistor_label.font().bold() is True
    assert ui.advanced_parameters_label.font().bold() is True
    assert ui.experiment_time_step_label.font().bold() is True
    assert ui.experiment_setpoint_gain_label.font().bold() is True
    assert ui.experiment_setpoint_offset_label.font().bold() is True


if __name__ == "__main__":
    pytest.main()
