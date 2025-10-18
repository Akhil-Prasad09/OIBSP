@echo off
title Advanced Password Generator - Oasis Infobyte

echo ╔══════════════════════════════════════════════════════════════╗
echo ║           🔐 Advanced Password Generator 🔐                  ║
echo ║              Oasis Infobyte Internship Project              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo Installing required dependencies...
pip install pyperclip --quiet

echo.
echo Starting Advanced Password Generator...
echo.

python password_generator.py

echo.
echo Application closed.
pause