|Icon| |title|_
===============

.. |title| replace:: pytentiostat
.. _title: https://juami.github.io/pytentiostat

.. |Icon| image:: https://avatars.githubusercontent.com/juami
        :target: https://juami.github.io/pytentiostat
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/juami/pytentiostat/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/juami/pytentiostat/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/juami/pytentiostat/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/juami/pytentiostat

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/pytentiostat
        :target: https://anaconda.org/conda-forge/pytentiostat

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/pytentiostat
        :target: https://pypi.org/project/pytentiostat/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/pytentiostat
        :target: https://pypi.org/project/pytentiostat/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/juami/pytentiostat/issues

Python code for the JUAMI potentiostat

The JUAMI potentiostat is a low-cost potentiostat, for classroom demonstrations and simple lab potentiostat experiments, that is built on the Arduino platform.

This project is to build a Python API for controlling the potentiostat.

For more info about JUAMI: http://www.juami.org/
For more questions about the pytentionstat project: Austin Plymill: austinplymill2021@u.northwestern.edu
Simon Billinge: sb2896@columbia.edu

For more information about the pytentiostat library, please consult our `online documentation <https://juami.github.io/pytentiostat>`_.

Citation
--------

If you use pytentiostat in a scientific publication, we would like you to cite this package as

Yuguang C. Li, Elizabeth L. Melenbrink, Guy J. Cordonier, Christopher Boggs, Anupama Khan,
Morko Kwembur Isaac, Lameck Kabambalika Nkhonjera, David Bahati, Billinge, Simon J.,
Sossina M. Haile, Rodney A. Kreuter, Robert M. Crable, and Thomas E. Mallouk. “An easily fabricated
low-cost potentiostat coupled with user- friendly software for introducing students to electrochemical
reactions and electroanalytical techniques”. In: J. Chem. Educ. 95 (2018), pp. 1658-1661. DOI:
10.1021/acs.jchemed.8b00340

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``pytentiostat_env`` ::

        conda create -n pytentiostat_env pytentiostat
        conda activate pytentiostat_env

To confirm that the installation was successful, type ::

        python -c "import pytentiostat; print(pytentiostat.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``pytentiostat_env`` environment, type ::

        pip install pytentiostat

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/juami/pytentiostat/>`_. Once installed, ``cd`` into your ``pytentiostat`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://juami.github.io/pytentiostat>`_ for tutorials and API references.

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of pytentiostat. Please join the pytentiostat users community by joining the Google group. The pytentiostat project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/juami/pytentiostat/issues>`_ and/or `submit a fix as a PR <https://github.com/juami/pytentiostat/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_.

Feel free to fork the project and contribute. To install pytentiostat
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/juami/pytentiostat/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on pytentiostat please visit the project `web-page <https://juami.github.io/>`_ or email Prof. Simon Billinge at  sb2896@columbia.edu.
