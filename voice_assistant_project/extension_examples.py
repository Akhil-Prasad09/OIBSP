"""
Extension Examples for Voice Assistant

This file contains examples of how you can extend the voice assistant
with additional features and commands.
"""

import random
import subprocess
import os

def get_joke():
    """Return a random programming joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why did the programmer quit his job? He didn't get arrays!",
        "What's the object-oriented way to become wealthy? Inheritance!",
        "Why do Java developers wear glasses? Because they can't C#!"
    ]
    return random.choice(jokes)

def get_motivational_quote():
    """Return a motivational quote"""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Code is like humor. When you have to explain it, it's bad. - Cory House",
        "First, solve the problem. Then, write the code. - John Johnson",
        "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
        "In order to be irreplaceable, one must always be different. - Coco Chanel"
    ]
    return random.choice(quotes)

def open_application(app_name):
    """Open a system application (Windows example)"""
    apps = {
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'browser': 'start chrome',
        'file explorer': 'explorer.exe'
    }
    
    if app_name.lower() in apps:
        try:
            os.system(apps[app_name.lower()])
            return f"Opening {app_name}..."
        except Exception as e:
            return f"Could not open {app_name}. Error: {e}"
    else:
        return f"I don't know how to open {app_name}. Available apps: {', '.join(apps.keys())}"

def get_system_info():
    """Get basic system information"""
    try:
        import platform
        return f"System: {platform.system()} {platform.release()}, Python: {platform.python_version()}"
    except:
        return "Could not retrieve system information."

# Example of how to add these to the main voice assistant:
"""
In voice_assistant.py, in the get_response() method, add these conditions:

        # Jokes
        elif "joke" in command or "funny" in command:
            return get_joke()
        
        # Motivational quotes
        elif "motivate" in command or "quote" in command:
            return get_motivational_quote()
        
        # Open applications
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            return open_application(app_name)
        
        # System information
        elif "system info" in command or "system information" in command:
            return get_system_info()

Don't forget to import the functions at the top of voice_assistant.py:
from extension_examples import get_joke, get_motivational_quote, open_application, get_system_info
"""

# Weather API example (requires API key)
def get_weather(city="London"):
    """
    Example weather function using OpenWeatherMap API
    You need to sign up at https://openweathermap.org/api to get a free API key
    """
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    
    if API_KEY == "your_api_key_here":
        return "Weather feature requires an API key. Please get one from OpenWeatherMap and update the code."
    
    try:
        import requests
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"The weather in {city} is {temp}°C with {description}."
        else:
            return f"Could not get weather information for {city}."
    except Exception as e:
        return f"Error getting weather: {e}"

# More advanced examples:

def set_reminder(message, minutes):
    """Set a simple reminder (basic implementation)"""
    return f"Reminder set: '{message}' in {minutes} minutes. (Note: This is just a demo - actual implementation would require a scheduler)"

def calculate(expression):
    """Safe calculator for simple math"""
    try:
        # Only allow safe mathematical operations
        allowed_chars = set('0123456789+-*/.() ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"The result is: {result}"
        else:
            return "Sorry, I can only do basic math operations."
    except:
        return "Sorry, I couldn't calculate that. Please check your expression."

def get_random_fact():
    """Return a random tech fact"""
    facts = [
        "The first computer bug was an actual bug - a moth found in a Harvard computer in 1947.",
        "The term 'debugging' was coined by Admiral Grace Hopper.",
        "Python was named after Monty Python's Flying Circus, not the snake.",
        "The first 1GB hard drive cost $40,000 and weighed over 500 pounds.",
        "More than 90% of the world's currency is digital."
    ]
    return random.choice(facts)

# To integrate any of these functions into the main assistant,
# add the appropriate conditions to the get_response() method
# and import the functions you want to use.
