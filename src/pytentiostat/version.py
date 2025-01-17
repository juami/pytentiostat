#!/usr/bin/env python
##############################################################################
#
# (c) 2025 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Simon J. L. Billinge, Michael Spencer, Yao Tong, Austin
#    Plymill, eremy Hitt, Weizi Yuan, and JUAMI community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/juami/pytentiostat/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Definition of __version__."""

#  We do not use the other three variables, but can be added back if needed.
#  __all__ = ["__date__", "__git_commit__", "__timestamp__", "__version__"]

# obtain version information
from importlib.metadata import version

__version__ = version("pytentiostat")

# End of file
