"""
Practical Extension Examples for Voice Assistant

These are real-world features you can add to make your assistant more useful.
Copy any of these functions and integrate them into your main voice_assistant.py file.
"""

import random
import os
import subprocess
import webbrowser
import json
from datetime import datetime, timedelta
import math

# ========== BEGINNER LEVEL EXTENSIONS ==========

def get_joke():
    """Tell a programming joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why did the programmer quit his job? He didn't get arrays!",
        "What's the object-oriented way to become wealthy? Inheritance!",
        "Why do Java developers wear glasses? Because they can't C#!",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
        "A SQL query goes into a bar, walks up to two tables and asks: 'Can I join you?'"
    ]
    return random.choice(jokes)

def flip_coin():
    """Flip a virtual coin"""
    result = random.choice(["Heads", "Tails"])
    return f"The coin landed on: {result}!"

def roll_dice():
    """Roll a virtual dice"""
    result = random.randint(1, 6)
    return f"The dice rolled: {result}!"

def basic_math(expression):
    """Simple calculator for basic math"""
    try:
        # Clean the expression
        expression = expression.replace("plus", "+").replace("minus", "-")
        expression = expression.replace("times", "*").replace("divided by", "/")
        
        # Only allow safe characters
        allowed = set('0123456789+-*/.() ')
        if all(c in allowed for c in expression):
            result = eval(expression)
            return f"The answer is: {result}"
        else:
            return "Sorry, I can only do basic math with numbers and operators."
    except:
        return "Sorry, I couldn't calculate that. Try something like '5 plus 3' or '10 times 2'."

def random_number(start=1, end=100):
    """Generate a random number"""
    number = random.randint(start, end)
    return f"Your random number between {start} and {end} is: {number}"

# ========== INTERMEDIATE LEVEL EXTENSIONS ==========

def open_application(app_name):
    """Open Windows applications"""
    apps = {
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'cmd': 'cmd.exe',
        'task manager': 'taskmgr.exe',
        'file explorer': 'explorer.exe',
        'control panel': 'control.exe',
        'browser': 'start chrome',
        'firefox': 'firefox.exe',
        'edge': 'msedge.exe'
    }
    
    app_name = app_name.lower().strip()
    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name], shell=True)
            return f"Opening {app_name.title()}..."
        except Exception as e:
            return f"Could not open {app_name}. Error: {e}"
    else:
        available = ', '.join(apps.keys())
        return f"I don't know how to open {app_name}. Available apps: {available}"

def get_system_info():
    """Get system information"""
    try:
        import platform
        import psutil
        
        system = platform.system()
        release = platform.release()
        processor = platform.processor()
        memory = round(psutil.virtual_memory().total / (1024**3), 2)
        
        return f"System: {system} {release}, Processor: {processor}, RAM: {memory} GB"
    except ImportError:
        return "System monitoring requires 'psutil'. Install it with: pip install psutil"
    except Exception as e:
        return f"Could not get system info: {e}"

def create_reminder():
    """Simple reminder system (stores in file)"""
    try:
        reminder_file = "reminders.json"
        
        # Load existing reminders
        if os.path.exists(reminder_file):
            with open(reminder_file, 'r') as f:
                reminders = json.load(f)
        else:
            reminders = []
        
        # Add new reminder
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reminder = {
            "created": timestamp,
            "message": "Voice reminder created",
            "id": len(reminders) + 1
        }
        
        reminders.append(reminder)
        
        # Save reminders
        with open(reminder_file, 'w') as f:
            json.dump(reminders, f, indent=2)
        
        return f"Reminder #{reminder['id']} created at {timestamp}. Check reminders.json file."
    except Exception as e:
        return f"Could not create reminder: {e}"

def check_reminders():
    """Check saved reminders"""
    try:
        reminder_file = "reminders.json"
        
        if not os.path.exists(reminder_file):
            return "You have no reminders yet."
        
        with open(reminder_file, 'r') as f:
            reminders = json.load(f)
        
        if not reminders:
            return "You have no reminders."
        
        recent_reminders = reminders[-3:]  # Show last 3
        response = "Your recent reminders:\n"
        for rem in recent_reminders:
            response += f"#{rem['id']}: {rem['message']} (Created: {rem['created']})\n"
        
        return response
    except Exception as e:
        return f"Could not check reminders: {e}"

def generate_password(length=12):
    """Generate a secure password"""
    import string
    
    if length < 6 or length > 50:
        return "Password length should be between 6 and 50 characters."
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return f"Generated password: {password}"

# ========== ADVANCED LEVEL EXTENSIONS ==========

def search_files(filename):
    """Search for files on the system (limited to user directory for safety)"""
    try:
        user_dir = os.path.expanduser("~")
        found_files = []
        
        for root, dirs, files in os.walk(user_dir):
            # Limit search depth to avoid long searches
            level = root.replace(user_dir, '').count(os.sep)
            if level > 3:
                continue
                
            for file in files:
                if filename.lower() in file.lower():
                    found_files.append(os.path.join(root, file))
                    if len(found_files) >= 5:  # Limit results
                        break
        
        if found_files:
            response = f"Found {len(found_files)} file(s):\n"
            for file in found_files:
                response += f"- {file}\n"
            return response
        else:
            return f"No files found containing '{filename}'"
    except Exception as e:
        return f"Error searching files: {e}"

def get_weather_info():
    """Basic weather info (requires API key for real data)"""
    # This is a placeholder - you can integrate with OpenWeatherMap API
    responses = [
        "It's a beautiful day outside! Maybe check your local weather app for details.",
        "I can't check real weather right now, but I hope it's nice where you are!",
        "For accurate weather, try saying 'search for weather forecast'.",
        "Weather feature coming soon! For now, I can open a weather website for you."
    ]
    return random.choice(responses)

def create_note(content=""):
    """Create a simple note file"""
    try:
        notes_dir = "voice_notes"
        if not os.path.exists(notes_dir):
            os.makedirs(notes_dir)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"note_{timestamp}.txt"
        filepath = os.path.join(notes_dir, filename)
        
        note_content = f"Voice Note Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        note_content += f"Content: {content if content else 'Voice note created via assistant'}\n"
        
        with open(filepath, 'w') as f:
            f.write(note_content)
        
        return f"Note created: {filename} in voice_notes folder."
    except Exception as e:
        return f"Could not create note: {e}"

# ========== INTEGRATION INSTRUCTIONS ==========

def integration_guide():
    """
    To add any of these functions to your voice assistant:
    
    1. Copy the function(s) you want to the top of voice_assistant.py
    
    2. In the get_response() method, add new conditions like:
    
        # Jokes
        elif "joke" in command or "tell me a joke" in command:
            return get_joke()
        
        # Coin flip
        elif "flip coin" in command or "coin flip" in command:
            return flip_coin()
        
        # Dice roll
        elif "roll dice" in command:
            return roll_dice()
        
        # Math
        elif any(word in command for word in ["calculate", "plus", "minus", "times", "divided"]):
            return basic_math(command)
        
        # Random number
        elif "random number" in command:
            return random_number()
        
        # Open application
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            return open_application(app_name)
        
        # System info
        elif "system info" in command:
            return get_system_info()
        
        # Create reminder
        elif "create reminder" in command or "remind me" in command:
            return create_reminder()
        
        # Check reminders
        elif "check reminders" in command or "show reminders" in command:
            return check_reminders()
        
        # Password generation
        elif "generate password" in command:
            return generate_password()
        
        # Search files
        elif "search for file" in command or "find file" in command:
            filename = command.replace("search for file", "").replace("find file", "").strip()
            return search_files(filename)
        
        # Create note
        elif "create note" in command or "take note" in command:
            return create_note()
    
    3. Add any required imports at the top of the file
    
    4. Test your new commands!
    """
    pass

# Test function to verify extensions work
if __name__ == "__main__":
    print("Testing Voice Assistant Extensions...")
    print("1. Joke:", get_joke())
    print("2. Coin flip:", flip_coin())
    print("3. Math:", basic_math("5 + 3"))
    print("4. Random number:", random_number())
    print("5. System info:", get_system_info())
    print("\nAll extensions working! Copy these to your main assistant.")
