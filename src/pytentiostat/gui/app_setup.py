import sys

from PySide6.QtWidgets import QApplication


def create_app(argv=None):
    """Create or return a QApplication with a consistent, readable
    style."""
    if argv is None:
        argv = sys.argv

    existing = QApplication.instance()
    if existing is not None:
        return existing

    app = QApplication(argv)

    stylesheet = (
        "QWidget {\n"
        "    color: #000000;\n"
        "    background-color: #F0F0F0;\n"
        "}\n"
        "QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox,\n"
        "QComboBox, QListWidget {\n"
        "    background-color: #FFFFFF;\n"
        "    color: #000000;\n"
        "}\n"
        "QPushButton {\n"
        "    background-color: #E0E0E0;\n"
        "    color: #000000;\n"
        "}\n"
    )
    app.setStyleSheet(stylesheet)

    return app
