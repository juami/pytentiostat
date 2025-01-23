#!/usr/bin/env python
##############################################################################
#
# (c) 2025 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Simon J. L. Billinge, Michael Spencer, Yao Tong, Austin
#    Plymill, Jeremy Hitt, Weizi Yuan, and JUAMI community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/juami/pytentiostat/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Definition of __version__."""
import argparse
from importlib.metadata import PackageNotFoundError, version

# Obtain version information
__version__ = version("pytentiostat")

# Obtain version information
try:
    __version__ = version("pytentiostat")
except PackageNotFoundError:
    print("Error: pytentiostat package is not installed.")

# Set up argument parsing
parser = argparse.ArgumentParser(
    description="Pytentiostat Command Line Interface"
)
parser.add_argument(
    "--version",
    action="store_true",
    help="Show the version of pytentiostat",
)

# Parse the arguments
args = parser.parse_args()

# Check if the version flag is set
if args.version:
    print(f"Pytentiostat version: {__version__}")
else:
    print("No command provided. Use --version to get the version.")
