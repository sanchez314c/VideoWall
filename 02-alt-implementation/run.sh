#!/bin/bash
# Quick run script for VideoWall using Conda

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: Conda not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# Check if videowall environment exists
if conda env list | grep -q "videowall"; then
    # Activate the environment and run VideoWall
    eval "$(conda shell.bash hook)"
    conda activate videowall
    
    # Run VideoWall
    python -m videowall
else
    echo "Conda environment 'videowall' not found. Please run ./install.sh first."
    exit 1
fi