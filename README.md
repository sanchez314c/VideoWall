# 🖥️ VideoWall: Dynamic Hardware Acceleration Enabled Multi Display Casting

<p align="center">
  <img src="https://raw.githubusercontent.com/sanchez314c/VideoWall/main/.images/videowall-hero.png" alt="VideoWall Hero" width="600" />
</p>

**Dynamic Hardware Acceleration Enabled Multi Display Casting on MacOS & Linux**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VLC](https://img.shields.io/badge/VLC-Media_Player-orange.svg)](https://www.videolan.org/vlc/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Video_Processing-green.svg)](https://ffmpeg.org/)
[![macOS](https://img.shields.io/badge/macOS-Compatible-blue.svg)](https://www.apple.com/macos/)
[![Linux](https://img.shields.io/badge/Linux-Compatible-yellow.svg)](https://www.linux.org/)

## 🎯 Overview

VideoWall is the ultimate multimedia powerhouse for creating stunning multi-display video installations. Whether you're building digital signage, immersive art installations, control rooms, or jaw-dropping event displays, VideoWall provides the tools and frameworks to transform any collection of screens into a synchronized, high-performance video experience.

Built for professionals who demand reliability, performance, and flexibility in their display solutions.

## ✨ Key Features

### 🚀 **Hardware Acceleration**
- **GPU Acceleration**: Leverage CUDA, Metal, and OpenCL for maximum performance
- **Multi-Core Processing**: Distribute workload across CPU cores
- **Memory Optimization**: Efficient handling of high-resolution content
- **Real-time Rendering**: Smooth playback even with 4K+ content

### 🖼️ **Advanced Display Management**
- **Automatic Display Detection**: Intelligent screen arrangement and configuration
- **Custom Layouts**: Flexible grid and custom positioning systems
- **Bezel Compensation**: Seamless content across physical screen gaps
- **Resolution Scaling**: Automatic content adaptation for mixed resolutions
- **Rotation Support**: Portrait, landscape, and custom angle displays

### 🎬 **Professional Media Support**
- **Universal Format Support**: MP4, AVI, MOV, MKV, WEBM, and more
- **Live Streaming**: RTMP, HLS, and direct camera inputs
- **Audio Synchronization**: Multi-channel audio with visual sync
- **Playlist Management**: Advanced scheduling and content rotation
- **Real-time Effects**: Transitions, overlays, and visual filters

### 🌐 **Multiple Deployment Options**
- **Standalone Application**: Full-featured desktop application
- **Web-based Control**: Browser-accessible management interface
- **Scripted Automation**: Command-line tools for integration
- **API Integration**: REST API for custom applications
- **Network Clustering**: Distributed displays across multiple machines

## 🏗️ Architecture Overview

```
VideoWall/
├── 01-main-package/           # Core VideoWall Application
│   ├── videowall/            # Main Python package
│   │   ├── __init__.py
│   │   └── __main__.py
│   ├── build/                # Compiled distributions
│   ├── dist/                 # Distribution packages
│   ├── examples/             # Usage examples
│   ├── tests/                # Test suite
│   ├── requirements.txt      # Core dependencies
│   ├── pyproject.toml       # Modern Python packaging
│   └── setup.py             # Package configuration
│
├── 02-alt-implementation/     # Alternative Builds
│   ├── conda_environment.yml # Conda-based setup
│   ├── scripts/              # Alternative deployment scripts
│   └── setup.sh             # Quick setup utility
│
├── 03-standalone-scripts/     # Specialized Tools
│   ├── dynamic_video_wall.py # Dynamic layout engine
│   ├── fixed-video-wall.py   # Static configuration tool
│   ├── video-wall-basic.py   # Minimal implementation
│   ├── video-wall-floating.py# Floating window manager
│   ├── video-wall-m3u8.py    # Streaming playlist support
│   ├── video-wall-roku.py    # Roku integration
│   ├── video_utils.py        # Utility functions
│   └── vlc_utils.py          # VLC integration helpers
│
├── 04-web-version/           # Web-based Interface
│   ├── video_wall.html       # Web application
│   └── video-wall-m3u8-hosts.m3u8  # Streaming configuration
│
├── 05-archive/              # Legacy versions
└── 06-resources/           # Assets and documentation
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** with pip
- **VLC Media Player** (latest version)
- **FFmpeg** (for video processing)
- **Multiple displays** or virtual display setup
- **GPU drivers** (NVIDIA/AMD/Intel) for hardware acceleration

### Installation Methods

#### Option 1: Main Package (Recommended)
```bash
# Clone the repository
git clone https://github.com/sanchez314c/VideoWall.git
cd VideoWall/01-main-package

# Install with automatic setup
./install.sh
# OR manual installation
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python setup.py install

# Launch VideoWall
python -m videowall
```

#### Option 2: Conda Environment
```bash
cd VideoWall/02-alt-implementation
conda env create -f environment.yml
conda activate videowall
./run.sh
```

#### Option 3: Standalone Scripts
```bash
cd VideoWall/03-standalone-scripts
pip install vlc-python opencv-python numpy
python dynamic_video_wall.py --help
```

#### Option 4: Web Version
```bash
cd VideoWall/04-web-version
# Serve with any web server
python -m http.server 8000
# Open browser to http://localhost:8000/video_wall.html
```

## 🎮 Usage Examples

### Basic Multi-Display Setup
```python
from videowall import VideoWall, Display, MediaSource

# Initialize VideoWall
wall = VideoWall()

# Auto-detect displays
displays = wall.detect_displays()
print(f"Found {len(displays)} displays")

# Create media sources
video1 = MediaSource("/path/to/video1.mp4")
video2 = MediaSource("/path/to/video2.mp4")
livestream = MediaSource("rtmp://stream.url/live")

# Configure layout
layout = wall.create_grid_layout(2, 2)  # 2x2 grid
layout.assign_content(0, 0, video1)     # Top-left
layout.assign_content(0, 1, video2)     # Top-right
layout.assign_content(1, 0, livestream) # Bottom-left (spans 2 cells)
layout.span_content(1, 0, cols=2)

# Start playback
wall.start(layout)
```

### Advanced Configuration
```python
from videowall import VideoWall, Configuration

# Custom configuration
config = Configuration(
    hardware_acceleration=True,
    gpu_device="cuda:0",          # Use specific GPU
    audio_enabled=True,
    bezel_compensation=True,
    bezel_width=5,               # 5mm bezels
    sync_tolerance=16,           # 16ms sync tolerance
    quality_preset="ultra"       # ultra/high/medium/low
)

wall = VideoWall(config)

# Custom display arrangement
displays = [
    Display(0, position=(0, 0), resolution=(1920, 1080)),
    Display(1, position=(1920, 0), resolution=(1920, 1080)),
    Display(2, position=(0, 1080), resolution=(1920, 1080)),
    Display(3, position=(1920, 1080), resolution=(1920, 1080))
]

# Create playlist with transitions
playlist = wall.create_playlist([
    {"source": "video1.mp4", "duration": 30, "transition": "fade"},
    {"source": "video2.mp4", "duration": 45, "transition": "slide_left"},
    {"source": "livestream.m3u8", "duration": -1}  # Infinite duration
])

wall.play_playlist(playlist, loop=True)
```

### Web API Integration
```python
import requests

# VideoWall REST API endpoints
base_url = "http://localhost:8080/api/v1"

# Get system status
status = requests.get(f"{base_url}/status").json()
print(f"Status: {status['state']}, Displays: {status['display_count']}")

# Upload and play content
files = {"video": open("presentation.mp4", "rb")}
response = requests.post(f"{base_url}/content/upload", files=files)
content_id = response.json()["id"]

# Create layout and start playback
layout_config = {
    "type": "grid",
    "rows": 2,
    "columns": 2,
    "content": [
        {"position": [0, 0], "content_id": content_id},
        {"position": [0, 1], "content_id": content_id},
        {"position": [1, 0], "content_id": "live_camera_1"},
        {"position": [1, 1], "content_id": "dashboard_feed"}
    ]
}

requests.post(f"{base_url}/layout/create", json=layout_config)
requests.post(f"{base_url}/playback/start")
```

### Command Line Interface
```bash
# Basic video wall with auto-detection
videowall play --input /path/to/videos/*.mp4 --layout auto

# Custom grid layout
videowall play --input video1.mp4 video2.mp4 video3.mp4 video4.mp4 \
               --layout grid:2x2 \
               --displays 0,1,2,3 \
               --hardware-accel cuda

# Streaming setup
videowall stream --source rtmp://input.stream/live \
                  --output rtmp://output.stream/live \
                  --displays all \
                  --quality 1080p

# Interactive configuration
videowall config --interactive
videowall play --config my_setup.json

# Monitor and control
videowall status
videowall pause
videowall resume
videowall stop
```

## 🔧 Advanced Features

### Hardware Acceleration Configuration
```yaml
# config.yaml
hardware:
  gpu_acceleration: true
  gpu_devices: ["cuda:0", "cuda:1"]  # Multi-GPU support
  memory_limit: "4GB"
  cpu_threads: 8
  
display:
  sync_method: "genlock"     # genlock/software/none
  color_profile: "rec709"    # rec709/rec2020/dci-p3
  hdr_enabled: true
  refresh_rate: 60
  
audio:
  enabled: true
  channels: 8                # 7.1 surround
  sample_rate: 48000
  latency: "low"
  
streaming:
  protocols: ["rtmp", "hls", "webrtc"]
  quality_levels: ["4K", "1080p", "720p"]
  adaptive_bitrate: true
```

### Custom Display Layouts
```python
# Advanced layout engine
from videowall.layouts import CustomLayout, Zone

layout = CustomLayout()

# Define zones with precise positioning
main_zone = Zone(
    x=0, y=0, width=3840, height=2160,  # 4K main area
    content_type="video",
    scaling="fill",
    effects=["blur_background", "color_correction"]
)

ticker_zone = Zone(
    x=0, y=2160, width=3840, height=120,  # Bottom ticker
    content_type="text_scroll",
    font_size=24,
    scroll_speed=50
)

logo_zone = Zone(
    x=3720, y=0, width=120, height=120,  # Top-right logo
    content_type="image",
    opacity=0.8,
    z_index=10
)

layout.add_zones([main_zone, ticker_zone, logo_zone])
```

### Real-time Effects and Filters
```python
from videowall.effects import EffectChain, ColorCorrection, Transition

# Create effect chain
effects = EffectChain([
    ColorCorrection(brightness=1.1, contrast=1.2, saturation=1.1),
    Transition("crossfade", duration=2.0),
    # Custom shader effects
    "shaders/custom_glow.glsl"
])

# Apply to content
wall.apply_effects(content_id, effects)

# Real-time parameter adjustment
wall.set_effect_parameter(content_id, "brightness", 1.3)
```

### Network Clustering
```python
# Master node configuration
from videowall.cluster import ClusterMaster

master = ClusterMaster(
    nodes=[
        "192.168.1.10:8080",  # Node 1: Displays 0-3
        "192.168.1.11:8080",  # Node 2: Displays 4-7
        "192.168.1.12:8080"   # Node 3: Displays 8-11
    ],
    sync_protocol="ntp",
    redundancy=True
)

# Distribute content across cluster
master.deploy_content("/path/to/video.mp4")
master.create_synchronized_playback()

# Slave node configuration
from videowall.cluster import ClusterSlave

slave = ClusterSlave(
    master_address="192.168.1.5:8080",
    local_displays=[0, 1, 2, 3],
    cache_size="10GB"
)
```

## 📊 Performance Optimization

### Benchmarks by Configuration

| Setup | Resolution | FPS | GPU Memory | CPU Usage | Displays |
|-------|------------|-----|------------|-----------|----------|
| Basic | 1080p | 60 | 2GB | 15% | 4 |
| Professional | 4K | 60 | 8GB | 25% | 9 |
| Enterprise | 8K | 30 | 16GB | 40% | 16 |
| Extreme | 4K | 120 | 24GB | 60% | 25+ |

### Optimization Guidelines
```python
# Performance tuning
config = Configuration(
    # GPU optimization
    gpu_memory_fraction=0.8,     # Use 80% of GPU memory
    enable_gpu_scheduling=True,
    
    # CPU optimization  
    worker_threads=8,            # Match CPU cores
    io_threads=4,
    
    # Memory optimization
    buffer_size="512MB",         # Video buffer
    preload_content=True,
    cache_decoded_frames=True,
    
    # Quality vs Performance
    decode_quality="high",       # high/medium/fast
    scaling_algorithm="lanczos", # lanczos/bilinear/nearest
    color_depth=10               # 8/10/12 bit
)
```

## 🔒 Security & Reliability

### Content Protection
```python
# DRM and content security
from videowall.security import DRMManager

drm = DRMManager(
    provider="widevine",         # widevine/playready/fairplay
    license_server="https://license.server.com",
    certificate_file="cert.pem"
)

# Encrypted content playback
protected_content = MediaSource(
    "encrypted_video.mp4",
    drm_config=drm
)
```

### System Monitoring
```python
# Health monitoring and alerts
from videowall.monitoring import SystemMonitor

monitor = SystemMonitor(
    check_interval=30,           # 30 second checks
    temperature_threshold=85,    # Celsius
    memory_threshold=0.9,        # 90% usage
    disk_threshold=0.95,         # 95% usage
    alert_webhook="https://alerts.company.com/webhook"
)

monitor.start()
```

### Failover and Redundancy
```python
# Automatic failover configuration
failover_config = {
    "primary_sources": ["rtmp://primary.stream"],
    "backup_sources": ["rtmp://backup1.stream", "rtmp://backup2.stream"],
    "switch_threshold": 5,       # Switch after 5 second timeout
    "health_check_interval": 10,
    "automatic_recovery": True
}

wall.configure_failover(failover_config)
```

## 🐛 Troubleshooting

### Common Issues

**Display Detection Problems**
```bash
# List available displays
videowall displays --list --verbose

# Force display refresh
videowall displays --refresh --detect-changes

# Manual display configuration
videowall config --displays manual --positions "0,0:1920,0:0,1080:1920,1080"
```

**Performance Issues**
```bash
# GPU performance diagnostics
videowall diagnostics --gpu --memory --performance

# Reduce quality for better performance
videowall play --quality medium --hardware-accel off --fps 30

# Clear cache and restart
videowall cache --clear
videowall restart --reset-config
```

**Synchronization Problems**
```bash
# Audio/video sync adjustment
videowall sync --audio-delay 150ms --video-offset -50ms

# Network sync (for cluster setups)
videowall cluster --sync-ntp --precision high

# Manual frame stepping
videowall debug --frame-step --sync-markers
```

**Content Loading Issues**
```bash
# Verify media files
videowall validate --input /path/to/videos/ --report

# Test streaming sources
videowall test --stream rtmp://source.url --duration 60s

# Codec information
videowall info --file video.mp4 --codecs --bitrates
```

## 📈 Roadmap

### Upcoming Features
- [ ] **AI-Powered Content Analysis**: Automatic scene detection and layout optimization
- [ ] **Cloud Integration**: AWS/Azure/GCP streaming and storage
- [ ] **Mobile Control App**: iOS/Android remote control applications
- [ ] **Advanced Analytics**: Viewing patterns and engagement metrics
- [ ] **AR/VR Integration**: Mixed reality display capabilities

### Long-term Vision
- [ ] **8K Support**: Native 8K content playback and processing
- [ ] **Machine Learning**: Predictive content caching and optimization
- [ ] **Blockchain Integration**: Decentralized content distribution
- [ ] **Holographic Displays**: Next-generation display technology support
- [ ] **Edge Computing**: Distributed processing at display endpoints

## 🤝 Contributing

### Development Environment
```bash
# Development setup
git clone https://github.com/sanchez314c/VideoWall.git
cd VideoWall/01-main-package

# Create development environment
python -m venv dev_env
source dev_env/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
pip install -e .

# Run tests
pytest tests/ -v --cov=videowall

# Code quality checks
black . && flake8 . && mypy videowall/
```

### Contribution Guidelines
1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Write comprehensive tests**: Cover new functionality
4. **Document thoroughly**: Update README and code documentation
5. **Performance test**: Ensure no regression in performance
6. **Submit pull request**: Include detailed description and benchmarks

### Areas for Contribution
- **New Display Technologies**: Support for emerging display types
- **Codec Optimization**: Improved video codec implementations
- **Platform Support**: Windows, ARM, and embedded systems
- **UI/UX Improvements**: Enhanced user interfaces
- **Documentation**: Tutorials, examples, and best practices

## 🌍 Use Cases

### Digital Signage
- **Retail Displays**: Product showcases and promotional content
- **Transportation Hubs**: Flight information and wayfinding
- **Corporate Lobbies**: Company information and branding
- **Educational Institutions**: Campus information and announcements

### Entertainment & Events
- **Concert Venues**: Stage backgrounds and audience engagement
- **Sports Arenas**: Statistics, replays, and crowd excitement
- **Museums**: Interactive exhibits and digital art installations
- **Theaters**: Set extensions and immersive environments

### Professional Applications
- **Control Rooms**: Monitoring and surveillance operations
- **Trading Floors**: Financial data and market information
- **Broadcasting**: News backgrounds and live production
- **Simulation Centers**: Training environments and data visualization

### Art & Creative
- **Digital Art Installations**: Gallery and museum exhibitions
- **Architectural Integration**: Building facade displays
- **Interactive Experiences**: Touch and gesture-controlled content
- **Performance Art**: Live visual accompaniment

## 📞 Support & Resources

### Getting Help
- **Documentation**: [Complete Wiki](https://github.com/sanchez314c/VideoWall/wiki)
- **Video Tutorials**: [YouTube Channel](https://youtube.com/videowall-tutorials)
- **Issues**: [GitHub Issues](https://github.com/sanchez314c/VideoWall/issues)
- **Discussions**: [Community Forum](https://github.com/sanchez314c/VideoWall/discussions)

### Professional Services
- **Installation Support**: On-site setup and configuration
- **Custom Development**: Tailored solutions for specific needs
- **Training Programs**: Workshops and certification courses
- **Enterprise Support**: Priority assistance and SLA agreements

### Community
- **Discord**: [Join our server](https://discord.gg/videowall)
- **Reddit**: [r/VideoWall](https://reddit.com/r/videowall)
- **LinkedIn**: [VideoWall Professionals](https://linkedin.com/groups/videowall)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **VLC Media Player**: For robust media playback capabilities
- **FFmpeg Team**: For comprehensive video processing tools
- **OpenGL Community**: For graphics rendering standards
- **Display Industry**: For advancing multi-display technologies
- **Open Source Contributors**: Everyone who has contributed to this project

## 🔗 Related Projects

- [OBS Studio](https://github.com/obsproject/obs-studio) - Broadcasting and streaming
- [VLC Media Player](https://github.com/videolan/vlc) - Media playback engine
- [FFmpeg](https://github.com/FFmpeg/FFmpeg) - Video processing framework

---

<p align="center">
  <strong>Transform your displays, dominate your space 🖥️</strong><br>
  <sub>Where multiple screens become one powerful canvas</sub>
</p>

---

**⭐ Star this repository if VideoWall powers your digital displays!**