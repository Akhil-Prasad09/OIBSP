"""Run from the 'Chat Application' folder:  python -m pytest tests -q"""
import json
import socket
import sqlite3
import sys
import threading
import time
from pathlib import Path

import pytest
from cryptography.fernet import Fernet

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import EncryptionHandler  # noqa: E402


def test_encrypt_round_trip_and_wrong_key():
    a, b = EncryptionHandler(Fernet.generate_key()), EncryptionHandler(Fernet.generate_key())
    token = a.encrypt('hello, नमस्ते')
    assert token != 'hello, नमस्ते'
    assert a.decrypt(token) == 'hello, नमस्ते'
    assert b.decrypt(token) == '[message could not be decrypted]'


def test_password_hashing():
    h1, h2 = EncryptionHandler.hash_password('s3cret'), EncryptionHandler.hash_password('s3cret')
    assert h1 != h2                                   # salted
    assert EncryptionHandler.verify_password('s3cret', h1)
    assert not EncryptionHandler.verify_password('wrong', h1)
    assert not EncryptionHandler.verify_password('s3cret', 'not-a-hash')


class Conn:
    def __init__(self, port):
        self.sock = socket.create_connection(('127.0.0.1', port), timeout=5)
        self.buf = b''

    def send(self, **msg):
        self.sock.sendall(json.dumps(msg).encode() + b'\n')

    def recv_until(self, mtype):
        while True:
            while b'\n' in self.buf:
                line, self.buf = self.buf.split(b'\n', 1)
                msg = json.loads(line)
                if msg.get('type') == mtype:
                    return msg
            self.buf += self.sock.recv(4096)


@pytest.fixture
def server(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)                       # fresh chat_app.db
    monkeypatch.setenv('CHAT_KEY', Fernet.generate_key().decode())
    from server import ChatServer
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        port = s.getsockname()[1]
    srv = ChatServer('127.0.0.1', port)
    threading.Thread(target=srv.start, daemon=True).start()
    time.sleep(0.3)
    yield port, tmp_path


def test_two_clients_exchange_encrypted_message(server):
    port, tmp = server
    alice, bob = Conn(port), Conn(port)
    for c, name in [(alice, 'alice'), (bob, 'bob')]:
        c.send(action='register', username=name, password='pw-' + name, email='')
        assert c.recv_until('register')['success']
        c.send(action='login', username=name, password='pw-' + name)
        assert c.recv_until('login')['success']

    alice.send(action='send_message', content='meet at 5', room_id=1, message_type='text')
    msg = bob.recv_until('message')
    assert msg['sender'] == 'alice'
    assert msg['content'] != 'meet at 5'              # broadcast is ciphertext
    assert EncryptionHandler().decrypt(msg['content']) == 'meet at 5'

    stored = sqlite3.connect(tmp / 'chat_app.db').execute('SELECT content FROM messages').fetchall()
    assert stored and all(row[0] != 'meet at 5' for row in stored)

    bob.send(action='login', username='alice', password='wrong')
    assert not bob.recv_until('login')['success']
