#!/bin/bash

# Pytentiostat installer for Macbooks
ENV_NAME="pytentiostat_env"

# Check if conda is installed
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found. Please install Anaconda or Miniconda first."
    exit 1
fi

# Create a new conda environment
echo "Creating conda environment '$ENV_NAME'..."
conda create -n $ENV_NAME python=3.12 -y

# Activate the new environment
echo "Activating conda environment '$ENV_NAME'..."
source activate $ENV_NAME

# Install pytentiostat
echo "Installing pytentiostat..."
pip install pytentiostat

# Confirm installation
if pip show pytentiostat &> /dev/null; then
    echo "pytentiostat installed successfully in the '$ENV_NAME' environment."
else
    echo "Failed to install pytentiostat."
    exit 1
fi

echo "Setup complete! To activate the environment, run 'conda activate $ENV_NAME'."
