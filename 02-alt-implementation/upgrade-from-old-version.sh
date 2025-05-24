#!/bin/bash
# Upgrade script for migrating from old VideoWall version

echo "=== VideoWall Upgrade ==="
echo "This script will copy your existing M3U8 playlist to the new VideoWall installation."
echo

# Check for conda
if ! command -v conda &> /dev/null; then
    echo "Error: Conda not found. Please install Miniconda or Anaconda first."
    echo "You can download it from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Check for old configuration file
old_m3u8="/Volumes/mpRAID/Development/Project/VideoWall/video-wall-m3u8-hosts.m3u8"

if [ -f "$old_m3u8" ]; then
    echo "Found existing M3U8 playlist."
    echo "Copying to the new location..."
    cp "$old_m3u8" .
    echo "M3U8 playlist copied successfully."
else
    echo "No existing M3U8 playlist found."
    echo "You'll need to create a new playlist or copy it manually."
fi

echo
echo "Please run the install.sh script to complete the installation:"
echo "./install.sh"
echo
echo "After installation, you can run VideoWall with:"
echo "conda activate videowall"
echo "python -m videowall"
echo
echo "Or simply use the run script:"
echo "./run.sh"