.. instructions for creating a USB that can install pytentiostat offline

=============================================================================
Installing pytentiostat onto an offline *Windows* computer with a USB
=============================================================================

These instructions create a USB flash drive that can install pytentiostat on a
lab computer that has **no internet access**. The wheels and the Python
installer are *not* stored in the repository -- you download them once on an
internet-connected machine using the helper script below.

Part 1 -- prepare the USB (on a machine **with** internet)
----------------------------------------------------------

#. Install Python 3.12 and copy (or ``git clone``) this repository onto the
   machine.
#. From the top level of the repository, build the offline bundle::

       python scripts/build_local_install.py

   This builds the pytentiostat wheel and downloads every dependency wheel
   into ``local-install/whls``.

   **Note:** for the most reliable result, run this on the same operating
   system and Python version as the target computer (Windows + Python 3.12 for
   a typical lab machine). To build for a different platform, pass
   ``--platform win_amd64 --python-version 3.12``.

#. Download a Windows Python 3.12 installer from
   https://www.python.org/downloads/windows/ and place the ``python-3.12*.exe``
   file in the ``local-install`` folder. The installer script launches it
   automatically if Python is missing on the target machine.
#. Copy the entire repository directory onto the USB flash drive.

Part 2 -- install pytentiostat (on the **offline** machine)
-----------------------------------------------------------

#. Plug in the USB flash drive and copy the pytentiostat directory onto the
   computer.
#. Open the ``scripts`` folder and double-click ``install_from_local.bat``.
#. If Python is not already installed, the bundled installer launches first --
   be sure to tick **"Add Python to PATH"** on the first screen. (If Python was
   just installed, close the window, open a new terminal, and run the script
   again so the updated ``PATH`` takes effect.)
#. The script creates a ``pytentiostat-env`` virtual environment and installs
   pytentiostat and its dependencies from the bundled wheels. When it finishes
   you will see a success message.
#. Activate the environment and launch the program::

       pytentiostat-env\Scripts\activate
       pytentiostat

   Refer to the main documentation in the ``docs`` folder to start running
   experiments.
