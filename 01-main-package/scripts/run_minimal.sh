#!/bin/bash
# Run VideoWall with minimal configuration

# Activate the Python environment if using virtual environments
# Uncomment and modify if needed:
# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate videowall_env

# Set GStreamer environment variables for macOS if needed
if [[ "$OSTYPE" == "darwin"* ]]; then
  export GST_PLUGIN_PATH="/Library/Frameworks/GStreamer.framework/Libraries/GStreamer/gstreamer-1.0"
  export GST_DEBUG=1  # Minimal logging
fi

# Run the application as a module
echo "Starting VideoWall..."
python -m videowall