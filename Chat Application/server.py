"""
Multi-threaded chat server with authentication, rooms, and encryption
"""
import socket
import threading
import json
from typing import Dict, Tuple
from database import DatabaseHandler
from utils import EncryptionHandler


HOST = '127.0.0.1'
PORT = 5555


class ClientThread(threading.Thread):
    def __init__(self, conn: socket.socket, addr: Tuple[str, int], server: 'ChatServer'):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr
        self.server = server
        self.user_id = None
        self.username = None
        self.encryption = EncryptionHandler()

    def send(self, payload: dict):
        try:
            data = json.dumps(payload).encode('utf-8') + b'\n'
            self.conn.sendall(data)
        except Exception:
            self.server.disconnect_client(self)

    def run(self):
        buffer = b''
        while True:
            try:
                data = self.conn.recv(4096)
                if not data:
                    break
                buffer += data
                while b'\n' in buffer:
                    line, buffer = buffer.split(b'\n', 1)
                    if not line:
                        continue
                    try:
                        msg = json.loads(line.decode('utf-8'))
                        self.handle_message(msg)
                    except json.JSONDecodeError:
                        continue
            except ConnectionResetError:
                break
            except Exception:
                break
        self.server.disconnect_client(self)

    def handle_message(self, msg: dict):
        action = msg.get('action')
        if action == 'register':
            username = msg.get('username')
            password = msg.get('password')
            email = msg.get('email')
            self.server.handle_register(self, username, password, email)
        elif action == 'login':
            username = msg.get('username')
            password = msg.get('password')
            self.server.handle_login(self, username, password)
        elif action == 'join_room':
            room_id = int(msg.get('room_id', 1))
            self.server.handle_join_room(self, room_id)
        elif action == 'send_message':
            content = msg.get('content', '')
            room_id = int(msg.get('room_id', 1))
            mtype = msg.get('message_type', 'text')
            encrypted = self.encryption.encrypt(content)
            self.server.handle_send_message(self, room_id, encrypted, mtype)
        elif action == 'get_rooms':
            self.server.handle_get_rooms(self)
        elif action == 'get_history':
            room_id = int(msg.get('room_id', 1))
            limit = int(msg.get('limit', 100))
            self.server.handle_get_history(self, room_id, limit)
        else:
            self.send({'type': 'error', 'message': 'Unknown action'})


class ChatServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.db = DatabaseHandler()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients: Dict[int, ClientThread] = {}
        self.room_members: Dict[int, set[int]] = {}  # room_id -> set of user_ids
        self.lock = threading.Lock()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(50)
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                conn, addr = self.server_socket.accept()
                client = ClientThread(conn, addr, self)
                client.start()
        finally:
            self.server_socket.close()

    def broadcast(self, room_id: int, payload: dict):
        with self.lock:
            members = self.room_members.get(room_id, set()).copy()
            for uid in members:
                client = self.clients.get(uid)
                if client:
                    client.send(payload)

    def disconnect_client(self, client: ClientThread):
        with self.lock:
            if client.user_id in self.clients:
                print(f"Client disconnected: {client.username or client.addr}")
                # Update DB status
                if client.user_id:
                    self.db.update_user_status(client.user_id, False)
                # Remove from room members
                for members in self.room_members.values():
                    members.discard(client.user_id)
                del self.clients[client.user_id]
        try:
            client.conn.close()
        except Exception:
            pass

    # Handlers
    def handle_register(self, client: ClientThread, username: str, password: str, email: str | None):
        from utils import EncryptionHandler
        pwd_hash = EncryptionHandler.hash_password(password)
        user_id = self.db.create_user(username, pwd_hash, email)
        if user_id is None:
            client.send({'type': 'register', 'success': False, 'message': 'Username already exists'})
        else:
            client.send({'type': 'register', 'success': True, 'message': 'Registration successful'})

    def handle_login(self, client: ClientThread, username: str, password: str):
        from utils import EncryptionHandler
        user = self.db.get_user_by_username(username)
        if not user:
            client.send({'type': 'login', 'success': False, 'message': 'User not found'})
            return
        if not EncryptionHandler.verify_password(password, user.password_hash):
            client.send({'type': 'login', 'success': False, 'message': 'Invalid credentials'})
            return
        # Mark online and attach
        self.db.update_user_status(user.user_id, True)
        client.user_id = user.user_id
        client.username = user.username
        with self.lock:
            self.clients[user.user_id] = client
        # Auto join General
        self.handle_join_room(client, 1)
        client.send({'type': 'login', 'success': True, 'user': user.to_dict()})
        # Notify room
        self.broadcast(1, {'type': 'user_joined', 'room_id': 1, 'username': user.username})

    def handle_join_room(self, client: ClientThread, room_id: int):
        if not client.user_id:
            client.send({'type': 'error', 'message': 'Not authenticated'})
            return
        with self.lock:
            self.room_members.setdefault(room_id, set()).add(client.user_id)
        client.send({'type': 'joined_room', 'room_id': room_id})

    def handle_send_message(self, client: ClientThread, room_id: int, encrypted_content: str, message_type: str):
        if not client.user_id:
            client.send({'type': 'error', 'message': 'Not authenticated'})
            return
        # Save to DB
        from database import Message
        msg = Message(
            sender_id=client.user_id,
            sender_username=client.username,
            room_id=room_id,
            content=encrypted_content,
            message_type=message_type,
            is_encrypted=True
        )
        msg_id = self.db.save_message(msg)
        payload = {
            'type': 'message',
            'message_id': msg_id,
            'room_id': room_id,
            'sender': client.username,
            'content': encrypted_content,
            'message_type': message_type
        }
        self.broadcast(room_id, payload)

    def handle_get_rooms(self, client: ClientThread):
        rooms = [r.to_dict() for r in self.db.get_all_rooms()]
        client.send({'type': 'rooms', 'rooms': rooms})

    def handle_get_history(self, client: ClientThread, room_id: int, limit: int):
        messages = [m.to_dict() for m in self.db.get_room_messages(room_id, limit)]
        client.send({'type': 'history', 'room_id': room_id, 'messages': messages})


if __name__ == '__main__':
    ChatServer(HOST, PORT).start()
