:: This batch script will install Python 3.12, pytentiostat, and its necessary packages
@echo off
cd ../local_install
echo Installing Python 3.12
START /WAIT python-3.12.8-amd64.exe
python --version
if errorlevel 1 goto NoPython

:: Upgrade pip to the latest version
python -m pip install --upgrade pip

:: Install necessary packages
pip install pytentiostat
pip install pytz
pip install kiwisolver
pip install six
pip install pyparsing
pip install python_dateutil
pip install pyserial
pip install pyFirmata
pip install numpy
pip install pandas
pip install PyYAML
pip install urllib3
pip install py
pip install idna
pip install chardet
pip install certifi
pip install pluggy
pip install packaging
pip install more_itertools
pip install wcwidth
pip install atomicwrites
pip install attrs
pip install cycler
pip install matplotlib
pip install coverage
pip install colorama
pip install requests
pip install pytest
pip install mock
pip install codecov

cd ..
python setup.py install
@pause
goto:eof

:NoPython
echo Python installation failed. Please retry.
@pause
goto:eof