import unittest
from unittest.mock import MagicMock, patch

from src.GUI.code.GUI_file_operation import (
    add_exp,
    edit_file,
    load_file,
    remove_file,
)


class TestGUIFileOperation(unittest.TestCase):

    def setUp(self):
        # Create a mock UI object
        self.ui_mock = MagicMock()
        self.ui_mock.show_exp.return_value.ca_button = MagicMock()
        self.ui_mock.show_exp.return_value.cv_button = MagicMock()
        self.ui_mock.show_exp.return_value.lsv_button = MagicMock()
        self.ui_mock.load_config.return_value = "gui_test/config_CA.yml"
        self.ui_mock.experiment_queue = MagicMock()

    @patch("MultipleFiles.GUI_file_operation.CA_main")
    @patch("MultipleFiles.GUI_file_operation.CV_main")
    @patch("MultipleFiles.GUI_file_operation.LSV_main")
    def test_add_exp(self, mock_lsv_main, mock_cv_main, mock_ca_main):
        add_exp(self.ui_mock)
        self.ui_mock.show_exp.return_value.ca_button.clicked.emit()
        mock_ca_main.assert_called_once_with(self.ui_mock)

        self.ui_mock.show_exp.return_value.cv_button.clicked.emit()
        mock_cv_main.assert_called_once_with(self.ui_mock)

        self.ui_mock.show_exp.return_value.lsv_button.clicked.emit()
        mock_lsv_main.assert_called_once_with(self.ui_mock)

    @patch("MultipleFiles.GUI_file_operation.QListWidgetItem")
    @patch("MultipleFiles.GUI_file_operation.QIcon")
    def test_load_file(self, mock_qicon, mock_qlistwidgetitem):
        mock_item = MagicMock()
        mock_qlistwidgetitem.return_value = mock_item
        mock_qicon.return_value = MagicMock()

        load_file(self.ui_mock)

        # Check if the filename is parsed correctly
        self.ui_mock.experiment_queue.addItem.assert_called_once_with(mock_item)
        mock_item.setData.assert_any_call(1, mock_qicon.return_value)
        mock_item.setData.assert_any_call(2, "config_CA.yml")
        mock_item.setData.assert_any_call(3, "gui_test/config_CA.yml")

    @patch("MultipleFiles.GUI_file_operation.CA_main")
    @patch("MultipleFiles.GUI_file_operation.CV_main")
    @patch("MultipleFiles.GUI_file_operation.LSV_main")
    @patch("MultipleFiles.GUI_file_operation.parse_config_file")
    @patch("MultipleFiles.GUI_file_operation.warning")
    def test_edit_file(self, mock_warning, mock_parse_config_file, mock_lsv_main, mock_cv_main, mock_ca_main):
        # Mock the current item in the experiment queue
        mock_item = MagicMock()
        mock_item.data.return_value = "gui_test/config_CA.yml"
        self.ui_mock.experiment_queue.currentItem.return_value = mock_item
        mock_parse_config_file.return_value = {"key": "value"}

        edit_file(self.ui_mock)

        # Check if the parse_config_file was called with the correct filename
        mock_parse_config_file.assert_called_once_with("gui_test/config_CA.yml")

        # Check if the correct main function was called
        mock_ca_main.assert_called_once()  # Assuming CA_main is called for CA config

    @patch("MultipleFiles.GUI_file_operation.warning")
    def test_edit_file_no_item(self, mock_warning):
        # Simulate no current item selected
        self.ui_mock.experiment_queue.currentItem.return_value = None
        edit_file(self.ui_mock)

        # Check if the warning was called
        mock_warning.assert_called_once_with(
            "Do you want to edit a existing config file? If so, please load it!"
        )

    def test_remove_file(self):
        # Create a mock item and add it to the experiment queue
        mock_item = MagicMock()
        self.ui_mock.experiment_queue.selectedItems.return_value = [mock_item]
        self.ui_mock.experiment_queue.row.return_value = 0

        remove_file(self.ui_mock)

        # Check if the item was removed from the experiment queue
        self.ui_mock.experiment_queue.takeItem.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
