@echo off
title BMI Calculator Pro - Professional Health Analytics
color 0B

echo.
echo  ================================================================
echo           BMI CALCULATOR PRO - PROFESSIONAL EDITION
echo                Health Analytics and Management
echo                        Version 2.0 Pro
echo  ================================================================
echo.

REM Check if Python is installed
echo [*] Checking system requirements...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Error: Python is not installed or not in PATH
    echo.
    echo [!] Please download and install Python 3.7+ from:
    echo    https://python.org/downloads/
    echo.
    echo [!] IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [+] Python detected: 
python --version
echo.

REM Check if required packages are installed
echo [*] Checking dependencies...
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo [!] Installing required dependencies...
    echo.
    echo Installing matplotlib (for data visualization)...
    pip install matplotlib
    if errorlevel 1 (
        echo [X] Failed to install matplotlib
        pause
        exit /b 1
    )
    
    echo Installing numpy (for calculations)...
    pip install numpy
    if errorlevel 1 (
        echo [X] Failed to install numpy
        pause
        exit /b 1
    )
    
    echo Installing seaborn (for enhanced plots)...
    pip install seaborn
    if errorlevel 1 (
        echo [X] Failed to install seaborn
        pause
        exit /b 1
    )
    
    echo [+] Dependencies installed successfully!
    echo.
)

echo [*] Launching BMI Calculator Pro...
echo.

REM Launch the main application
python "%~dp0bmi_calculator_pro.py"

REM If application fails, show error
if errorlevel 1 (
    echo.
    echo [X] Failed to launch BMI Calculator Pro
    echo Please check if all files are present in the directory
    echo.
    echo Required files:
    echo - bmi_calculator_pro.py
    echo - bmi_engine.py
    echo.
    pause
)

echo.
echo [*] Thank you for using BMI Calculator Pro!
echo Your health data is safely stored locally.
pause