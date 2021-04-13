.. This page should include information for users to install the Pytentiostat package
   and take any additional measures necessary prior to starting to use the pytentiostat
   for experiments.

.. _get_started:

Getting Started
================


Installing from Github
_______________________

#. Navigate to `<https://github.com/juami/pytentiostat>`_ and click the green button that says Code with a down arrow.
   Then select Download ZIP from the dropdown list.

#. Once the download is finished, unzip the folder.

#. Make sure you have all the dependencies for pytentiostat installed. All the dependencies are listed in the
   requirements folder. For managing dependencies, we recommend `conda <https://www.anaconda.com/>`_ or
   `pip <https://pypi.org/project/pip/>`_.

#. Open a command prompt and navigate to the pytentiostat folder. Run the command ``python setup.py install``.

#. The application should be installed if there were no errors. Now move on to `basic operation <basic_operation.html>`_
   to get started.

Installing from conda-forge
____________________________

Installing from PyPI
_____________________

Flash Drive Installation
_________________________

Instructions for installing pytentiostat onto a Windows computer with a USB
   #. Copy the entire top level directory of Pytentiostat onto a USB flash drive.

      .. important:: Download the Python 3.8 installer and corresponding wheel files onto the USB. Copy the python
                     installer to the folder 'local_install' and the wheels to a subdirectory named 'whls'.

      .. note:: For help to obtain a copy of the installer and wheel files, contact the development team through Github
                or email. `<https://github.com/juami/pytentiostat>`_

   #. Plug in the flash drive to the desired computer and copy all the files onto the computer.

   #. Find the file called 'install_from_local' in the scripts folder and double click it.

   #. Follow the prompts on the screen to install Python 3.8. Be sure to select 'add Python to PATH' at the bottom of
      the first screen.

      It will take a couple of minutes to install all the packages. If everything was successful, you will see no errors
      and the bottom of the command window will say 'press any key to continue...'

   #. For further information on running experiments, continue to `basic operation <basic_operation.rst>`_.
