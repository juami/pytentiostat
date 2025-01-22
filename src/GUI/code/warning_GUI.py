from PySide6 import QtGui, QtWidgets


def warning(text):
    """Initializes the warning window.

    Parameters
    ------
    text : string

    Return
    ------
    Boolean : True if 'OK' is clicked, False if 'cancel'.
    """

    msg = QtWidgets.QMessageBox()
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap("../pics/icon_pytentiostat.ico"),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off,
    )
    msg.setWindowIcon(icon)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(
        QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
    )
    msg.show()
    reply = msg.exec_()
    if reply == QtWidgets.QMessageBox.Ok:
        return True
    elif reply == QtWidgets.QMessageBox.Cancel:
        return False
    return msg
