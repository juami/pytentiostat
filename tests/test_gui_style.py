import pytest

from GUI.code.app_setup import create_app

pytest.importorskip("PySide6")


def test_app_stylesheet_sets_readable_colors():
    """The global stylesheet should enforce readable text/background colors."""
    app = create_app(["test"])
    stylesheet = app.styleSheet()

    # Basic sanity checks on the stylesheet content
    assert "QLineEdit" in stylesheet
    assert "QComboBox" in stylesheet
    assert "QListWidget" in stylesheet

    # Ensure text and background colors are explicitly set
    assert "color: black" in stylesheet
    assert "background-color: white" in stylesheet
