import os
import sys
from unittest.mock import MagicMock, patch

import pytest
from PySide6.QtWidgets import QApplication

# Assuming the main.py is structured as a module
from src.GUI.code.main import disconnect_port, find_port, start_exp

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)


@pytest.fixture
def app(qtbot):
    """Create a QApplication instance for testing."""
    app = QApplication(sys.argv)
    yield app
    app.quit()


@pytest.fixture
def mock_ui():
    """Mock the UI components."""
    ui = MagicMock()
    return ui


def test_find_port(app, mock_ui):
    """Test the find_port function."""
    with patch(
        "src.GUI.code.GUI_routines.find_port_main",
        return_value=(True, (MagicMock(), None, None, None)),
    ):
        find_port()
        assert mock_ui.find_potentiostat_button.clicked.call_count == 1


def test_disconnect_port(app, mock_ui):
    """Test the disconnect_port function."""
    with patch(
        "src.GUI.code.GUI_routines.disconnect_port_main"
    ) as mock_disconnect:
        disconnect_port()
        mock_disconnect.assert_called_once_with(mock_ui, None, None)


def test_add_experiment(app, mock_ui):
    """Test the add experiment button functionality."""
    with patch("src.GUI.code.GUI_file_operation.add_exp") as mock_add_exp:
        mock_ui.add_experiment_button.clicked.emit()
        mock_add_exp.assert_called_once_with(mock_ui)


def test_load_experiment(app, mock_ui):
    """Test the load experiment button functionality."""
    with patch("src.GUI.code.GUI_file_operation.load_file") as mock_load_file:
        mock_ui.load_experiment_button.clicked.emit()
        mock_load_file.assert_called_once_with(mock_ui)


def test_edit_experiment(app, mock_ui):
    """Test the edit experiment button functionality."""
    with patch("src.GUI.code.GUI_file_operation.edit_file") as mock_edit_file:
        mock_ui.edit_experiment_button.clicked.emit()
        mock_edit_file.assert_called_once_with(mock_ui)


def test_remove_experiment(app, mock_ui):
    """Test the remove experiment button functionality."""
    with patch(
        "src.GUI.code.GUI_file_operation.remove_file"
    ) as mock_remove_file:
        mock_ui.remove_experiment_button.clicked.emit()
        mock_remove_file.assert_called_once_with(mock_ui)


def test_start_exp(app, mock_ui):
    """Test the start experiment functionality."""
    grid = MagicMock()
    with patch("src.GUI.code.GUI_run_exp.run_exp_main") as mock_run_exp:
        start_exp(grid)
        mock_run_exp.assert_called_once_with(
            mock_ui, None, (None, None, None, None), grid
        )
