# Chat Application 💬

A multi-client chat app in Python: a multithreaded socket server, a PyQt5 desktop client with animations, SQLite message history, and encrypted message storage.

## Features

- **Accounts:** register and log in; passwords stored as salted scrypt hashes
- **Real-time group chat:** a multithreaded TCP server broadcasts each message to everyone in the room
- **Encrypted storage and broadcast:** the server encrypts each message with Fernet (AES-128-CBC + HMAC-SHA256) before saving it and sending it to clients, which decrypt it locally
- **Message history:** the last 100 messages load when you log in
- **Emoji:** picker and `:alias:` shortcodes
- **Desktop notifications** for new messages and users joining (via plyer, where supported)
- **Multiple clients at once:** open as many windows as you like

### Security model, precisely

All clients and the server share one key (`chat.key`, created on first run, or the `CHAT_KEY` environment variable). Messages are encrypted at rest in the database and on the way from the server to clients. The server holds the key, so this is **not end-to-end encryption**, and messages travel from client to server unencrypted. The default setup runs everything on `localhost`. To run across machines, put the server behind TLS and copy `chat.key` to each client.

### Not implemented yet

- Sending files and images: the 📎 button only inserts the file name into your message
- Creating extra rooms: everyone chats in "General" (the database layer already supports rooms)
- Filling the online-users sidebar from the server

## Install

Python 3.10+.

```bash
pip install -r requirements.txt
```

## Run

**Windows:** double-click `1_Start_Server.bat`, then `2_Start_Client.bat` once per user.

**Any OS:**
```bash
python server.py     # terminal 1: listens on localhost:5555
python client.py     # terminal 2, 3, ...: one chat window each
```

Register a user in each window and start chatting.

## Tests

```bash
python -m pytest tests -q
```

The tests cover encryption round-trips, password hashing, and a full two-client session against a real server: register, log in, send, receive the encrypted broadcast, decrypt it, and check that the database never stores plaintext.

## Project structure

```
Chat Application/
├── server.py              # multithreaded socket server
├── client.py              # PyQt5 client + network thread
├── database/
│   ├── db_handler.py      # SQLite operations
│   └── models.py          # dataclasses
├── gui/
│   ├── login_window.py    # login / register
│   ├── chat_window.py     # chat interface
│   └── styles.py          # theme
├── utils/
│   ├── encryption.py      # Fernet messages, scrypt passwords, key loading
│   └── notifications.py   # desktop notifications
└── tests/test_chat.py
```

## Troubleshooting

- **"Could not connect to server":** start `server.py` first.
- **"[message could not be decrypted]":** the client and server are using different keys. Make sure they share the same `chat.key` or `CHAT_KEY`.
- **Old accounts can't log in:** password hashing changed to scrypt; delete `chat_app.db` and register again.
