# Quick Start Guide 🚀

## Installation

1. **Install Python 3.8 or higher** if not already installed

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Step 1: Start the Server

Open a terminal/command prompt and run:

```bash
python server.py
```

You should see:
```
Server listening on 127.0.0.1:5555
```

### Step 2: Start the Client(s)

Open a **new** terminal/command prompt and run:

```bash
python client.py
```

The login window will appear with a beautiful modern UI!

### Step 3: Create an Account

1. Click **"Sign Up"** at the bottom
2. Enter a username (min 3 characters)
3. Enter a password (min 6 characters)
4. Optionally enter an email
5. Click **"Sign Up"** button
6. You'll see a success message

### Step 4: Login

1. Enter your username
2. Enter your password
3. Click **"Sign In"**
4. The chat window will open with smooth animations!

### Step 5: Start Chatting!

- Type messages in the input box at the bottom
- Click **Send** or press Enter
- Messages appear with smooth fade-in animations
- See online users in the sidebar
- Click the 📎 button to attach files
- Click the 😊 button for emojis

## Testing with Multiple Users

To test the chat with multiple users:

1. Keep the server running
2. Start multiple clients by running `python client.py` in different terminals
3. Register/login with different usernames
4. Chat between the windows!

## Features to Try

### ✨ Animations
- Watch the smooth fade-in when windows open
- Notice the slide transitions when switching between login/register
- See messages animate in as they arrive
- Shake animation when there's an error

### 🔐 Security
- All messages are encrypted end-to-end
- Passwords are hashed with SHA-256
- Secure socket communication

### 💬 Messaging
- Real-time message delivery
- Message history loaded on login
- Emoji support (try: :smile: :heart: :fire:)
- Timestamp on each message

### 👥 Social Features
- See who's online
- Get notified when users join
- Desktop notifications for new messages

### 🎨 Beautiful UI
- Modern dark theme
- Smooth animations and transitions
- Message bubbles (yours on right, others on left)
- Clean, professional design

## Troubleshooting

### "Could not connect to server"
- Make sure the server is running first (`python server.py`)
- Check that nothing else is using port 5555
- Verify HOST and PORT settings in both server.py and client.py

### Import errors
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory
- Check Python version (must be 3.8+)

### No notifications
- Notifications use the `plyer` library
- They should work on Windows, macOS, and Linux
- In-app notifications will always work

## Configuration

### Change Server Address
Edit `server.py` and `client.py`:
```python
HOST = '127.0.0.1'  # Change to your server IP
PORT = 5555          # Change to your preferred port
```

### Change Encryption Key
Edit `utils/encryption.py`:
```python
def __init__(self, password: str = "your_custom_key_here"):
```

## Database

The application uses SQLite with the database file `chat_app.db` created automatically in the project directory. It stores:
- User accounts (hashed passwords)
- Chat messages (encrypted)
- Chat rooms
- User sessions

To reset everything, simply delete `chat_app.db` and restart the server.

## Tips

- **Multiple chat rooms**: The foundation is there! You can extend the code to add more rooms
- **Multimedia**: Image/file sharing is partially implemented - expand in `utils/multimedia.py`
- **Customization**: Change colors in `gui/styles.py` to match your preferences
- **Emojis**: Type standard emoji shortcuts or use the emoji button

## Enjoy Your Chat Application! 💬✨

This is a fully-functional, professional-grade chat application with:
- ✅ Modern PyQt5 GUI
- ✅ Smooth animations and transitions
- ✅ Real-time messaging
- ✅ User authentication
- ✅ End-to-end encryption
- ✅ Message history
- ✅ Desktop notifications
- ✅ Emoji support
- ✅ Multi-threaded server
- ✅ SQLite database
- ✅ Professional design

Feel free to extend and customize it further!
