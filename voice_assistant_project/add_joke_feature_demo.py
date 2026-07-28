#!/usr/bin/env python3
"""
DEMO: Adding Joke Feature to Voice Assistant

This script demonstrates how to add a new feature (jokes) to your voice assistant.
Run this script to automatically add the joke feature to your voice_assistant.py file.
"""

import os

def add_joke_feature():
    """Add joke functionality to the voice assistant"""
    
    # Read the current voice assistant file
    with open('voice_assistant.py', 'r') as f:
        content = f.read()
    
    # Check if joke feature already exists
    if 'def get_joke(' in content:
        print("❌ Joke feature already exists in voice_assistant.py")
        return False
    
    # Add the joke function after the imports
    joke_function = '''
def get_joke():
    """Return a random programming joke"""
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
'''
    
    # Find where to insert the function (after imports, before class)
    class_pos = content.find('class VoiceAssistant:')
    if class_pos == -1:
        print("❌ Could not find VoiceAssistant class")
        return False
    
    # Insert the function before the class
    new_content = content[:class_pos] + joke_function + '\n' + content[class_pos:]
    
    # Add joke handling in get_response method
    joke_condition = '''        
        # Jokes (added by demo script)
        elif "joke" in command or "tell me a joke" in command or "funny" in command:
            return get_joke()
        '''
    
    # Find the get_response method and add our condition
    # Look for the weather condition as a landmark
    weather_pos = content.find('# Weather (basic response')
    if weather_pos == -1:
        print("❌ Could not find insertion point for joke condition")
        return False
    
    # Insert before the weather condition
    insertion_point = new_content.find('# Weather (basic response')
    new_content = new_content[:insertion_point] + joke_condition + '\n        ' + new_content[insertion_point:]
    
    # Add random import if not present
    if 'import random' not in new_content:
        import_pos = new_content.find('import threading')
        if import_pos != -1:
            new_content = new_content[:import_pos] + 'import random\n' + new_content[import_pos:]
    
    # Write the modified content back
    with open('voice_assistant.py', 'w') as f:
        f.write(new_content)
    
    print("✅ Joke feature successfully added to voice_assistant.py!")
    print("\nNow you can say:")
    print("- 'Tell me a joke'")
    print("- 'I want to hear a joke'") 
    print("- 'Say something funny'")
    
    return True

def create_backup():
    """Create a backup of the original file"""
    if os.path.exists('voice_assistant.py') and not os.path.exists('voice_assistant_backup.py'):
        with open('voice_assistant.py', 'r') as original:
            with open('voice_assistant_backup.py', 'w') as backup:
                backup.write(original.read())
        print("📁 Backup created: voice_assistant_backup.py")
        return True
    return False

def main():
    print("=" * 50)
    print("Voice Assistant Feature Addition Demo")
    print("=" * 50)
    print("This will add joke functionality to your voice assistant.")
    print()
    
    if not os.path.exists('voice_assistant.py'):
        print("❌ voice_assistant.py not found in current directory!")
        print("Make sure you're in the voice_assistant_project folder.")
        return
    
    # Create backup first
    create_backup()
    
    # Ask user confirmation
    response = input("Do you want to add the joke feature? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        if add_joke_feature():
            print("\n🎉 Success! Your voice assistant now tells jokes!")
            print("\nTo test it:")
            print("1. Run: python voice_assistant.py")
            print("2. Click 'Start Listening'")
            print("3. Say: 'Tell me a joke'")
            print("\nIf something goes wrong, restore from: voice_assistant_backup.py")
        else:
            print("❌ Failed to add joke feature. Check the error messages above.")
    else:
        print("⏹️ Operation cancelled.")

if __name__ == "__main__":
    main()
