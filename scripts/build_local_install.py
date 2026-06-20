#!/usr/bin/env python
"""Build an offline install bundle for pytentiostat.

Run this on a machine **with** internet access to populate
``local-install/whls`` with the pytentiostat wheel and all of its
dependencies. The whole repository directory (now containing the wheels and,
optionally, a bundled Python installer) can then be copied to a USB flash
drive and used to install pytentiostat on an **offline** machine via
``scripts/install_from_local.bat``.

For the most reliable result, run this on the same OS/Python as the target
machine (Windows + Python 3.12 for a typical lab computer). To download wheels
for a *different* platform than the one you are on, pass ``--platform`` and
``--python-version`` (this forces wheel-only downloads).

Examples
--------
Build for the current machine::

    python scripts/build_local_install.py

Build Windows wheels for Python 3.12 from another OS by adding::

    --platform win_amd64 --python-version 3.12
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DEST = REPO_ROOT / "local-install" / "whls"
DEFAULT_REQUIREMENTS = REPO_ROOT / "requirements" / "pip.txt"

# A recent Windows installer URL is printed as a reminder; the installer
# itself is intentionally not committed to the repository.
PYTHON_INSTALLER_HINT = (
    "https://www.python.org/downloads/windows/ "
    "(pick a 3.12.x 'Windows installer (64-bit)')"
)


def _run(cmd):
    """Run a subprocess command, echoing it first, and raise on
    failure."""
    print("  $ " + " ".join(str(part) for part in cmd))
    subprocess.run(cmd, check=True)


def build_wheel(dest):
    """Build the pytentiostat wheel (without dependencies) into
    ``dest``."""
    print("Building the pytentiostat wheel...")
    _run(
        [
            sys.executable,
            "-m",
            "pip",
            "wheel",
            str(REPO_ROOT),
            "--no-deps",
            "--wheel-dir",
            str(dest),
        ]
    )


def download_dependencies(dest, requirements, platform, python_version):
    """Download all runtime dependency wheels into ``dest``."""
    print("Downloading dependency wheels...")
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "download",
        "--requirement",
        str(requirements),
        "--dest",
        str(dest),
    ]
    # Cross-platform downloads require pip to fetch pre-built wheels only.
    if platform:
        cmd += ["--only-binary=:all:", "--platform", platform]
    if python_version:
        cmd += ["--python-version", python_version]
    _run(cmd)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help="Directory to write wheels into (default: local-install/whls).",
    )
    parser.add_argument(
        "--requirements",
        type=Path,
        default=DEFAULT_REQUIREMENTS,
        help="Requirements file to download (default: requirements/pip.txt).",
    )
    parser.add_argument(
        "--platform",
        default=None,
        help="Target wheel platform, e.g. win_amd64. Omit to use this "
        "machine's platform.",
    )
    parser.add_argument(
        "--python-version",
        default=None,
        help="Target Python version, e.g. 3.12. Omit to use this "
        "interpreter's version.",
    )
    args = parser.parse_args(argv)

    dest = args.dest.resolve()
    dest.mkdir(parents=True, exist_ok=True)

    build_wheel(dest)
    download_dependencies(
        dest, args.requirements, args.platform, args.python_version
    )

    wheels = sorted(p.name for p in dest.glob("*.whl"))
    archives = sorted(p.name for p in dest.glob("*.tar.gz"))
    print()
    print(f"Done. {len(wheels) + len(archives)} package(s) staged in {dest}")
    print()
    print("Next steps to finish the USB bundle:")
    print(
        "  1. Download a Windows Python installer into 'local-install/'\n"
        f"     {PYTHON_INSTALLER_HINT}"
    )
    print("  2. Copy the whole repository directory onto the USB flash drive.")
    print(
        "  3. On the offline machine, run " "'scripts/install_from_local.bat'."
    )


if __name__ == "__main__":
    main()
