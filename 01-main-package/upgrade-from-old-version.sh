#!/bin/bash
# Upgrade script for migrating from old VideoWall version

echo "=== VideoWall Upgrade ==="
echo "This script will copy your existing M3U8 playlist to the new VideoWall installation."
echo

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
echo "source videowall_env/bin/activate"
echo "python -m videowall"