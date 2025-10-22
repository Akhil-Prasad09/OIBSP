@echo off
echo ========================================
echo   Weather Pro - Starting Application
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo Checking dependencies...
pip show requests >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install -r requirements.txt
    echo.
)

REM Check if config file exists
if not exist config.json (
    echo WARNING: config.json not found!
    echo Please create config.json with your API key.
    echo See README.md for instructions.
    echo.
    pause
)

REM Run the application
echo Starting Weather Pro...
echo.
python weather_app.py

if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    pause
)
