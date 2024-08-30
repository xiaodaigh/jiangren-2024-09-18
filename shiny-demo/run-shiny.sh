#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Check if shiny is installed
if ! python3 -c "import shiny" &> /dev/null
then
    echo "Shiny for Python is not installed. Installing now..."
    pip3 install shiny
fi

# Run the Shiny app
echo "Starting the Shiny app..."
python3 shiny-demo.py
