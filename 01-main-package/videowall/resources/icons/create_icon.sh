#!/bin/bash
# Script to generate VideoWall icon

# Check for ImageMagick
if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is required. Please install it first."
    echo "Typically: brew install imagemagick"
    exit 1
fi

# Create a simple video wall icon
convert -size 1024x1024 \
    -background black \
    -fill blue -draw "rectangle 10,10 500,500" \
    -fill red -draw "rectangle 510,10 1000,500" \
    -fill green -draw "rectangle 10,510 500,1000" \
    -fill orange -draw "rectangle 510,510 1000,1000" \
    -fill white -gravity center -pointsize 120 -annotate 0 "VideoWall" \
    videowall.png

echo "Created videowall.png icon"

# Create icon set for macOS
mkdir -p VideoWall.iconset
convert videowall.png -resize 16x16 VideoWall.iconset/icon_16x16.png
convert videowall.png -resize 32x32 VideoWall.iconset/icon_16x16@2x.png
convert videowall.png -resize 32x32 VideoWall.iconset/icon_32x32.png
convert videowall.png -resize 64x64 VideoWall.iconset/icon_32x32@2x.png
convert videowall.png -resize 128x128 VideoWall.iconset/icon_128x128.png
convert videowall.png -resize 256x256 VideoWall.iconset/icon_128x128@2x.png
convert videowall.png -resize 256x256 VideoWall.iconset/icon_256x256.png
convert videowall.png -resize 512x512 VideoWall.iconset/icon_256x256@2x.png
convert videowall.png -resize 512x512 VideoWall.iconset/icon_512x512.png
convert videowall.png -resize 1024x1024 VideoWall.iconset/icon_512x512@2x.png

# Create icns file
if command -v iconutil &> /dev/null; then
    iconutil -c icns VideoWall.iconset
    echo "Created VideoWall.icns icon"
    mv VideoWall.icns videowall.icns
else
    echo "Warning: iconutil not found. Cannot create .icns file."
    echo "You can create it manually on macOS using the generated iconset."
fi

# Clean up
rm -rf VideoWall.iconset
echo "Done!"