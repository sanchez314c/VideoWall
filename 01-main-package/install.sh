#!/bin/bash
# VideoWall Installation Script

echo "=== VideoWall Installation ==="
echo "This script will install VideoWall and its dependencies."
echo

# Check for Python 3.7+
python_version=$(python3 --version 2>&1 | awk '{print $2}')
if [[ -z "$python_version" ]]; then
    echo "Error: Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv videowall_env

# Activate the environment
echo "Activating virtual environment..."
source videowall_env/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Install the package in development mode
echo "Installing VideoWall package..."
pip install -e .

echo
echo "Installation complete!"
echo
echo "To run VideoWall:"
echo "1. Activate the environment: source videowall_env/bin/activate"
echo "2. Run the application: python -m videowall"
echo
echo "To build the macOS app:"
echo "./scripts/build_macos_app.sh"
echo
echo "Enjoy VideoWall!"