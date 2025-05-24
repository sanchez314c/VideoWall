#!/bin/bash
# Quick run script for VideoWall

# Check if virtual environment exists
if [ -d "videowall_env" ]; then
    # Activate the environment
    source videowall_env/bin/activate
    
    # Run VideoWall
    python -m videowall
else
    echo "Virtual environment not found. Please run ./install.sh first."
    exit 1
fi