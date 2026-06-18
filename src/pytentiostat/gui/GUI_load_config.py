import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget


class Ui_Load(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        file = self.openFileNameDialog()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../pics/icon_pytentiostat.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        return file

    def setupUi_save(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        folder = self.saveFileDialog()
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../pics/icon_pytentiostat.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        return folder

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file, _ = QFileDialog.getOpenFileName(
            self,
            "Load config file",
            "",
            "All Files (*);;Config Files (*config.yml)",
            options=options,
        )
        if file:
            return file

    def saveFileDialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Select directory")
        if folder:
            return folder + "/"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_Load()
    sys.exit(app.exec_())
