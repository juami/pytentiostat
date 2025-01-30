@echo off
SET ENV_NAME=pytentiostat_env

REM Check if conda is installed
where conda >nul 2>nul
IF ERRORLEVEL 1 (
    echo Conda could not be found. Please install Anaconda or Miniconda first.
    exit /b 1
)

REM Create a new conda environment
echo Creating conda environment "%ENV_NAME%"...
conda create -n %ENV_NAME% python=3.12 -y

REM Activate the new environment
echo Activating conda environment "%ENV_NAME%"...
call conda activate %ENV_NAME%

REM Install pytentiostat
echo Installing pytentiostat...
pip install pytentiostat

REM Confirm installation
pip show pytentiostat >nul 2>nul
IF ERRORLEVEL 1 (
    echo Failed to install pytentiostat.
    exit /b 1
) ELSE (
    echo pytentiostat installed successfully in the "%ENV_NAME%" environment.
)

echo Setup complete! To activate the environment, run "conda activate %ENV_NAME%".
