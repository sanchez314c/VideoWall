#!/bin/bash
# Build VideoWall macOS application

# Ensure we're in the project root
cd "$(dirname "$0")/.." || exit 1

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