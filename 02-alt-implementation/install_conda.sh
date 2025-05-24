#!/bin/bash
# VideoWall Installation Script using conda env file

echo "=== VideoWall Installation ==="
echo "This script will install VideoWall and its dependencies using Conda."
echo

# Check for conda
if ! command -v conda &> /dev/null; then
    echo "Error: Conda not found. Please install Miniconda or Anaconda first."
    echo "You can download it from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Create a conda environment from environment.yml
echo "Creating conda environment 'videowall' from environment.yml..."
conda env create -f environment.yml
echo

# Activate the environment
echo "Activating conda environment..."
eval "$(conda shell.bash hook)"
conda activate videowall

# Install the package in development mode
echo "Installing VideoWall package..."
pip install -e .

echo
echo "Installation complete!"
echo
echo "To run VideoWall:"
echo "1. Activate the environment: conda activate videowall"
echo "2. Run the application: python -m videowall"
echo
echo "Or use the run script: ./run.sh"
echo
echo "To build the macOS app:"
echo "conda activate videowall"
echo "./scripts/build_macos_app.sh"
echo
echo "Enjoy VideoWall!"