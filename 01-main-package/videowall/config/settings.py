"""
Configuration settings for VideoWall.
"""
import os

# Default grid configuration
DEFAULT_GRID_ROWS = 3
DEFAULT_GRID_COLS = 3

# Performance settings
VIDEO_BUFFER_SIZE = 8192
LOW_LATENCY_MODE = False
HARDWARE_DECODE_PRIORITY = True

# Timing configurations
ANIMATION_DURATION_MS = 8000
STREAM_CHECK_INTERVAL_MS = 30000

# Default configuration
DEFAULT_CONFIG = {
    "grid_rows": DEFAULT_GRID_ROWS,
    "grid_cols": DEFAULT_GRID_COLS,
    "use_local_videos": True,
    "skip_stream_testing": True,
    "max_active_players": 15,
}

# Resource paths
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCE_DIR = os.path.join(APP_DIR, "resources")
ICON_PATH = os.path.join(RESOURCE_DIR, "icons", "videowall.png")