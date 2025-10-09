# Voice Assistant Test Examples 🎤

## Basic Commands to Try

### 1. **Greetings** 👋
Try saying:
- "Hello"
- "Hi there"
- "Good morning"
- "Hey assistant"

Expected Response: "Hello! How can I help you today?"

### 2. **Time & Date** ⏰
Try saying:
- "What time is it?"
- "Tell me the time"
- "What's the current time?"

Expected Response: Current time (e.g., "The current time is 2:45 PM")

Try saying:
- "What's the date?"
- "Tell me the date"
- "What's today's date?"

Expected Response: Current date (e.g., "Today's date is October 9, 2025")

### 3. **Web Search** 🔍
Try saying:
- "Search for Python programming"
- "Search weather forecast"
- "Search best pizza recipes"

Expected Response: Opens browser with Google search results

### 4. **Wikipedia Information** 📖
Try saying:
- "Tell me about Albert Einstein"
- "What is machine learning?"
- "Who is Bill Gates?"
- "Tell me about Python programming language"

Expected Response: Brief Wikipedia summary about the topic

### 5. **Weather Query** 🌤️
Try saying:
- "What's the weather?"
- "How's the weather today?"

Expected Response: Basic response suggesting web search (can be enhanced with API)

### 6. **Goodbye** 👋
Try saying:
- "Goodbye"
- "Bye"
- "Exit"
- "Stop"

Expected Response: "Goodbye! Have a great day!"

## Testing Steps

1. **Launch the application**: 
   ```bash
   python voice_assistant.py
   ```

2. **Click "Start Listening"** - Button turns red

3. **Speak clearly** into your microphone

4. **Wait for response** - Both text and voice output

5. **Check History tab** - See your conversation logged

## Common Issues & Solutions

### 🔧 If speech recognition isn't working:
- Check internet connection (uses Google Speech API)
- Speak closer to microphone
- Reduce background noise
- Try speaking slower and clearer

### 🔧 If microphone isn't detected:
- Check Windows microphone permissions
- Ensure microphone is set as default recording device
- Try running application as administrator

### 🔧 If text-to-speech isn't working:
- Check system volume
- Verify Windows Speech Platform is installed
- Try different voice commands to test

## Fun Experiments

Try these creative commands:
- "Search for funny cat videos"
- "Tell me about artificial intelligence"
- "What time is it in different time zones" (will give local time)
- "Search for latest technology news"
- "Tell me about the history of computers"
