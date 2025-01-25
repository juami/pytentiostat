import unittest
from unittest.mock import MagicMock, patch

from PySide6.QtWidgets import QApplication

from src.GUI.code.GUI_load_config import Ui_Load


class TestUiLoad(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])  # Create a QApplication instance
        self.ui = Ui_Load()  # Create an instance of the Ui_Load class

    @patch("MultipleFiles.GUI_load_config.QFileDialog.getOpenFileName")
    def test_openFileNameDialog(self, mock_getOpenFileName):
        # Mock the return value of the file dialog
        mock_getOpenFileName.return_value = ("path/to/config.yml", "")

        file = self.ui.openFileNameDialog()

        # Check if the returned file path is correct
        self.assertEqual(file, "path/to/config.yml")

    @patch("MultipleFiles.GUI_load_config.QFileDialog.getExistingDirectory")
    def test_saveFileDialog(self, mock_getExistingDirectory):
        # Mock the return value of the directory dialog
        mock_getExistingDirectory.return_value = "path/to/directory"

        folder = self.ui.saveFileDialog()

        # Check if the returned folder path is correct
        self.assertEqual(folder, "path/to/directory/")

    @patch("MultipleFiles.GUI_load_config.QMainWindow")
    def test_setupUi(self, mock_main_window):
        mock_main_window.setObjectName = MagicMock()
        mock_main_window.resize = MagicMock()
        mock_main_window.setWindowIcon = MagicMock()

        file = self.ui.setupUi(mock_main_window)

        # Check if the main window is set up correctly
        mock_main_window.setObjectName.assert_called_with("MainWindow")
        mock_main_window.resize.assert_called_with(640, 480)
        self.assertIsNotNone(file)  # Ensure a file is returned

    @patch("MultipleFiles.GUI_load_config.QMainWindow")
    def test_setupUi_save(self, mock_main_window):
        mock_main_window.setObjectName = MagicMock()
        mock_main_window.resize = MagicMock()
        mock_main_window.setWindowIcon = MagicMock()

        folder = self.ui.setupUi_save(mock_main_window)

        # Check if the main window is set up correctly
        mock_main_window.setObjectName.assert_called_with("MainWindow")
        mock_main_window.resize.assert_called_with(640, 480)
        self.assertIsNotNone(folder)  # Ensure a folder is returned


if __name__ == "__main__":
    unittest.main()
