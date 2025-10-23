# Advanced Chat Application 💬

A professional-level chat application built with Python, featuring a modern PyQt5 GUI with smooth animations and transitions.

## Features ✨

- 🔐 **User Authentication** - Secure registration and login system
- 💬 **Real-time Messaging** - Instant message delivery using socket programming
- 🎨 **Modern UI** - Professional interface with smooth animations and transitions
- 🖼️ **Multimedia Sharing** - Send and receive images and files
- 😊 **Emoji Support** - Full emoji integration in messages
- 📜 **Message History** - Persistent chat history stored in database
- 🔔 **Notifications** - Desktop notifications for new messages
- 🔒 **End-to-End Encryption** - Secure message transmission with AES encryption
- 🏠 **Multiple Chat Rooms** - Create and join different chat rooms
- 👥 **Online Users** - See who's currently online

## Installation 🚀

1. Clone the repository or navigate to the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 📖

### Option 1: Easy Launch (Windows - Recommended)

**For Windows users**, simply use the batch files:

1. **Double-click** `1_Start_Server.bat` to start the server
2. **Double-click** `2_Start_Client.bat` to open a chat window
3. **Double-click** `2_Start_Client.bat` again for each additional user you want to test

✨ **Multiple instances work!** You can run as many clients as you want simultaneously.

### Option 2: Command Line

**Starting the Server:**
```bash
python server.py
```
The server will start on `localhost:5555` by default.

**Starting the Client(s):**
```bash
python client.py
```
You can run this command multiple times in different terminals to open multiple chat windows.

The client GUI will launch. You can:
- Register a new account
- Login with existing credentials
- Join chat rooms
- Send messages, emojis, and multimedia
- View message history
- Open multiple chat windows simultaneously

## Project Structure 📁

```
Chat Application/
├── server.py              # Main server application
├── client.py              # Main client application
├── database/
│   ├── db_handler.py      # Database operations
│   └── models.py          # Database models
├── gui/
│   ├── login_window.py    # Login/Register interface
│   ├── chat_window.py     # Main chat interface
│   └── styles.py          # UI styles and themes
├── utils/
│   ├── encryption.py      # Encryption utilities
│   ├── notifications.py   # Notification system
│   └── multimedia.py      # Multimedia handling
└── requirements.txt       # Project dependencies
```

## Configuration ⚙️

Default settings:
- **Host**: localhost
- **Port**: 5555
- **Encryption**: AES-256
- **Database**: SQLite (chat_app.db)

## Recent Updates 🆕

### Version 1.1 - Bug Fixes & Improvements

✅ **Fixed:** Username display issue - usernames now show correctly in messages (no more "Unknown")

✅ **Fixed:** Disconnect freeze issue - disconnecting is now instant and smooth

✅ **Added:** Multiple instance support - run as many chat windows as you need simultaneously

✅ **Added:** Easy-launch batch files for Windows users (`.bat` files)

✅ **Improved:** Network thread management for better performance

## Security 🔒

- Passwords are hashed using SHA-256
- Messages are encrypted using AES-256 encryption
- Secure socket communication
- PBKDF2HMAC key derivation (100,000 iterations)

## Technologies Used 🛠️

- **Python 3.8+**
- **PyQt5 5.15+** - GUI framework with animations
- **Socket Programming** - Real-time network communication
- **SQLite** - Lightweight database
- **Cryptography 41.0+** - AES-256 encryption
- **Pillow 10.0+** - Image processing
- **Emoji 2.0+** - Native emoji support
- **Plyer 2.0+** - Cross-platform notifications

## Testing Multiple Users 👥

To test the full chat experience with multiple users:

**Windows:**
1. Start the server: Double-click `1_Start_Server.bat`
2. Open client 1: Double-click `2_Start_Client.bat` → Register as "Alice"
3. Open client 2: Double-click `2_Start_Client.bat` → Register as "Bob"
4. Open client 3: Double-click `2_Start_Client.bat` → Register as "Charlie"
5. Chat between all windows with smooth animations!

**Command Line:**
```bash
# Terminal 1
python server.py

# Terminal 2
python client.py  # Alice

# Terminal 3
python client.py  # Bob

# Terminal 4
python client.py  # Charlie
```

## Troubleshooting 🔧

**Issue:** "Cannot import name 'PBKDF2'"
- **Solution:** Already fixed! Make sure you have the latest version of the code.

**Issue:** Usernames showing as "Unknown"
- **Solution:** Already fixed! Update to the latest version.

**Issue:** App freezes when disconnecting
- **Solution:** Already fixed! The disconnect is now instant.

**Issue:** Can't open multiple clients
- **Solution:** Already fixed! Multiple instances now work perfectly.

**Issue:** "python is not recognized"
- **Solution:** Make sure Python is installed and added to your system PATH.

## License 📄

MIT License - Feel free to use and modify!
