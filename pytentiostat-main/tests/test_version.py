"""Unit tests for __version__.py."""

import pytentiostat


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(pytentiostat, "__version__")
    assert pytentiostat.__version__ != "0.0.0"
