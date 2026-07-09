#!/bin/bash


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "---> Checking for system graphics libraries (Cairo)..."
    # If cairo is missing, prompt the user to install it
    if ! pkg-config --exists cairo; then
        echo "Error: Missing 'libcairo2-dev'. Please run:"
        echo "sudo apt update && sudo apt install libcairo2-dev pkg-config python3-dev"
        echo "You might be missing the Cairo graphics library."
        echo "If you have Homebrew, run: brew install cairo pkg-config"
        echo "-------------------------------------------------------"
        exit 1
    fi
echo "---> Setting up virtual environment..."
python3 -m venv .venv

echo "---> Installing cmu-graphics (this may take a minute)..."
./.venv/bin/python3 -m pip install --upgrade pip
./.venv/bin/python3 -m pip install cmu-graphics


if [ -f "main.py" ]; then
    echo "---> Launching Memory Game..."
    ./.venv/bin/python3 main.py
else
    echo "Error: main.py not found!"
fi
