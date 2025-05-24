"""
Setup configuration for VideoWall.
"""
from setuptools import setup, find_packages
import os
import sys

# Read version from package
with open(os.path.join("videowall", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"\'')
            break

# Additional py2app configuration for macOS
if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=['videowall/__main__.py'],
        options=dict(
            py2app=dict(
                iconfile='videowall/resources/icons/videowall.icns',
                plist=dict(
                    CFBundleName="VideoWall",
                    CFBundleDisplayName="VideoWall",
                    CFBundleGetInfoString="Multi-Monitor Video Wall",
                    CFBundleIdentifier="com.jasonpaulmichaels.videowall",
                    CFBundleVersion=version,
                    CFBundleShortVersionString=version,
                    NSHumanReadableCopyright="Copyright © 2025 Jason Paul Michaels",
                    NSHighResolutionCapable=True,
                ),
                packages=['PyQt5'],
                includes=['sip'],
                excludes=['PyQt5.QtWebEngine', 'numpy', 'scipy'],
                resources=['videowall/resources'],
            ),
        ),
    )
else:
    extra_options = dict()

setup(
    name="videowall",
    version=version,
    description="Multi-Monitor Video Wall with M3U8 and Local Video Support",
    author="Jason Paul Michaels",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/videowall",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5>=5.15.0",
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "videowall=videowall.core.app:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Multimedia :: Video :: Display",
    ],
    **extra_options
)