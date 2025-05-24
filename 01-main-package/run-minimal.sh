#!/bin/bash
# Run VideoWall with minimal configuration

# Activate the Python 3.9 environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate base_39

# Set GStreamer environment variables
export GST_PLUGIN_PATH="/Library/Frameworks/GStreamer.framework/Libraries/GStreamer/gstreamer-1.0"
export GST_DEBUG=1  # Minimal logging

# Run the application
echo "Starting VideoWall from Python 3.9 environment..."
python /Volumes/mpRAID/Apps/VideoWall/fixed-video-wall.py