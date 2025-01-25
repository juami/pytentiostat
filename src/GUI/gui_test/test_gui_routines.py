import sys
import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_routines import (
    _initialize_arduino,
    _load_arduino,
    closing_routine,
    disconnect_port_main,
    find_port_main,
    startup_routine,
)


class TestGUIRoutines(unittest.TestCase):

    @patch('serial.tools.list_ports.comports')
    def test_load_arduino(self, mock_comports):
        """Test the _load_arduino function."""
        mock_comports.return_value = [MagicMock(device='COM3'), MagicMock(device='COM4')]
        ui_mock = MagicMock()
        ports = _load_arduino(ui_mock)

        # Check if the ports are loaded correctly
        self.assertEqual(ports, ['COM3', 'COM4'])
        ui_mock.arduino_connection_name.addItem.assert_any_call('COM3')
        ui_mock.arduino_connection_name.addItem.assert_any_call('COM4')

    @patch('pyfirmata.Arduino')
    def test_initialize_arduino_success(self, mock_arduino):
        """Test the _initialize_arduino function for successful
        initialization."""
        com_port = 'COM3'
        board = _initialize_arduino(com_port)
        self.assertEqual(board, mock_arduino.return_value)

    @patch('pyfirmata.Arduino')
    def test_initialize_arduino_failure(self, mock_arduino):
        """Test the _initialize_arduino function for failure."""
        mock_arduino.side_effect = Exception("Error")
        with self.assertRaises(SystemExit):
            _initialize_arduino('COM3')

    @patch('serial.tools.list_ports.comports')
    @patch('GUI_routines.warning')
    @patch('pyfirmata.Arduino')
    def test_startup_routine_success(self, mock_arduino, mock_warning, mock_comports):
        """Test the startup_routine function for successful startup."""
        mock_comports.return_value = [MagicMock(device='COM3')]
        ui_mock = MagicMock()
        ui_mock.arduino_connection_name.currentText.return_value = 'COM3'

        board_mock = MagicMock()
        mock_arduino.return_value = board_mock

        com, board, a0, a2, d9 = startup_routine(ui_mock)

        self.assertEqual(com, 'COM3')
        self.assertEqual(board, board_mock)
        self.assertIsNotNone(a0)
        self.assertIsNotNone(a2)
        self.assertIsNotNone(d9)

    @patch('serial.tools.list_ports.comports')
    @patch('GUI_routines.warning')
    def test_startup_routine_failure(self, mock_warning, mock_comports):
        """Test the startup_routine function for failure when port is not
        connected."""
        mock_comports.return_value = []
        ui_mock = MagicMock()
        ui_mock.arduino_connection_name.currentText.return_value = 'COM3'

        com, board, a0, a2, d9 = startup_routine(ui_mock)

        self.assertEqual(com, 'COM3')
        self.assertIsNone(board)
        self.assertIsNone(a0)
        self.assertIsNone(a2)
        self.assertIsNone(d9)
        mock_warning.assert_called_with("Current port not connected!")

    @patch('pyfirmata.Arduino')
    def test_closing_routine(self, mock_arduino):
        """Test the closing_routine function."""
        board_mock = MagicMock()
        d9_mock = MagicMock()
        closing_routine(board_mock, d9_mock)

        d9_mock.write.assert_called_with(0.5)
        board_mock.exit.assert_called()

    @patch('GUI_routines.startup_routine')
    @patch('GUI_routines.warning')
    @patch('PySide6.QtGui.QIcon')
    def test_find_port_main_success(self, mock_qicon, mock_warning, mock_startup_routine):
        """Test the find_port_main function for successful port finding."""
        ui_mock = MagicMock()
        mock_startup_routine.return_value = ('COM3', MagicMock(), MagicMock(), MagicMock(), MagicMock())

        com, board_objects = find_port_main(ui_mock)

        self.assertEqual(com, 'COM3')
        self.assertIsNotNone(board_objects)
        ui_mock.arduino_connection_indicator.setIcon.assert_called_with(mock_qicon.return_value)

    @patch('GUI_routines.closing_routine')
    @patch('PySide6.QtGui.QIcon')
    def test_disconnect_port_main(self, mock_qicon, mock_closing_routine):
        """Test the disconnect_port_main function."""
        ui_mock = MagicMock()
        board_mock = MagicMock()
        d9_mock = MagicMock()

        disconnect_port_main(ui_mock, board_mock, d9_mock)

        mock_closing_routine.assert_called_with(board_mock, d9_mock)
        ui_mock.arduino_connection_indicator.setIcon.assert_called_with(mock_qicon.return_value)


if __name__ == '__main__':
    unittest.main()
