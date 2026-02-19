import sys

from PySide6.QtWidgets import QApplication


def create_app(argv=None):
    """Create or return a QApplication with a consistent, readable style."""
    if argv is None:
        argv = sys.argv

    app = QApplication.instance()
    if app is None:
        app = QApplication(argv)

    # Ensure readable text/background colors across platforms (e.g. macOS dark mode)
    app.setStyleSheet(
        """
        QWidget {
            color: black;
        }

        QLineEdit,
        QListWidget,
        QComboBox,
        QPlainTextEdit,
        QTextEdit,
        QTableView,
        QTreeView {
            color: black;
            background-color: white;
        }
        """
    )

    return app

