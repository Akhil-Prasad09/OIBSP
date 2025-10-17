#!/bin/bash
# BMI Calculator Pro - Setup Script for Unix-like systems (macOS, Linux)

echo "================================================================"
echo "          BMI CALCULATOR PRO - PROFESSIONAL EDITION"
echo "               Health Analytics and Management"
echo "                        Version 2.0 Pro"
echo "================================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
echo -e "${BLUE}[*]${NC} Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo -e "${RED}[X]${NC} Error: Python is not installed or not in PATH"
    echo ""
    echo -e "${YELLOW}[!]${NC} Please install Python 3.7+ from: https://python.org/downloads/"
    echo -e "${YELLOW}[!]${NC} Or use your system package manager:"
    echo "    macOS: brew install python"
    echo "    Ubuntu/Debian: sudo apt install python3 python3-pip python3-tk"
    echo "    CentOS/RHEL: sudo yum install python3 python3-pip tkinter"
    echo ""
    exit 1
fi

echo -e "${GREEN}[+]${NC} Python found!"
$PYTHON_CMD --version
echo ""

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
MIN_VERSION="3.7"

if [ "$(printf '%s\n' "$MIN_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$MIN_VERSION" ]; then
    echo -e "${RED}[X]${NC} Error: Python $PYTHON_VERSION is installed, but Python $MIN_VERSION or higher is required"
    exit 1
fi

# Check if pip is available
echo -e "${BLUE}[*]${NC} Checking pip..."
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo -e "${RED}[X]${NC} Error: pip is not installed"
    echo -e "${YELLOW}[!]${NC} Please install pip first"
    exit 1
fi

# Determine pip command
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
else
    PIP_CMD="pip"
fi

# Install dependencies
echo -e "${BLUE}[*]${NC} Installing dependencies..."
$PIP_CMD install --user matplotlib numpy seaborn

if [ $? -ne 0 ]; then
    echo -e "${RED}[X]${NC} Failed to install dependencies"
    echo -e "${YELLOW}[!]${NC} Try running: $PIP_CMD install --user -r requirements.txt"
    exit 1
fi

echo -e "${GREEN}[+]${NC} Dependencies installed successfully!"
echo ""

# Check if tkinter is available (for GUI)
echo -e "${BLUE}[*]${NC} Checking GUI support..."
if $PYTHON_CMD -c "import tkinter" 2>/dev/null; then
    echo -e "${GREEN}[+]${NC} GUI support available"
else
    echo -e "${YELLOW}[!]${NC} Warning: tkinter not found. Install python3-tk package:"
    echo "    Ubuntu/Debian: sudo apt install python3-tk"
    echo "    CentOS/RHEL: sudo yum install tkinter"
    echo "    macOS: Should be included with Python"
fi
echo ""

# Make the script executable
chmod +x "$0"

echo -e "${BLUE}[*]${NC} Setup complete! You can now run the application:"
echo ""
echo "  $PYTHON_CMD bmi_calculator_pro_clean.py"
echo ""
echo -e "${GREEN}[*]${NC} Thank you for using BMI Calculator Pro!"
echo ""