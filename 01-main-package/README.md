# VideoWall

Multi-Monitor Video Wall with M3U8 and Local Video Support

## Features

- Multiple monitor support with unique videos per screen
- M3U8 stream playback with local video fallback
- Can run with only local videos (no M3U8 playlist required)
- Dynamic tile layouts with smooth animations
- Grid layout with random resizing and full-screen takeover
- Automatic stream health monitoring
- macOS app compilation support
- GitHub-ready project structure

## Quick Start

### Installation

```bash
# Clone the repository (if you're using git)
git clone https://github.com/yourusername/videowall.git
cd videowall

# Run the installation script
./install.sh
```

### Running VideoWall

```bash
# Simple run script
./run.sh

# Or manually:
source videowall_env/bin/activate
python -m videowall
```

### Building macOS App

```bash
# Build a macOS .app package
./scripts/build_macos_app.sh
```

## Configuration

### M3U8 Streams

Create a file named `video-wall-m3u8-hosts.m3u8` in the project root with your stream URLs:

```
https://example.com/stream1.m3u8
https://example.com/stream2.m3u8
# Add more streams as needed
```

### Local Videos

Use the configuration dialog when starting the app to select a folder with local video files.

## Usage

- **Right Arrow Key**: Trigger a manual refresh
- **F11 or Alt+F**: Toggle fullscreen mode
- **Escape**: Exit fullscreen or quit
- **Ctrl+Q**: Quit application

## Requirements

- Python 3.7+
- PyQt5
- Working OS Multimedia Backend
- Internet connection for M3U8 streams (optional)

## Upgrading from Old Version

If you're upgrading from a previous version:

```bash
./upgrade-from-old-version.sh
```

## Documentation

For more detailed documentation, see the `docs/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original implementation by Jason Paul Michaels
- Enhanced by the community