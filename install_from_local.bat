:: This batch script will install python 3.8, pytentiostat and it's necessary packages

echo Installing python
START /WAIT python-3.8.1-amd64
echo next step
pip install cycler-0.10.0-py2.py3-none-any.whl
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
pip install matplotlib-3.1.2-cp38-cp38-win_amd64.whl
