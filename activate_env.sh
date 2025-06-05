#!/bin/bash
set -e

# Create and activate a virtual environment
echo "Activating virtual environment..."

# Activation command differs between Windows and Unix-like systems
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows system"
    # For Git Bash or other MSYS terminals on Windows
    .venv/Scripts/activate
elif [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Detected Cygwin on Windows"
    # For Cygwin on Windows
    source .venv/Scripts/activate
else
    echo "Detected Unix-like system (Linux/macOS)"
    # For Linux or macOS
    source .venv/bin/activate
fi