import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.mainwindow_GUI import Ui_MainWindow


class TestUiMainWindow(unittest.TestCase):

    @patch('PySide6.QtWidgets.QDialog')
    @patch('Exp_type_GUI.Ui_Experiment')
    def test_show_exp(self, mock_ui_experiment, mock_qdialog):
        """Test the show_exp method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_experiment_instance = mock_ui_experiment.return_value
        mock_ui_experiment_instance.setupUi = MagicMock()

        ui_main_window = Ui_MainWindow()
        ui_main_window.window = mock_window

        # Act
        exp = ui_main_window.show_exp()

        # Assert
        mock_ui_experiment_instance.setupUi.assert_called_once_with(mock_window)
        self.assertEqual(exp, mock_ui_experiment_instance)

    @patch('PySide6.QtWidgets.QMainWindow')
    @patch('LSV_GUI.Ui_LSV')
    def test_show_LSVwindow(self, mock_ui_lsv, mock_qmainwindow):
        """Test the show_LSVwindow method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_lsv_instance = mock_ui_lsv.return_value
        mock_ui_lsv_instance.setupUi = MagicMock()

        ui_main_window = Ui_MainWindow()
        ui_main_window.window = mock_window

        # Act
        lsv, window = ui_main_window.show_LSVwindow()

        # Assert
        mock_ui_lsv_instance.setupUi.assert_called_once_with(mock_window)
        self.assertEqual(lsv, mock_ui_lsv_instance)
        self.assertEqual(window, mock_window)

    @patch('PySide6.QtWidgets.QMainWindow')
    @patch('CV_GUI.Ui_CV')
    def test_show_CVwindow(self, mock_ui_cv, mock_qmainwindow):
        """Test the show_CVwindow method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_cv_instance = mock_ui_cv.return_value
        mock_ui_cv_instance.setupUi = MagicMock()

        ui_main_window = Ui_MainWindow()
        ui_main_window.window = mock_window

        # Act
        cv, window = ui_main_window.show_CVwindow()

        # Assert
        mock_ui_cv_instance.setupUi.assert_called_once_with(mock_window)
        self.assertEqual(cv, mock_ui_cv_instance)
        self.assertEqual(window, mock_window)

    @patch('PySide6.QtWidgets.QMainWindow')
    @patch('CA_GUI.Ui_CA')
    def test_show_CAwindow(self, mock_ui_ca, mock_qmainwindow):
        """Test the show_CAwindow method."""
        # Arrange
        mock_window = MagicMock()
        mock_ui_ca_instance = mock_ui_ca.return_value
        mock_ui_ca_instance.setupUi = MagicMock()

        ui_main_window = Ui_MainWindow()
        ui_main_window.window = mock_window

        # Act
        ca, window = ui_main_window.show_CAwindow()

        # Assert
        mock_ui_ca_instance.setupUi.assert_called_once_with(mock_window)
        self.assertEqual(ca, mock_ui_ca_instance)
        self.assertEqual(window, mock_window)

    @patch('PySide6.QtWidgets.QWidget')
    @patch('GUI_load_config.Ui_Load')
    def test_load_config(self, mock_ui_load, mock_qwidget):
        """Test the load_config method."""
        # Arrange
        mock_ui_load_instance = mock_ui_load.return_value
        mock_ui_load_instance.setupUi = MagicMock()

        ui_main_window = Ui_MainWindow()
        mock_window = MagicMock()

        # Act
        result = ui_main_window.load_config()

        # Assert
        mock_ui_load_instance.setupUi.assert_called_once_with(mock_window)
        self.assertIsNone(result)  # load_config does not return anything

    @patch('PySide6.QtWidgets.QMainWindow')
    @patch('PySide6.QtGui.QPalette')
    @patch('PySide6.QtGui.QBrush')
    @patch('PySide6.QtGui.QColor')
    @patch('PySide6.QtGui.QIcon')
    @patch('PySide6.QtGui.QPixmap')
    def test_setupUi(self, mock_pixmap, mock_icon, mock_color, mock_brush, mock_palette, mock_main_window):
        """Test the setupUi method."""
        # Arrange
        mock_main_window_instance = MagicMock()
        ui_main_window = Ui_MainWindow()

        # Act
        ui_main_window.setupUi(mock_main_window_instance)

        # Assert
        mock_main_window_instance.setObjectName.assert_called_once_with("MainWindow")
        mock_main_window_instance.resize.assert_called_once_with(1272, 953)
        mock_main_window_instance.setPalette.assert_called_once()
        mock_main_window_instance.setWindowIcon.assert_called_once()
        mock_main_window_instance.setCentralWidget.assert_called_once()
        mock_main_window_instance.setMenuBar.assert_called_once()
        mock_main_window_instance.setStatusBar.assert_called_once()


if __name__ == '__main__':
    unittest.main()
