@echo off
title BMI Calculator Pro - Professional Health Analytics

echo.
echo  ================================================================
echo           BMI CALCULATOR PRO - PROFESSIONAL EDITION
echo                Health Analytics and Management
echo                        Version 2.0 Pro
echo  ================================================================
echo.

REM Check if Python is installed
echo [*] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Error: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.7+ from: https://python.org/downloads/
    pause
    exit /b 1
)

echo [+] Python found!
python --version

echo.
echo [*] Installing dependencies...
pip install matplotlib numpy seaborn --quiet

echo.
echo [*] Launching BMI Calculator Pro...
python bmi_calculator_pro_clean.py

if errorlevel 1 (
    echo.
    echo [X] Failed to launch BMI Calculator Pro
    echo Check if all files are present in the directory
    pause
)

echo.
echo [*] Thank you for using BMI Calculator Pro!
pause