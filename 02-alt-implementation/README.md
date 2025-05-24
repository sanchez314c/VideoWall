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

### Prerequisites

- Miniconda or Anaconda installed (download from [here](https://docs.conda.io/en/latest/miniconda.html))

### Installation and Running

Use the unified setup script to install, update, and run VideoWall:

```bash
# Clone the repository (if you're using git)
git clone https://github.com/yourusername/videowall.git
cd videowall

# Run the setup script (sets up environment and runs the app)
./setup.sh

# Show available options
./setup.sh --help
```

The setup script provides the following options:
- `./setup.sh -s` or `./setup.sh --setup`: Set up or update the Conda environment
- `./setup.sh -r` or `./setup.sh --run`: Run VideoWall (will set up first if needed)
- `./setup.sh -b` or `./setup.sh --build`: Build the macOS app (will set up first if needed)

### Alternative Run Methods

```bash
# Simple run script (if environment is already set up)
./run.sh

# Or manually:
conda activate videowall
python -m videowall
```

### Building macOS App

```bash
# Using the setup script (recommended)
./setup.sh --build

# Or manually:
conda activate videowall
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

- Python 3.7+ (installed via Conda)
- PyQt5
- Working OS Multimedia Backend
- Internet connection for M3U8 streams (optional)

## Upgrading from Old Version

If you're upgrading from a previous version:

```bash
# Using the setup script (recommended)
./setup.sh --setup

# Or using the dedicated upgrade script
./upgrade-from-old-version.sh
```

## Documentation

For more detailed documentation, see the `docs/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original implementation by Jason Paul Michaels
- Enhanced by the community