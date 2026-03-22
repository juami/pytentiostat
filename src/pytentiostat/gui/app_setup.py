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

    app.setStyleSheet(
        """
        QWidget {
            color: #000000;
            background-color: #F0F0F0;
        }
        QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox,
        QComboBox, QListWidget {
            background-color: #FFFFFF;
            color: #000000;
        }
        QPushButton {
            background-color: #E0E0E0;
            color: #000000;
        }
        """
    )

    return app
