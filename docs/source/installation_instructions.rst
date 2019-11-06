.. The purpose of this file is to provide instructions on how to install the software necessary to access and run
   the pytentiostat software package.

Installation
=============

.. rubric:: Conda Installation

.. seealso:: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

Before installing Conda, the following system requirements must be met:

* 32- or 64-bit computer
* 400 MB disk space
* Windows, MacOS, or Linux
* Python 2.7, 3.4, 3.5, 3.6, or 3.7
* pycosat
* PyYaml
* Requests

If you do not already have one of the required versions of Python, follow the instructions below.

.. note::
   We used Python 3._ for the Pytentiostat software, so it is encouraged to download that version to ensure
   compatibility.

Go to the following page that corresponds with the operating system that you are working on.

* Windows:      https://www.python.org/downloads/windows/
* MacOS:        https://www.python.org/downloads/mac-osx/
* Linux/UNIX:   https://www.python.org/downloads/source/

Click on the download for the latest release of Python 3.7. Double click the .exe file and follow prompts to proceed
with installation.

-----------------------------------------------------------------------------
| Here we need to add instructions to install pycosat, PyYaml, and Requests.|
-----------------------------------------------------------------------------

Once all system requirements are met, navigate to the following conda installation page corresponding to the operating
system you are using.

* Windows:  https://conda.io/projects/conda/en/latest/user-guide/install/windows.html
* MacOS:    https://conda.io/projects/conda/en/latest/user-guide/install/macos.html
* Linux:    https://conda.io/projects/conda/en/latest/user-guide/install/linux.html

Following the instructions on the documentation page, click the installer link for Miniconda. Then click on the
link for the 32- or 64- bit installer. This downloads an executable file. Once the file is downloaded, you should verify
the installer hashes using the instructions found at https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification.

Once the installer hashes have been verified, double click the .exe file and follow on-screen prompts to complete the
installation. If you do not have settings preferences, continue with defaults. When the installation is complete, you
can test whether it was successful by navigating to the anaconda prompt in the start menu and running the following line.

.. code-block:: conda
   conda list

If the Miniconda installation was successful, a list of available packages will appear.


.. rubric:: Pytentiostat Package Installation

Once python and the conda environment are installed, installing the pytentiostat package is simple.