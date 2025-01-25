import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.main import disconnect_port, find_port, start_exp


class TestMain(unittest.TestCase):

    @patch('GUI_routines.find_port_main')
    def test_find_port(self, mock_find_port_main):
        """Test the find_port function."""
        # Arrange
        mock_ui = MagicMock()
        mock_find_port_main.return_value = ('COM3', (MagicMock(), None, None, None))

        # Act
        find_port()

        # Assert
        mock_find_port_main.assert_called_once_with(mock_ui)
        self.assertEqual(mock_ui.arduino_connection_name.currentText(), 'COM3')

    @patch('GUI_routines.disconnect_port_main')
    def test_disconnect_port(self, mock_disconnect_port_main):
        """Test the disconnect_port function."""
        # Arrange
        mock_ui = MagicMock()
        mock_board = MagicMock()
        mock_d9 = MagicMock()

        # Act
        disconnect_port()

        # Assert
        mock_disconnect_port_main.assert_called_once_with(mock_ui, mock_board, mock_d9)

    @patch('GUI_run_exp.run_exp_main')
    def test_start_exp(self, mock_run_exp_main):
        """Test the start_exp function."""
        # Arrange
        mock_grid = MagicMock()
        mock_ui = MagicMock()
        mock_com = 'COM3'
        mock_board_objects = (MagicMock(), None, None, MagicMock())

        # Act
        start_exp(mock_grid)

        # Assert
        mock_run_exp_main.assert_called_once_with(mock_ui, mock_com, mock_board_objects, mock_grid)

    @patch('GUI_file_operation.add_exp')
    def test_add_experiment(self, mock_add_exp):
        """Test the add experiment button connection."""
        mock_ui = MagicMock()
        mock_add_exp.return_value = None

        # Act
        mock_ui.add_experiment_button.clicked.emit()

        # Assert
        mock_add_exp.assert_called_once_with(mock_ui)

    @patch('GUI_file_operation.load_file')
    def test_load_experiment(self, mock_load_file):
        """Test the load experiment button connection."""
        mock_ui = MagicMock()
        mock_load_file.return_value = None

        # Act
        mock_ui.load_experiment_button.clicked.emit()

        # Assert
        mock_load_file.assert_called_once_with(mock_ui)

    @patch('GUI_file_operation.edit_file')
    def test_edit_experiment(self, mock_edit_file):
        """Test the edit experiment button connection."""
        mock_ui = MagicMock()
        mock_edit_file.return_value = None

        # Act
        mock_ui.edit_experiment_button.clicked.emit()

        # Assert
        mock_edit_file.assert_called_once_with(mock_ui)

    @patch('GUI_file_operation.remove_file')
    def test_remove_experiment(self, mock_remove_file):
        """Test the remove experiment button connection."""
        mock_ui = MagicMock()
        mock_remove_file.return_value = None

        # Act
        mock_ui.remove_experiment_button.clicked.emit()

        # Assert
        mock_remove_file.assert_called_once_with(mock_ui)


if __name__ == '__main__':
    unittest.main()
