#!/usr/bin/env python3
"""
Test script to verify voice assistant functionality
"""

import speech_recognition as sr
import pyttsx3
import sys

def test_text_to_speech():
    """Test text-to-speech functionality"""
    print("Testing Text-to-Speech...")
    try:
        engine = pyttsx3.init()
        engine.say("Hello! Text to speech is working!")
        engine.runAndWait()
        print("✓ Text-to-Speech: PASSED")
        return True
    except Exception as e:
        print(f"✗ Text-to-Speech: FAILED - {e}")
        return False

def test_microphone():
    """Test microphone access"""
    print("Testing Microphone Access...")
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1)
        print("✓ Microphone Access: PASSED")
        return True
    except Exception as e:
        print(f"✗ Microphone Access: FAILED - {e}")
        return False

def test_speech_recognition():
    """Test speech recognition (without actually recording)"""
    print("Testing Speech Recognition Setup...")
    try:
        r = sr.Recognizer()
        print("✓ Speech Recognition Setup: PASSED")
        return True
    except Exception as e:
        print(f"✗ Speech Recognition Setup: FAILED - {e}")
        return False

def main():
    print("=" * 50)
    print("Voice Assistant Functionality Test")
    print("=" * 50)
    
    tests = [
        test_speech_recognition,
        test_microphone,
        test_text_to_speech
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your voice assistant should work properly.")
        print("Run 'python voice_assistant.py' to start the application.")
    else:
        print("⚠️  Some tests failed. Check the error messages above.")
        print("You may need to install additional dependencies or check hardware.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
