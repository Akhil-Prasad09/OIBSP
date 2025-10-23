"""
Main client application with PyQt5 GUI and network handling
"""
import sys
import socket
import json
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from gui import LoginWindow, ChatWindow
from utils import EncryptionHandler, NotificationManager


HOST = '127.0.0.1'
PORT = 5555


class NetworkThread(QThread):
    """Thread for handling network communication"""
    
    message_received = pyqtSignal(dict)
    disconnected = pyqtSignal()
    
    def __init__(self, sock: socket.socket):
        super().__init__()
        self.sock = sock
        self.running = True
        self.buffer = b''
        
    def run(self):
        """Receive messages from server"""
        while self.running:
            try:
                data = self.sock.recv(4096)
                if not data:
                    break
                    
                self.buffer += data
                while b'\n' in self.buffer:
                    line, self.buffer = self.buffer.split(b'\n', 1)
                    if not line:
                        continue
                    try:
                        msg = json.loads(line.decode('utf-8'))
                        self.message_received.emit(msg)
                    except json.JSONDecodeError:
                        continue
            except ConnectionResetError:
                break
            except Exception as e:
                print(f"Network error: {e}")
                break
                
        self.disconnected.emit()
        
    def stop(self):
        """Stop the network thread"""
        self.running = False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except:
            pass


class ChatClient(QObject):
    """Main chat client controller"""
    
    def __init__(self):
        super().__init__()
        self.sock = None
        self.network_thread = None
        self.encryption = EncryptionHandler()
        self.notification_manager = NotificationManager()
        
        self.login_window = None
        self.chat_window = None
        self.user_data = None
        
    def start(self):
        """Start the application"""
        # Show login window
        self.login_window = LoginWindow()
        self.login_window.login_success.connect(self.handle_auth)
        self.login_window.show()
        
    def connect_to_server(self) -> bool:
        """Connect to chat server"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            
            # Start network thread
            self.network_thread = NetworkThread(self.sock)
            self.network_thread.message_received.connect(self.handle_server_message)
            self.network_thread.disconnected.connect(self.handle_disconnection)
            self.network_thread.start()
            
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            QMessageBox.critical(None, "Connection Error", 
                               f"Could not connect to server.\nMake sure the server is running on {HOST}:{PORT}")
            return False
            
    def handle_auth(self, data: dict):
        """Handle authentication (login/register)"""
        # Connect if not already connected
        if not self.sock:
            if not self.connect_to_server():
                self.login_window.reset_button()
                return
        
        # Send auth request
        mode = data['mode']
        if mode == 'register':
            self.send_message({
                'action': 'register',
                'username': data['username'],
                'password': data['password'],
                'email': data.get('email', '')
            })
        else:
            self.send_message({
                'action': 'login',
                'username': data['username'],
                'password': data['password']
            })
            
    def handle_server_message(self, msg: dict):
        """Handle messages from server"""
        msg_type = msg.get('type')
        
        if msg_type == 'register':
            if msg.get('success'):
                QMessageBox.information(self.login_window, "Success", 
                                      "Registration successful! Please log in.")
                self.login_window.reset_button()
            else:
                self.login_window.show_error(msg.get('message', 'Registration failed'))
                self.login_window.reset_button()
                
        elif msg_type == 'login':
            if msg.get('success'):
                self.user_data = msg.get('user')
                self.show_chat_window()
                # Request message history
                self.send_message({'action': 'get_history', 'room_id': 1, 'limit': 100})
            else:
                self.login_window.show_error(msg.get('message', 'Login failed'))
                self.login_window.reset_button()
                
        elif msg_type == 'message':
            if self.chat_window:
                content = msg.get('content', '')
                # Decrypt message
                decrypted = self.encryption.decrypt(content)
                
                display_msg = {
                    'sender': msg.get('sender'),
                    'content': decrypted,
                    'timestamp': None,
                    'message_type': msg.get('message_type', 'text')
                }
                
                is_sent = msg.get('sender') == self.user_data.get('username')
                self.chat_window.add_message(display_msg, is_sent)
                
                # Show notification if not sent by self
                if not is_sent:
                    self.notification_manager.notify_new_message(
                        msg.get('sender', 'Someone'),
                        decrypted
                    )
                    
        elif msg_type == 'history':
            if self.chat_window:
                messages = msg.get('messages', [])
                # Decrypt all messages
                for m in messages:
                    try:
                        m['content'] = self.encryption.decrypt(m['content'])
                    except:
                        pass
                self.chat_window.load_message_history(messages)
                
        elif msg_type == 'user_joined':
            username = msg.get('username')
            if self.chat_window and username != self.user_data.get('username'):
                self.chat_window.show_notification("User Joined", f"{username} joined the chat")
                self.notification_manager.notify_user_joined(username)
                
        elif msg_type == 'error':
            QMessageBox.warning(None, "Error", msg.get('message', 'An error occurred'))
            
    def show_chat_window(self):
        """Show chat window and hide login window"""
        self.login_window.hide()
        
        self.chat_window = ChatWindow(self.user_data)
        self.chat_window.send_message.connect(self.send_chat_message)
        self.chat_window.disconnect_requested.connect(self.disconnect)
        self.chat_window.show()
        
    def send_chat_message(self, content: str, message_type: str):
        """Send chat message to server"""
        self.send_message({
            'action': 'send_message',
            'content': content,
            'room_id': 1,
            'message_type': message_type
        })
        
    def send_message(self, data: dict):
        """Send message to server"""
        if self.sock:
            try:
                msg = json.dumps(data).encode('utf-8') + b'\n'
                self.sock.sendall(msg)
            except Exception as e:
                print(f"Send error: {e}")
                
    def disconnect(self):
        """Disconnect from server"""
        # Stop network thread first
        if self.network_thread:
            self.network_thread.stop()
            self.network_thread = None
            
        # Close socket
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
            self.sock = None
        
        # Close chat window
        if self.chat_window:
            self.chat_window.close()
            self.chat_window = None
        
        # Reset and show login window
        self.user_data = None
        self.login_window.show()
        self.login_window.reset_button()
        
    def handle_disconnection(self):
        """Handle unexpected disconnection"""
        QMessageBox.warning(None, "Disconnected", "Connection to server lost.")
        self.disconnect()


def main():
    """Main entry point"""
    # Allow multiple instances
    import os
    app_id = f"Chat Application {os.getpid()}"
    
    app = QApplication(sys.argv)
    app.setApplicationName(app_id)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and start client
    client = ChatClient()
    client.start()
    
    # Run application
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
