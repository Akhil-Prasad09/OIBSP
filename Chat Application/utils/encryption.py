"""
Message encryption and password hashing.

Messages: Fernet (AES-128-CBC with an HMAC-SHA256 integrity check) under one shared key.
The server encrypts each message before storing and broadcasting it; clients decrypt.
Because the server holds the key, this is encryption at rest and on broadcast, not
end-to-end encryption.

Key: the CHAT_KEY environment variable if set, otherwise chat.key next to the app
(created on first run). Server and client must use the same key.

Passwords: salted scrypt, stored as "scrypt$<salt hex>$<hash hex>".
"""
import hashlib
import hmac
import os
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = Path(__file__).resolve().parent.parent / 'chat.key'
SCRYPT = dict(n=2 ** 14, r=8, p=1, dklen=32)


def load_key() -> bytes:
    env = os.environ.get('CHAT_KEY')
    if env:
        return env.encode()
    if not KEY_FILE.exists():
        KEY_FILE.write_bytes(Fernet.generate_key())
        KEY_FILE.chmod(0o600)
    return KEY_FILE.read_bytes().strip()


class EncryptionHandler:
    def __init__(self, key: bytes | None = None):
        self.fernet = Fernet(key or load_key())

    def encrypt(self, text: str) -> str:
        return self.fernet.encrypt(text.encode('utf-8')).decode('ascii')

    def decrypt(self, token: str) -> str:
        """Return the plaintext, or a placeholder if the token was made with another key."""
        try:
            return self.fernet.decrypt(token.encode('ascii')).decode('utf-8')
        except (InvalidToken, ValueError):
            return '[message could not be decrypted]'

    @staticmethod
    def hash_password(password: str) -> str:
        salt = os.urandom(16)
        digest = hashlib.scrypt(password.encode('utf-8'), salt=salt, **SCRYPT)
        return f'scrypt${salt.hex()}${digest.hex()}'

    @staticmethod
    def verify_password(password: str, stored: str) -> bool:
        try:
            scheme, salt_hex, digest_hex = stored.split('$')
        except ValueError:
            return False
        if scheme != 'scrypt':
            return False
        digest = hashlib.scrypt(password.encode('utf-8'), salt=bytes.fromhex(salt_hex), **SCRYPT)
        return hmac.compare_digest(digest.hex(), digest_hex)
