#!/bin/bash
# Build VideoWall macOS application

# Ensure we're in the project root
cd "$(dirname "$0")/.." || exit 1

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: Conda not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# Check if videowall environment exists
if ! conda env list | grep -q "videowall"; then
    echo "Error: Conda environment 'videowall' not found. Please run ./install.sh first."
    exit 1
fi

# Activate the conda environment
eval "$(conda shell.bash hook)"
conda activate videowall

# Check for py2app
if ! pip list | grep -q "py2app"; then
    echo "Installing py2app..."
    pip install py2app
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Building the macOS app
echo "Building macOS app..."
python setup.py py2app

# Check if build succeeded
if [ -d "dist/VideoWall.app" ]; then
    echo "Build successful! App is at dist/VideoWall.app"
    
    # Open the dist folder
    open dist/
else
    echo "Build failed. Check errors above."
    exit 1
fi