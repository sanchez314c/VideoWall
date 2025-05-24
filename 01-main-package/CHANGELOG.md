# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project restructured into proper Python package
- Proper documentation and examples
- Test suite
- macOS app build system

## [1.5.0] - 2025-05-04

### Added
- Multi-Monitor support with unique videos per screen
- Optional M3U8 stream support with local video fallback
- Can run with only local videos (no M3U8 playlist required)
- Optional local video integration via folder selection
- Recursive scanning of video folders
- 4x4 Grid layout (16 tiles)
- Random tile resizing (e.g., 2x2, 1x3) and full-screen takeover
- Discrete Random Intervals (30s/60s) for actions
- Throttled Retry Mechanism with Improved Stream Validation
- Right-arrow key for manual full refresh
- Unique stream assignment attempt
- Periodic stream health monitoring (30s)

## [1.0.0] - 2023-11-23

### Added
- Initial release with basic video wall functionality
- Basic grid layout
- Support for local video files
- Basic animation system