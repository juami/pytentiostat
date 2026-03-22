:: This batch script will install Python 3.12 and pytentiostat with all
:: necessary packages including PySide6 for the GUI.
@echo off

echo ============================================================
echo   JUAMI Pytentiostat Installer
echo ============================================================
echo.

:: Step 1 - Install Python 3.12
echo Installing Python 3.12...
cd /d "%~dp0..\local_install"
START /WAIT python-3.12.0-amd64.exe /passive InstallAllUsers=0 PrependPath=1 Include_pip=1
echo.

:: Verify Python installed correctly
python --version
if errorlevel 1 goto NoPython
echo Python installed successfully.
echo.

:: Step 2 - Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
echo.

:: Step 3 - Install runtime dependencies
echo Installing pytentiostat dependencies...
pip install pyfirmata
pip install matplotlib
pip install pyyaml
pip install pandas
pip install numpy
pip install pyserial
pip install pyside6
echo.

:: Step 4 - Install test dependencies
echo Installing test dependencies...
pip install pytest
pip install mock
echo.

:: Step 5 - Install pytentiostat
echo Installing pytentiostat...
cd /d "%~dp0.."
pip install .
echo.

echo ============================================================
echo   Installation complete!
echo.
echo   To run the pytentiostat CLI:
echo     python -m pytentiostat.main
echo.
echo   To run in simulation mode (no hardware needed):
echo     set PYTENTIOSTAT_SIMULATE=1
echo     python -m pytentiostat.main
echo ============================================================
@pause
goto :eof

:NoPython
echo.
echo Python installation failed. Please retry.
echo Make sure python-3.12.0-amd64.exe is in the local_install folder.
@pause
goto :eof
