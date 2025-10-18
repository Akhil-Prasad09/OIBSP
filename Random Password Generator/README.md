# 🔐 Advanced Password Generator

**Oasis Infobyte Internship Project**

A sophisticated GUI-based password generator built with Python and Tkinter, featuring advanced customization options, real-time strength analysis, and an intuitive user interface.

## 🌟 Features

### Core Functionality
- **Customizable Length**: Generate passwords from 4 to 50 characters
- **Character Type Selection**: 
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)  
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- **Smart Exclusions**: Option to exclude similar-looking characters (0,O,1,l,I)

### User Experience
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Visual Feedback**: Button animations and status confirmations
- **Password History**: Maintains history of last 10 generated passwords
- **Quick Presets**: Pre-configured strength levels (Weak, Medium, Strong, Ultra)

### Security Features  
- **Real-Time Strength Analysis**: Dynamic password strength evaluation
- **Animated Progress Bar**: Visual representation of password security level
- **Smart Recommendations**: Tips for improving password strength
- **Secure Generation**: Uses Python's cryptographically secure random module

### Interface Design
- **Professional Dark Theme**: Modern, eye-friendly color scheme
- **Responsive Layout**: Clean, organized sections with labeled frames
- **Clear Typography**: High-contrast text for excellent readability
- **Intuitive Controls**: Logical grouping and clear button labeling

## 🖥️ Screenshots

The application features a professional dark theme interface with:
- Password length slider at the top
- Character type selection checkboxes
- Large, prominent "GENERATE PASSWORD" button
- Clear white output textbox for generated passwords
- Green "Copy to Clipboard" and orange "Clear" buttons
- Real-time password strength meter
- Quick preset buttons for common configurations

## 🚀 Quick Start

### Method 1: Using Batch File (Recommended)
```bash
# Simply double-click or run:
run.bat
```

### Method 2: Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python password_generator.py
```

## 📋 Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: 
  - `tkinter` (usually included with Python)
  - `pyperclip` (for clipboard functionality)

## 🎯 Usage Guide

### Basic Usage
1. **Set Password Length**: Use the slider to choose desired length (4-50 characters)
2. **Select Character Types**: Check/uncheck boxes for character categories
3. **Generate Password**: Click the red "🚀 GENERATE PASSWORD" button
4. **Copy Password**: Click the green "📋 Copy to Clipboard" button

### Advanced Features
- **Quick Presets**: Use preset buttons for instant configuration:
  - **Weak**: 8 chars, letters only
  - **Medium**: 12 chars, letters + numbers  
  - **Strong**: 16 chars, letters + numbers + symbols
  - **Ultra**: 24 chars, all character types
- **Exclude Similar**: Enable to avoid confusing characters (0,O,1,l,I)
- **Strength Analysis**: Monitor the colored progress bar and recommendations

### Keyboard Shortcuts
- The interface is fully mouse-driven for ease of use
- All buttons provide visual feedback when clicked
- Copy function automatically selects the entire password

## 🔧 Technical Details

### Architecture
- **Framework**: Python Tkinter (cross-platform GUI)
- **Design Pattern**: Object-oriented with clean separation of concerns
- **Threading**: Non-blocking UI updates for smooth animations

### Security Implementation
- Uses `random.choice()` with cryptographically appropriate randomness
- Character sets are properly sanitized
- No password storage or logging (security by design)
- Clipboard integration with automatic cleanup

### Code Structure
```
password_generator.py
├── PasswordGenerator class
│   ├── __init__()          # Initialize UI and variables
│   ├── create_widgets()    # Build the interface
│   ├── generate_password() # Core password generation
│   ├── calculate_strength()# Security analysis
│   ├── copy_password()     # Clipboard functionality
│   └── animate_progress()  # Visual effects
```

## 🛠️ Customization

### Modifying Character Sets
Edit the character sets in the `generate_password()` method:
```python
# Add custom symbols
if self.symbols_var.get():
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    # Add more symbols here
```

### Changing UI Theme
Modify colors in the widget creation sections:
```python
bg='#2c3e50'  # Background color
fg='#ecf0f1'  # Text color
```

### Adjusting Strength Calculation
Update scoring logic in `calculate_strength()`:
```python
# Modify scoring weights
if len(password) >= 8:
    score += 25  # Adjust points for length
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Module not found: pyperclip"
**Solution**: Install dependencies using `pip install pyperclip`

**Issue**: Copy to clipboard not working
**Solution**: Ensure pyperclip is installed and system clipboard is accessible

**Issue**: Application won't start
**Solution**: Verify Python 3.6+ is installed and tkinter is available

**Issue**: Characters not displaying correctly
**Solution**: Ensure system supports Unicode characters

### System Requirements
- **Windows**: Windows 7 or later
- **macOS**: macOS 10.12 or later  
- **Linux**: Most modern distributions with GUI support

## 📈 Password Strength Scoring

The strength calculation uses the following criteria:

| Factor | Points | Description |
|--------|---------|-------------|
| Length 8+ | 25 | Basic security length |
| Length 12+ | +25 | Good security length |
| Length 16+ | +25 | Excellent security length |
| Uppercase | 10 | Capital letters present |
| Lowercase | 10 | Small letters present |
| Numbers | 10 | Digits present |
| Symbols | 15 | Special characters present |

**Strength Levels**:
- 🔴 **Weak** (0-49%): Basic protection
- 🟡 **Medium** (50-69%): Moderate security
- 🟠 **Strong** (70-84%): Good security
- 🟢 **Very Strong** (85-100%): Excellent security

## 🤝 Contributing

This project was created as part of the Oasis Infobyte internship program. The code is well-documented and structured for educational purposes.

### Development Setup
1. Clone or download the project
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python password_generator.py`
4. Make your modifications
5. Test thoroughly before deployment

## 📄 License

This project is created for educational purposes as part of the Oasis Infobyte internship program.

## 🙏 Acknowledgments

- **Oasis Infobyte**: For providing the internship opportunity and project guidelines
- **Python Community**: For the excellent tkinter and pyperclip libraries
- **Security Community**: For best practices in password generation

## 📞 Contact

Created as part of the Oasis Infobyte internship program.

---

**⚡ Ready to generate secure passwords? Run `run.bat` and start protecting your digital life!**