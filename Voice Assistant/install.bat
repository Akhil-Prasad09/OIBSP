@echo off
echo ====================================
echo Voice Assistant Setup Script
echo ====================================
echo.

echo Installing required packages...
echo.

REM Upgrade pip first
python -m pip install --upgrade pip

REM Install packages from requirements.txt
echo Installing dependencies...
pip install -r requirements.txt

REM Try to install PyAudio using pipwin if regular installation fails
echo.
echo Trying to install PyAudio...
pip install pipwin
pipwin install pyaudio

echo.
echo ====================================
echo Installation Complete!
echo ====================================
echo.
echo To run the voice assistant, type:
echo python voice_assistant.py
echo.
echo Make sure your microphone is working and connected.
echo The application requires internet connection for speech recognition.
echo.
pause
