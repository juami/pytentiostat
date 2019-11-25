.. This page should include information for users to install the Pytentiostat package
   and take any additional measures necessary prior to starting to use the pytentiostat
   for experiments.

Getting Started
================

.. rubric:: Miniconda Installation

Navigate to the following conda installation page corresponding to the operating system you are using.

* Windows:  https://conda.io/projects/conda/en/latest/user-guide/install/windows.html
* MacOS:    https://conda.io/projects/conda/en/latest/user-guide/install/macos.html
* Linux:    https://conda.io/projects/conda/en/latest/user-guide/install/linux.html

Following the instructions on the documentation page, click the installer link for Miniconda. Then click on the
link for the 32- or 64- bit installer. This downloads an executable file. Once the file is downloaded, you should verify
the installer hashes using the instructions found at https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification.

Next, double click the .exe file and follow on-screen prompts to complete the
installation. If you do not have settings preferences, continue with defaults.

.. rubric:: Pytentiostat package installation

.. topic:: Easy install using Anaconda Prompt

   #. Open the anaconda prompt from the start menu.

   #. Create a conda environment where <mycondaenv> is the name you assign to your environment. You can verify that Python
      version 3 is available by typing :code:`conda search "^python$"` and checking the list of available Python versions.
      To create the conda environment, type:

      .. code-block::

         conda create -n <mycondaenv> python=3 anaconda

   #. Type :code:`y` to install the python version and the anaconda packaged libraries in the path_to_your_anaconda_location/anaconda/envs/mycondaenv.

   #. Activate the environment you created.

      .. code-block::

         conda activate <mycondaenv>

   #. Next setup the channel to conda-forge:

      .. code-block::

         conda config --add channels conda-forge

   #. Install the pytentiostat package.

      .. code-block::

         conda install --channels conda-forge pytentiostat