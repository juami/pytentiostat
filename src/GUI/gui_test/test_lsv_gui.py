import unittest
from unittest.mock import MagicMock, patch

from PySide6 import QtWidgets

from src.GUI.code.LSV_GUI import Ui_LSV


class TestUiLSV(unittest.TestCase):

    @patch('LSV_GUI.Ui_Load')
    def test_load_folder_name(self, mock_ui_load):
        """Test the load_folder_name method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_load_instance = mock_ui_load.return_value
        mock_ui_load_instance.setupUi_save.return_value = "test_file.txt"

        ui_lsv = Ui_LSV()
        ui_lsv.window = mock_window

        # Act
        result = ui_lsv.load_folder_name()

        # Assert
        self.assertEqual(result, "test_file.txt")
        mock_ui_load_instance.setupUi_save.assert_called_once_with(mock_window)

    @patch('LSV_GUI.Ui_Adv_Params')
    def test_AP_window(self, mock_ui_adv_params):
        """Test the AP_window method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_adv_params_instance = mock_ui_adv_params.return_value
        ui_lsv = Ui_LSV()
        ui_lsv.window = mock_window

        # Act
        result_ap, result_window = ui_lsv.AP_window()

        # Assert
        self.assertEqual(result_ap, mock_ui_adv_params_instance)
        self.assertEqual(result_window, mock_window)
        mock_ui_adv_params_instance.setupUi.assert_called_once_with(mock_window)

    @patch('PySide6.QtWidgets.QWidget')
    @patch('PySide6.QtWidgets.QMainWindow')
    @patch('PySide6.QtGui.QPalette')
    @patch('PySide6.QtGui.QBrush')
    @patch('PySide6.QtGui.QColor')
    @patch('PySide6.QtGui.QIcon')
    @patch('PySide6.QtGui.QPixmap')
    def test_setupUi(self, mock_pixmap, mock_icon, mock_color, mock_brush, mock_palette, mock_main_window, mock_widget):
        """Test the setupUi method."""
        # Arrange
        mock_lsv = MagicMock()
        mock_lsv.setObjectName = MagicMock()
        mock_lsv.resize = MagicMock()
        mock_lsv.setPalette = MagicMock()
        mock_lsv.setWindowIcon = MagicMock()
        mock_lsv.setCentralWidget = MagicMock()
        mock_lsv.setMenuBar = MagicMock()
        mock_lsv.setStatusBar = MagicMock()

        ui_lsv = Ui_LSV()

        # Act
        ui_lsv.setupUi(mock_lsv)

        # Assert
        mock_lsv.setObjectName.assert_called_once_with("LSV")
        mock_lsv.resize.assert_called_once_with(800, 519)
        mock_lsv.setPalette.assert_called_once()
        mock_lsv.setWindowIcon.assert_called_once()
        mock_lsv.setCentralWidget.assert_called_once()
        mock_lsv.setMenuBar.assert_called_once()
        mock_lsv.setStatusBar.assert_called_once()


if __name__ == '__main__':
    unittest.main()
