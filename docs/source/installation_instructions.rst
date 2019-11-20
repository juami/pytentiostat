.. The purpose of this file is to provide instructions on how to install the software necessary to access and run
   the pytentiostat software package.

Installation Instructions
=========================

.. seealso::
   Instructions are listed below for installing Miniconda, but the full user documentation for Anaconda is available at
   https://conda.io/projects/conda/en/latest/user-guide/install/index.html

-------------------
System Requirements
-------------------

* 32- or 64-bit computer
* 400 MB disk space
* Windows, MacOS, or Linux
* Python 2.7, 3.4, 3.5, 3.6, or 3.7
* pycosat
* PyYaml
* Requests

-----------------------
Miniconda Installation
-----------------------
Navigate to the following conda installation page corresponding to the operating system you are using.

* Windows:  https://conda.io/projects/conda/en/latest/user-guide/install/windows.html
* MacOS:    https://conda.io/projects/conda/en/latest/user-guide/install/macos.html
* Linux:    https://conda.io/projects/conda/en/latest/user-guide/install/linux.html

Following the instructions on the documentation page, click the installer link for Miniconda. Then click on the
link for the 32- or 64- bit installer. This downloads an executable file. Once the file is downloaded, you should verify
the installer hashes using the instructions found at https://conda.io/projects/conda/en/latest/user-guide/install/download.html#hash-verification.

Next, double click the .exe file and follow on-screen prompts to complete the
installation. If you do not have settings preferences, continue with defaults.

------------------------------------------------
Verify the Miniconda Installation was Successful
------------------------------------------------

When the installation is complete, you can test whether it was successful by navigating to the anaconda prompt in the
start menu and running the following line.

.. code-block::

   conda list

If the Miniconda installation was successful, a list of available packages will appear.


-------------------------------------------------
pytentiostat Package Installation - conda install
-------------------------------------------------


.. topic:: Anaconda Prompt

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

   #. Install the pytentiostat package.

      .. code-block::

         conda install [pytentiostat]

.. topic:: Windows Command Prompt

   #. Open command prompt, which can be found by searching cmd in the start menu.
   #. Set the path to where Anaconda was installed.

      .. code-block::

         >SETX PATH "%PATH%;C:\Users\mikes\Anaconda3\Scripts;C:\Users\mikes\Anaconda3\Library\bin;C:\Users\mikes\Anaconda3\condabin"
         SUCCESS: Specified value was saved.

   #. Verify that conda is installed by typing :code:`conda -V`. You should see the version of conda that is installed.
   #. Type :code:`conda update conda` to update conda to the most recent version and type :code:`y` when asked whether
      or not to proceed.
   #.

.. topic:: MacOS Terminal

   add instructions


.. topic:: Linux Terminal

   add instructions


-------------------------------------------------------
pytentiostat Installation Instructions - GitHub install
-------------------------------------------------------

.. topic:: Anaconda Prompt

   add instructions

.. topic:: Windows Command Prompt

   #. Go to https://github.com/juami/pytentiostat

   #. Click Clone or download, and click Download ZIP (shown below).

      .. image:: images/github_download.png

   #. Unzip the files and move them to a different directory, if you don't want them to stay in downloads.

   #. Open command prompt by searching cmd in start menu.

   #. In the command prompt, navigate to top level folder that contains the pytentiostat README.txt file.

   #. Run the setup file by typing :code:`python setup.py develop`

   #. Navigate to pytentiostat folder using :code:`cd pytentiostat`

   #. To start an experiment, run the main file by typing :code:`python main.py`

   #. Follow command line prompts to execute the experiment.


.. topic:: MacOS Terminal

   add instructions


.. topic:: Linux Terminal

   add instructions

