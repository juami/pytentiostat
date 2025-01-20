from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Experiment(object):

    def setupUi(self, Experiment):
        """Initializes the Experiment Type window."""
        Experiment.setObjectName("Experiment")
        Experiment.resize(510, 226)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../pics/icon_pytentiostat.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        Experiment.setWindowIcon(icon)
        Experiment.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Experiment)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.ca_button = QtWidgets.QPushButton(Experiment)
        self.ca_button.setGeometry(QtCore.QRect(15, 50, 131, 121))
        self.ca_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ca_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("../pics/icon_ca.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.ca_button.setIcon(icon1)
        self.ca_button.setIconSize(QtCore.QSize(120, 120))
        self.ca_button.setAutoDefault(False)
        self.ca_button.setFlat(True)
        self.ca_button.setObjectName("ca_button")
        self.cv_button = QtWidgets.QPushButton(Experiment)
        self.cv_button.setGeometry(QtCore.QRect(190, 50, 131, 121))
        self.cv_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("../pics/icon_cv.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.cv_button.setIcon(icon2)
        self.cv_button.setIconSize(QtCore.QSize(120, 120))
        self.cv_button.setAutoDefault(False)
        self.cv_button.setFlat(True)
        self.cv_button.setObjectName("cv_button")
        self.lsv_button = QtWidgets.QPushButton(Experiment)
        self.lsv_button.setGeometry(QtCore.QRect(360, 50, 131, 121))
        self.lsv_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("../pics/icon_lsv.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.lsv_button.setIcon(icon3)
        self.lsv_button.setIconSize(QtCore.QSize(120, 120))
        self.lsv_button.setAutoDefault(False)
        self.lsv_button.setFlat(True)
        self.lsv_button.setObjectName("lsv_button")
        self.ca_label = QtWidgets.QLabel(Experiment)
        self.ca_label.setGeometry(QtCore.QRect(20, 190, 120, 18))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 125, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 125, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ca_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.ca_label.setFont(font)
        self.ca_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ca_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ca_label.setLineWidth(2)
        self.ca_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ca_label.setObjectName("ca_label")
        self.cv_label = QtWidgets.QLabel(Experiment)
        self.cv_label.setGeometry(QtCore.QRect(200, 190, 120, 18))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 87, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 87, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cv_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.cv_label.setFont(font)
        self.cv_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cv_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cv_label.setLineWidth(2)
        self.cv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_label.setObjectName("cv_label")
        self.lsv_label = QtWidgets.QLabel(Experiment)
        self.lsv_label.setGeometry(QtCore.QRect(370, 190, 120, 18))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 221, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 221, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lsv_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.lsv_label.setFont(font)
        self.lsv_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lsv_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lsv_label.setLineWidth(2)
        self.lsv_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lsv_label.setObjectName("lsv_label")
        self.question_label = QtWidgets.QLabel(Experiment)
        self.question_label.setGeometry(QtCore.QRect(90, 20, 351, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.question_label.setFont(font)
        self.question_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.question_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.question_label.setLineWidth(2)
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("question_label")

        self.retranslateUi(Experiment)
        QtCore.QMetaObject.connectSlotsByName(Experiment)

    def retranslateUi(self, Experiment):
        _translate = QtCore.QCoreApplication.translate
        Experiment.setWindowTitle(_translate("Experiment", "Experiment Type"))
        self.ca_label.setText(_translate("Experiment", "CA"))
        self.cv_label.setText(_translate("Experiment", "CV"))
        self.lsv_label.setText(_translate("Experiment", "LSV"))
        self.question_label.setText(
            _translate("Experiment", "Please select an experiment")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Experiment = QtWidgets.QDialog()
    ui = Ui_Experiment()
    ui.setupUi(Experiment)
    Experiment.show()
    sys.exit(app.exec_())
