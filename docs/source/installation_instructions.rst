.. The purpose of this file is to provide instructions on how to install the software necessary to access and run
   the pytentiostat software package.

Installation Instructions
=========================

.. seealso::
   Instructions are listed below for installing Miniconda, but the full user documentation for Anaconda is available at
   https://conda.io/projects/conda/en/latest/user-guide/install/index.html

System Requirements
-------------------

* 32- or 64-bit computer
* 400 MB disk space
* Windows, MacOS, or Linux
* Python 2.7, 3.4, 3.5, 3.6, or 3.7
* pycosat
* PyYaml
* Requests

Miniconda Installation
-----------------------
Once all system requirements are met, navigate to the following conda installation page corresponding to the operating
system you are using.

* Windows:  https://conda.io/projects/conda/en/latest/user-guide/install/windows.html
* MacOS:    https://conda.io/projects/conda/en/latest/user-guide/install/macos.html
* Linux:    https://conda.io/projects/conda/en/latest/user-guide/install/linux.html

Following the instructions on the documentation page, click the installer link for Miniconda. Then click on the
link for the 32- or 64- bit installer. This downloads an executable file. Once the file is downloaded, you should verify
the installer hashes using the instructions found at https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification.

Once the installer hashes have been verified, double click the .exe file and follow on-screen prompts to complete the
installation. If you do not have settings preferences, continue with defaults.

Verify the Miniconda Installation was Successful
------------------------------------------------

When the installation is complete, you can test whether it was successful by navigating to the anaconda prompt in the
start menu and running the following line.

.. code-block::

   conda list

If the Miniconda installation was successful, a list of available packages will appear.


pytentiostat Package Installation
----------------------------------

Once the miniconda installation is complete, proceed with the pytentiostat package installation as follows.

1. Open the anaconda prompt from the start menu.

2. Create a conda environment where <mycondaenv> is the name you assign to your environment. You can verify that Python
   version 3 is available by typing :code:`conda search "^python$"` and checking the list of available Python versions.
   To create the conda environment, type:

.. code-block::

   conda create -n <mycondaenv> python=3 anaconda

3. Type :code:`y` to install the python version and the anaconda packaged libraries in the path_to_your_anaconda_location/anaconda/envs/mycondaenv.

4. Activate the environment you created.

.. code-block::

   conda activate <mycondaenv>

5. Install the pytentiostat package.

.. code-block::

   conda install [pytentiostat]


