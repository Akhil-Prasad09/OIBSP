import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import speech_recognition as sr
import pyttsx3
import threading
import datetime
import webbrowser
import wikipedia
import requests
import json
import os

class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        # Initialize speech recognition and text-to-speech
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        
        # Configure TTS settings
        self.tts_engine.setProperty('rate', 200)
        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
        
        # Conversation history
        self.conversation_history = []
        self.load_history()
        
        # Status variables
        self.is_listening = False
        
        self.create_gui()
        
        # Calibrate microphone for ambient noise
        self.calibrate_microphone()
    
    def create_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="🎤 Voice Assistant", 
                              font=("Arial", 24, "bold"), 
                              fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Main conversation tab
        self.main_frame = tk.Frame(self.notebook, bg="#34495e")
        self.notebook.add(self.main_frame, text="🏠 Assistant")
        
        # History tab
        self.history_frame = tk.Frame(self.notebook, bg="#34495e")
        self.notebook.add(self.history_frame, text="📚 History")
        
        self.create_main_tab()
        self.create_history_tab()
    
    def create_main_tab(self):
        # Status label
        self.status_label = tk.Label(self.main_frame, text="Ready to listen!", 
                                    font=("Arial", 14), 
                                    fg="#2ecc71", bg="#34495e")
        self.status_label.pack(pady=(20, 10))
        
        # Start button
        self.start_button = tk.Button(self.main_frame, text="🎤 Start Listening", 
                                     font=("Arial", 16, "bold"),
                                     bg="#3498db", fg="white",
                                     command=self.start_listening,
                                     padx=30, pady=15,
                                     relief=tk.RAISED,
                                     borderwidth=3)
        self.start_button.pack(pady=20)
        
        # Conversation display area
        conversation_frame = tk.Frame(self.main_frame, bg="#34495e")
        conversation_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        tk.Label(conversation_frame, text="Conversation:", 
                font=("Arial", 12, "bold"), 
                fg="#ecf0f1", bg="#34495e").pack(anchor=tk.W)
        
        self.conversation_text = scrolledtext.ScrolledText(conversation_frame, 
                                                          height=15, width=70,
                                                          font=("Arial", 10),
                                                          bg="#ecf0f1", fg="#2c3e50",
                                                          wrap=tk.WORD)
        self.conversation_text.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Add welcome message
        self.add_to_conversation("Assistant", "Hello! I'm your voice assistant. Click 'Start Listening' and try saying:\n- Hello\n- What time is it?\n- What's the date?\n- Search for [topic]\n- Tell me about [topic]")
    
    def create_history_tab(self):
        history_label = tk.Label(self.history_frame, text="Conversation History", 
                                font=("Arial", 16, "bold"), 
                                fg="#ecf0f1", bg="#34495e")
        history_label.pack(pady=(20, 10))
        
        # History display
        self.history_text = scrolledtext.ScrolledText(self.history_frame, 
                                                     height=20, width=70,
                                                     font=("Arial", 10),
                                                     bg="#ecf0f1", fg="#2c3e50",
                                                     wrap=tk.WORD,
                                                     state=tk.DISABLED)
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Clear history button
        clear_button = tk.Button(self.history_frame, text="Clear History", 
                               font=("Arial", 12),
                               bg="#e74c3c", fg="white",
                               command=self.clear_history,
                               padx=20, pady=10)
        clear_button.pack(pady=10)
        
        self.update_history_display()
    
    def calibrate_microphone(self):
        """Calibrate microphone for ambient noise"""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            print(f"Microphone calibration error: {e}")
    
    def start_listening(self):
        if not self.is_listening:
            self.is_listening = True
            self.start_button.config(text="🔴 Listening...", bg="#e74c3c")
            self.status_label.config(text="Listening... Speak now!", fg="#e74c3c")
            
            # Start listening in a separate thread
            listening_thread = threading.Thread(target=self.listen_for_command)
            listening_thread.daemon = True
            listening_thread.start()
    
    def listen_for_command(self):
        try:
            with self.microphone as source:
                # Listen for audio input
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
            
            # Update status
            self.root.after(0, lambda: self.status_label.config(text="Processing...", fg="#f39c12"))
            
            # Recognize speech
            command = self.recognizer.recognize_google(audio).lower()
            
            # Update GUI in main thread
            self.root.after(0, lambda: self.process_command(command))
            
        except sr.WaitTimeoutError:
            self.root.after(0, lambda: self.handle_error("Listening timeout. Please try again."))
        except sr.UnknownValueError:
            self.root.after(0, lambda: self.handle_error("Sorry, I couldn't understand what you said."))
        except sr.RequestError as e:
            self.root.after(0, lambda: self.handle_error(f"Speech recognition error: {e}"))
        except Exception as e:
            self.root.after(0, lambda: self.handle_error(f"An error occurred: {e}"))
        
        finally:
            # Reset button state
            self.root.after(0, self.reset_button_state)
    
    def process_command(self, command):
        """Process the recognized voice command"""
        self.add_to_conversation("You", command)
        
        response = self.get_response(command)
        self.add_to_conversation("Assistant", response)
        
        # Speak the response
        self.speak_response(response)
        
        # Save to history
        self.save_conversation_to_history(command, response)
    
    def get_response(self, command):
        """Generate appropriate response based on command"""
        command = command.lower().strip()
        
        # Greetings
        if any(greeting in command for greeting in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            return "Hello! How can I help you today?"
        
        # Time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        # Date
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            return f"Today's date is {current_date}"
        
        # Search commands
        elif "search for" in command or "search" in command:
            query = command.replace("search for", "").replace("search", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return f"I've opened a web search for '{query}' in your browser."
            else:
                return "What would you like me to search for?"
        
        # Wikipedia queries
        elif "tell me about" in command or "what is" in command or "who is" in command:
            query = command.replace("tell me about", "").replace("what is", "").replace("who is", "").strip()
            if query:
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    return f"Here's what I found about {query}: {summary}"
                except wikipedia.exceptions.DisambiguationError as e:
                    return f"There are multiple results for '{query}'. Could you be more specific?"
                except wikipedia.exceptions.PageError:
                    return f"I couldn't find information about '{query}'. Try a web search instead."
                except Exception as e:
                    return f"I encountered an error while searching for information about '{query}'."
            else:
                return "What would you like to know about?"
        
        # Weather (basic response - can be enhanced with API)
        elif "weather" in command:
            return "I can't check the weather right now, but you can ask me to search for weather information online."
        
        # Exit/goodbye
        elif any(word in command for word in ["bye", "goodbye", "exit", "quit", "stop"]):
            return "Goodbye! Have a great day!"
        
        # Default response
        else:
            return "I'm sorry, I didn't understand that command. Try saying 'hello', asking for the time or date, or ask me to search for something."
    
    def speak_response(self, response):
        """Convert text to speech"""
        def speak():
            try:
                self.tts_engine.say(response)
                self.tts_engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}")
        
        # Run TTS in separate thread
        tts_thread = threading.Thread(target=speak)
        tts_thread.daemon = True
        tts_thread.start()
    
    def add_to_conversation(self, speaker, message):
        """Add message to conversation display"""
        timestamp = datetime.datetime.now().strftime("%H:%M")
        formatted_message = f"[{timestamp}] {speaker}: {message}\n\n"
        
        self.conversation_text.insert(tk.END, formatted_message)
        self.conversation_text.see(tk.END)
    
    def save_conversation_to_history(self, user_input, assistant_response):
        """Save conversation to history"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversation = {
            "timestamp": timestamp,
            "user": user_input,
            "assistant": assistant_response
        }
        
        self.conversation_history.append(conversation)
        self.save_history()
        self.update_history_display()
    
    def update_history_display(self):
        """Update the history tab display"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        
        for conv in reversed(self.conversation_history[-50:]):  # Show last 50 conversations
            self.history_text.insert(tk.END, f"📅 {conv['timestamp']}\n")
            self.history_text.insert(tk.END, f"👤 You: {conv['user']}\n")
            self.history_text.insert(tk.END, f"🤖 Assistant: {conv['assistant']}\n")
            self.history_text.insert(tk.END, "-" * 50 + "\n\n")
        
        self.history_text.config(state=tk.DISABLED)
    
    def clear_history(self):
        """Clear conversation history"""
        if messagebox.askyesno("Clear History", "Are you sure you want to clear all conversation history?"):
            self.conversation_history = []
            self.save_history()
            self.update_history_display()
    
    def save_history(self):
        """Save history to file"""
        try:
            with open("conversation_history.json", "w") as f:
                json.dump(self.conversation_history, f, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def load_history(self):
        """Load history from file"""
        try:
            if os.path.exists("conversation_history.json"):
                with open("conversation_history.json", "r") as f:
                    self.conversation_history = json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
            self.conversation_history = []
    
    def handle_error(self, error_message):
        """Handle errors and update GUI"""
        self.status_label.config(text=error_message, fg="#e74c3c")
        self.add_to_conversation("System", error_message)
    
    def reset_button_state(self):
        """Reset the start button to original state"""
        self.is_listening = False
        self.start_button.config(text="🎤 Start Listening", bg="#3498db")
        self.status_label.config(text="Ready to listen!", fg="#2ecc71")

def main():
    root = tk.Tk()
    app = VoiceAssistant(root)
    
    # Handle window closing
    def on_closing():
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
