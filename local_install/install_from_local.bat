:: This batch script will install python 3.8, pytentiostat and it's necessary packages
@echo off
echo Installing python
START /WAIT python-3.8.1-amd64
python --version
if errorlevel 1 goto NoPython
pip install whls/pytz-2019.3-py2.py3-none-any.whl
pip install whls/kiwisolver-1.1.0-cp38-none-win_amd64.whl
pip install whls/six-1.14.0-py2.py3-none-any.whl
pip install whls/pyparsing-2.4.6-py2.py3-none-any.whl
pip install whls/python_dateutil-2.8.1-py2.py3-none-any.whl
pip install whls/pyserial-3.4-py2.py3-none-any.whl
pip install whls/pyFirmata-1.1.0-py2.py3-none-any.whl
pip install whls/numpy-1.18.1-cp38-cp38-win_amd64.whl
pip install whls/pandas-0.25.3-cp38-cp38-win_amd64.whl
pip install whls/PyYAML-5.3-cp38-cp38-win_amd64.whl
pip install whls/urllib3-1.25.8-py2.py3-none-any.whl
pip install whls/py-1.8.1-py2.py3-none-any.whl
pip install whls/idna-2.8-py2.py3-none-any.whl
pip install whls/chardet-3.0.4-py2.py3-none-any.whl
pip install whls/certifi-2019.11.28-py2.py3-none-any.whl
pip install whls/pluggy-0.13.1-py2.py3-none-any.whl
pip install whls/packaging-20.0-py2.py3-none-any.whl
pip install whls/more_itertools-8.1.0-py3-none-any.whl
pip install whls/wcwidth-0.1.8-py2.py3-none-any.whl
pip install whls/atomicwrites-1.3.0-py2.py3-none-any.whl
pip install whls/attrs-19.3.0-py2.py3-none-any.whl
pip install whls/cycler-0.10.0-py2.py3-none-any.whl
pip install whls/matplotlib-3.1.2-cp38-cp38-win_amd64.whl
pip install whls/coverage-5.0.3.tar.gz
pip install whls/colorama-0.4.3-py2.py3-none-any.whl
pip install whls/requests-2.22.0-py2.py3-none-any.whl
pip install whls/pytest-5.3.4-py3-none-any.whl
pip install whls/mock-3.0.5-py2.py3-none-any.whl
pip install whls/codecov-2.0.15-py2.py3-none-any.whl
cd ..
python setup.py install
@pause
goto:eof

:NoPython
echo Python installation failed. Please retry.
@pause
goto:eof
