# Voice Assistant Application 🎤

A simple, beginner-friendly voice assistant with a GUI that can respond to basic voice commands.

## Features

- 🎤 **Voice Recognition**: Speak commands and get responses
- 🗣️ **Text-to-Speech**: The assistant speaks back to you
- 💬 **Chat Interface**: See your conversation in real-time
- 📚 **History Tab**: View past conversations with timestamps
- 🔍 **Web Search**: Search for topics online
- 📖 **Wikipedia Integration**: Get information about various topics
- ⏰ **Time & Date**: Ask for current time and date
- 🎨 **User-Friendly GUI**: Clean, modern interface

## Supported Voice Commands

- **Greetings**: "Hello", "Hi", "Hey", "Good morning"
- **Time**: "What time is it?"
- **Date**: "What's the date?"
- **Search**: "Search for [topic]" or "Search [topic]"
- **Information**: "Tell me about [topic]", "What is [topic]", "Who is [person]"
- **Weather**: "What's the weather?" (basic response)
- **Goodbye**: "Bye", "Goodbye", "Exit"

## Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Step 1: Install Dependencies

Open Command Prompt or PowerShell and navigate to the project directory:

```bash
cd voice_assistant_project
pip install -r requirements.txt
```

### Step 2: Install PyAudio (Windows)

If you encounter issues with PyAudio installation, try:

```bash
pip install pipwin
pipwin install pyaudio
```

Alternatively, download the appropriate PyAudio wheel file from:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

### Step 3: Run the Application

```bash
python voice_assistant.py
```

## Usage

1. **Start the Application**: Run the Python script
2. **Click "Start Listening"**: The button will turn red and show "Listening..."
3. **Speak Your Command**: Clearly speak one of the supported commands
4. **View Response**: See the conversation in the main tab and hear the audio response
5. **Check History**: Click the "History" tab to see past conversations

## Troubleshooting

### Common Issues:

1. **Microphone Not Working**:
   - Check if your microphone is properly connected
   - Ensure microphone permissions are granted to Python
   - Try running the application as administrator

2. **PyAudio Installation Error**:
   - Install Visual Studio Build Tools
   - Use the pipwin method mentioned above
   - Try installing a pre-compiled wheel

3. **Speech Recognition Not Working**:
   - Check your internet connection (Google Speech API requires internet)
   - Speak clearly and closer to the microphone
   - Ensure minimal background noise

4. **Text-to-Speech Not Working**:
   - Check system audio settings
   - Try restarting the application
   - Ensure Windows Speech Platform is installed

## Project Structure

```
voice_assistant_project/
├── voice_assistant.py      # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── conversation_history.json  # Created automatically to store history
```

## Extending the Application

To add more features:

1. **Add New Commands**: Modify the `get_response()` method in `voice_assistant.py`
2. **Integrate APIs**: Add weather APIs, news APIs, etc.
3. **Improve NLP**: Use libraries like NLTK or spaCy for better command understanding
4. **Add Settings**: Create a settings tab for customization

## Dependencies

- `speechrecognition`: For voice input processing
- `pyttsx3`: For text-to-speech output
- `pyaudio`: For microphone access
- `wikipedia`: For Wikipedia information queries
- `requests`: For web requests
- `tkinter`: For GUI (included with Python)

## License

This project is for educational purposes. Feel free to modify and extend it!

## Contributing

Feel free to fork this project and submit pull requests for improvements!
