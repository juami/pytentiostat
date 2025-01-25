import unittest

from PySide6 import QtWidgets

from src.GUI.code.Exp_type_GUI import Ui_Experiment


class TestUiExperiment(unittest.TestCase):
    def setUp(self):
        """Set up the application and the UI before each test."""
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Experiment()
        self.ui.setupUi(self.window)

    def test_window_title(self):
        """Test if the window title is set correctly."""
        self.assertEqual(self.window.windowTitle(), "Experiment Type")

    def test_labels_exist(self):
        """Test if all labels are created and have the correct text."""
        self.assertIsNotNone(self.ui.ca_label)
        self.assertIsNotNone(self.ui.cv_label)
        self.assertIsNotNone(self.ui.lsv_label)
        self.assertIsNotNone(self.ui.question_label)

        self.assertEqual(self.ui.ca_label.text(), "CA")
        self.assertEqual(self.ui.cv_label.text(), "CV")
        self.assertEqual(self.ui.lsv_label.text(), "LSV")
        self.assertEqual(self.ui.question_label.text(), "Please select an experiment")

    def test_buttons_exist(self):
        """Test if all buttons are created."""
        self.assertIsNotNone(self.ui.ca_button)
        self.assertIsNotNone(self.ui.cv_button)
        self.assertIsNotNone(self.ui.lsv_button)

        # Check if buttons have icons set
        self.assertTrue(self.ui.ca_button.icon().isNull() is False)
        self.assertTrue(self.ui.cv_button.icon().isNull() is False)
        self.assertTrue(self.ui.lsv_button.icon().isNull() is False)

    def test_button_box_exists(self):
        """Test if the button box is created and has the correct buttons."""
        self.assertIsNotNone(self.ui.buttonBox)
        self.assertTrue(QtWidgets.QDialogButtonBox.Ok in self.ui.buttonBox.standardButtons())
        self.assertTrue(QtWidgets.QDialogButtonBox.Cancel in self.ui.buttonBox.standardButtons())

    def tearDown(self):
        """Clean up after each test."""
        self.window.close()


if __name__ == "__main__":
    unittest.main()
