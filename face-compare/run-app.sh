#!/bin/bash

# Check if Streamlit is installed
if ! command -v streamlit &> /dev/null
then
    echo "Streamlit is not installed. Please install it using: pip install streamlit"
    exit 1
fi

# Check if the face-compare-st.py file exists
if [ ! -f "face-compare-st.py" ]; then
    echo "Error: face-compare-st.py not found in the current directory."
    exit 1
fi

# Run the Streamlit app
echo "Launching Face Comparison App..."
streamlit run face-compare-st.py
