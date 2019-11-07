.. This page is designed to guide users through steps to setup the software and run experiments.

.. _potentiostat-operation:

How to Operate the JUAMI Potentiostat
=====================================

Once you are familiar with the electrochemical characterization techniques available through the JUAMI potentiostat
and how to setup an electrochemical experiment, follow the guide below that provides instructions on how to setup and run
the JUAMI potentiostat. These instructions assume that the sample or device of interest is ready to be connected and
tested (all that needs to be done is clip the leads to the electrodes). See :ref:`technique-background` and
:ref:`experiment-setup` for more information.

Start the Pytentiostat Experiment
---------------------------------

First, ensure that the JUAMI potentiostat is connected to a USB port via a USB-B to USB-A adapter. To begin an experiment,
open anaconda prompt from the start menu. Navigate to the pytentiostat/ directory and run main.py.

.. code-block:: python

   >main.py

The following message appears:

.. figure::


.. note::

   There is a small applied voltage while the program searches for the potentiostat. Therefore, in systems that are
   sensitive to ~ -2 V vs. the reference electrode, it is recommended to wait until after connection is made and the
   config.yml file is loaded to connect the clips to the electrochemical cell/device.

Press enter when ready to proceed with finding the JUAMI potentiostat.

Next, review the config.yml file in a text editor. An example is shown below. Refer to :ref:`technique-background` for
descriptions of each parameter. Once the config.yml reflects the desired experiment, save the file. Return to the
anaconda prompt and press enter.

Connect the potentiostat clips to their corresponding electrodes.

Press enter to start the experiment.

When the experiment is complete, you have the option to repeat the experiment. If yes, type *y* and press enter. To change
the experiment type or change some parameters, type *n*, press enter, and close the graph.

If no further testing is necessary, it is safe to disconnect the potentiostat from the computer and remove the clips
from the electrodes.






