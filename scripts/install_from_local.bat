:: Offline installer for pytentiostat.
::
:: Run this on the target (offline) Windows machine after the USB flash drive
:: has been prepared on an internet-connected machine with:
::     python scripts/build_local_install.py
:: It installs Python (from a bundled installer if needed), creates a virtual
:: environment, and installs pytentiostat plus its dependencies from the
:: bundled wheels in local-install/whls -- no internet access required.
@echo off
setlocal enabledelayedexpansion

set "HERE=%~dp0"
set "WHLS=%HERE%..\local-install\whls"
set "VENV=%HERE%..\pytentiostat-env"

echo ==================================================
echo  Installing pytentiostat (offline)
echo ==================================================

:: 1. Make sure Python is available; offer the bundled installer if not.
python --version >nul 2>&1
if not errorlevel 1 goto have_python

echo Python was not found on PATH.
set "PYEXE="
for %%f in ("%HERE%..\local-install\python-*.exe") do set "PYEXE=%%f"
if not defined PYEXE goto no_python
echo Launching bundled Python installer: !PYEXE!
echo IMPORTANT: tick "Add Python to PATH" on the first screen.
start /wait "" "!PYEXE!"

python --version >nul 2>&1
if errorlevel 1 goto path_refresh

:have_python
:: 2. Check that the wheels were staged onto the USB.
if not exist "%WHLS%" goto no_wheels

:: 3. Create an isolated virtual environment for pytentiostat.
echo Creating virtual environment at "%VENV%"...
python -m venv "%VENV%"
if errorlevel 1 goto venv_failed

:: 4. Install pytentiostat and all dependencies offline from local wheels.
echo Installing pytentiostat and dependencies from local wheels...
"%VENV%\Scripts\python" -m pip install --no-index --find-links "%WHLS%" pytentiostat
if errorlevel 1 goto install_failed

echo.
echo ==================================================
echo  Success! pytentiostat is installed.
echo  Activate the environment with:
echo      "%VENV%\Scripts\activate"
echo  then run:  pytentiostat
echo ==================================================
pause
goto end

:no_python
echo No bundled Python installer (local-install\python-*.exe) was found.
echo Please install Python 3.12 manually, then re-run this script.
pause
goto end

:path_refresh
echo Python was installed but is not on PATH yet.
echo Close this window, open a new terminal, and run this script again.
pause
goto end

:no_wheels
echo Could not find wheels at "%WHLS%".
echo Run "python scripts\build_local_install.py" on an internet-connected
echo machine first to populate the USB, then try again.
pause
goto end

:venv_failed
echo Failed to create the virtual environment.
pause
goto end

:install_failed
echo Offline install failed. Check that the wheels match this machine's
echo Python version and architecture.
pause
goto end

:end
endlocal
