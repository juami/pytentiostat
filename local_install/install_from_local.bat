:: This batch script will install python 3.8, pytentiostat and it's necessary packages

echo Installing python
START /WAIT python-3.8.1-amd64
python --version
if errorlevel 1 goto NoPython
pip install pytz-2019.3-py2.py3-none-any.whl
pip install kiwisolver-1.1.0-cp38-none-win_amd64.whl
pip install six-1.14.0-py2.py3-none-any.whl
pip install pyparsing-2.4.6-py2.py3-none-any.whl
pip install python_dateutil-2.8.1-py2.py3-none-any.whl
pip install pyserial-3.4-py2.py3-none-any.whl
pip install pyFirmata-1.1.0-py2.py3-none-any.whl
pip install numpy-1.18.1-cp38-cp38-win_amd64.whl
pip install pandas-0.25.3-cp38-cp38-win_amd64.whl
pip install PyYAML-5.3-cp38-cp38-win_amd64.whl
pip install urllib3-1.25.8-py2.py3-none-any.whl
pip install py-1.8.1-py2.py3-none-any.whl
pip install idna-2.8-py2.py3-none-any.whl
pip install chardet-3.0.4-py2.py3-none-any.whl
pip install certifi-2019.11.28-py2.py3-none-any.whl
pip install pluggy-0.13.1-py2.py3-none-any.whl
pip install packaging-20.0-py2.py3-none-any.whl
pip install more_itertools-8.1.0-py3-none-any.whl
pip install wcwidth-0.1.8-py2.py3-none-any.whl
pip install atomicwrites-1.3.0-py2.py3-none-any.whl
pip install attrs-19.3.0-py2.py3-none-any.whl
pip install cycler-0.10.0-py2.py3-none-any.whl
pip install matplotlib-3.1.2-cp38-cp38-win_amd64.whl
pip install coverage-5.0.3.tar.gz
pip install colorama-0.4.3-py2.py3-none-any.whl
pip install requests-2.22.0-py2.py3-none-any.whl
pip install pytest-5.3.4-py3-none-any.whl
pip install mock-3.0.5-py2.py3-none-any.whl
pip install codecov-2.0.15-py2.py3-none-any.whl
python pytentiostat/setup.py install
@pause
goto:eof

:NoPython
echo Python installation failed. Please retry.
goto:eof
