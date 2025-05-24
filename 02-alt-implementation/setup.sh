#!/bin/bash
# VideoWall Setup and Run Script
# This script provides a unified interface for setting up and running VideoWall

# Text formatting
BOLD="\033[1m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RED="\033[0;31m"
RESET="\033[0m"

# Print a section header
print_header() {
    echo -e "${BOLD}=== $1 ===${RESET}"
}

# Print a success message
print_success() {
    echo -e "${GREEN}✓ $1${RESET}"
}

# Print a warning message
print_warning() {
    echo -e "${YELLOW}⚠ $1${RESET}"
}

# Print an error message
print_error() {
    echo -e "${RED}✗ $1${RESET}"
}

# Check for conda
check_conda() {
    if ! command -v conda &> /dev/null; then
        print_error "Conda not found. Please install Miniconda or Anaconda first."
        echo "You can download it from: https://docs.conda.io/en/latest/miniconda.html"
        exit 1
    fi
    print_success "Conda found"
}

# Ensure conda environment exists or create it
ensure_environment() {
    print_header "Checking Conda Environment"
    
    # Check if videowall environment exists
    if conda env list | grep -q "videowall"; then
        print_success "Found existing 'videowall' environment"
        
        # Ask if user wants to update the environment
        read -p "Would you like to update the environment? (y/n) " -n 1 -r update_env
        echo
        
        if [[ $update_env =~ ^[Yy]$ ]]; then
            print_header "Updating Environment"
            conda env update -f environment.yml
            print_success "Environment updated"
        fi
    else
        print_warning "Environment 'videowall' not found"
        echo "Creating new conda environment 'videowall'..."
        conda env create -f environment.yml
        print_success "Environment created"
    fi
    
    # Activate the environment
    eval "$(conda shell.bash hook)"
    conda activate videowall
    
    # Install the package in development mode if not already installed
    if ! pip list | grep -q "videowall"; then
        print_header "Installing VideoWall Package"
        pip install -e .
        print_success "VideoWall package installed"
    fi
}

# Check for M3U8 playlist and copy from old location if needed
check_playlist() {
    print_header "Checking M3U8 Playlist"
    
    if [ -f "video-wall-m3u8-hosts.m3u8" ]; then
        print_success "Found M3U8 playlist file"
    else
        # Check for old configuration file
        old_m3u8="/Volumes/mpRAID/Development/Project/VideoWall/video-wall-m3u8-hosts.m3u8"
        
        if [ -f "$old_m3u8" ]; then
            print_warning "Found M3U8 playlist in old location"
            echo "Copying to the new location..."
            cp "$old_m3u8" .
            print_success "M3U8 playlist copied successfully"
        else
            print_warning "No M3U8 playlist file found"
            echo "You can still use local videos, or create a playlist file named 'video-wall-m3u8-hosts.m3u8'"
        fi
    fi
}

# Run the VideoWall application
run_videowall() {
    print_header "Running VideoWall"
    
    # Ensure the conda environment is activated
    eval "$(conda shell.bash hook)"
    conda activate videowall
    
    # Run VideoWall
    python -m videowall
}

# Build the macOS app
build_app() {
    print_header "Building macOS App"
    
    # Ensure the conda environment is activated
    eval "$(conda shell.bash hook)"
    conda activate videowall
    
    # Check for py2app
    if ! pip list | grep -q "py2app"; then
        print_warning "py2app not found, installing..."
        pip install py2app
    fi
    
    # Clean previous builds
    echo "Cleaning previous builds..."
    rm -rf build/ dist/ *.egg-info/
    
    # Building the macOS app
    echo "Building macOS app..."
    python setup.py py2app
    
    # Check if build succeeded
    if [ -d "dist/VideoWall.app" ]; then
        print_success "Build successful! App is at dist/VideoWall.app"
        
        # Open the dist folder
        open dist/
    else
        print_error "Build failed. Check errors above."
        exit 1
    fi
}

# Display help
show_help() {
    echo -e "${BOLD}VideoWall Setup and Run Script${RESET}"
    echo
    echo "Usage: $0 [option]"
    echo
    echo "Options:"
    echo "  -h, --help       Show this help message"
    echo "  -s, --setup      Set up or update the Conda environment"
    echo "  -r, --run        Run VideoWall (will set up first if needed)"
    echo "  -b, --build      Build the macOS app (will set up first if needed)"
    echo 
    echo "If no option is provided, the script will set up the environment and run VideoWall."
}

# Main script logic
main() {
    # Check for conda first
    check_conda
    
    # Handle arguments
    if [ $# -eq 0 ]; then
        # No arguments, run setup and then run the app
        ensure_environment
        check_playlist
        run_videowall
    else
        # Process arguments
        case "$1" in
            -h|--help)
                show_help
                ;;
            -s|--setup)
                ensure_environment
                check_playlist
                print_success "Setup complete!"
                ;;
            -r|--run)
                ensure_environment
                check_playlist
                run_videowall
                ;;
            -b|--build)
                ensure_environment
                check_playlist
                build_app
                ;;
            *)
                print_error "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    fi
}

# Run the main function
main "$@"