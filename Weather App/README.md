# Weather Pro - Professional Weather Application

A full-stack Python weather application with a professional Tkinter GUI that provides real-time weather information and 5-day forecasts for any location worldwide.

**OASIS Infobyte Internship Project**

---

## 🌟 Features

### Core Features
- **Real-time Weather Data**: Get current weather conditions for any city or ZIP code
- **5-Day Forecast**: View detailed weather forecasts for the next 5 days
- **Professional GUI**: Modern, clean interface built with Tkinter
- **Unit Conversion**: Toggle between Celsius and Fahrenheit
- **Detailed Information**: Temperature, humidity, wind speed, pressure, visibility, sunrise/sunset times

### Technical Features
- **API Integration**: Connects to OpenWeatherMap API for accurate weather data
- **Error Handling**: Comprehensive error handling for network issues, invalid locations, and API errors
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Responsive Design**: User-friendly interface with hover effects and visual feedback

---

## 📋 Requirements

- **Python 3.7 or higher**
- **requests** library (for API calls)
- **tkinter** (usually comes pre-installed with Python)
- **OpenWeatherMap API Key** (free tier available)

---

## ⚠️ Important: Protecting Your API Key

**NEVER commit your `config.json` file to GitHub or any public repository!**

Your API key is like a password. This project includes:
- `.gitignore` - Automatically excludes `config.json` from git
- `config.example.json` - Safe template to share publicly

Users cloning your repo should:
1. Copy `config.example.json` to `config.json`
2. Add their own API key to `config.json`

---

## 🚀 Installation & Setup

### Step 1: Install Python
If you don't have Python installed:
1. Download from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation: `python --version`

### Step 2: Install Dependencies
Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 3: Get Your API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to "API keys" in your account dashboard
4. Copy your API key (it may take a few minutes to activate)

### Step 4: Configure API Key
**If you cloned from GitHub:** Copy the example config first:
```bash
copy config.example.json config.json
```

Then open `config.json` and replace `YOUR_API_KEY_HERE` with your actual API key:

```json
{
    "api_key": "your_actual_api_key_here"
}
```

**⚠️ IMPORTANT:** Never commit `config.json` to git! It's already in `.gitignore`.

**Alternative Method**: Set an environment variable
```bash
# Windows
set OPENWEATHER_API_KEY=your_api_key_here

# macOS/Linux
export OPENWEATHER_API_KEY=your_api_key_here
```

---

## 💻 Running the Application

### Windows
Double-click `run_weather_app.bat` or run:
```bash
python weather_app.py
```

### macOS/Linux
```bash
python3 weather_app.py
```

---

## 📖 How to Use

1. **Launch the Application**: Run the app using one of the methods above
2. **Enter Location**: Type a city name (e.g., "London", "New York") or ZIP code in the search field
3. **Select Units**: Choose between Celsius (°C) or Fahrenheit (°F)
4. **Search**: Click "🔍 Search Weather" or press Enter
5. **View Results**: 
   - Current weather displays on the left with temperature, conditions, and details
   - 5-day forecast appears at the bottom with daily summaries

### Supported Location Formats
- City name: `London`, `Tokyo`, `New York`
- City with country: `Paris,FR`, `Toronto,CA`
- ZIP code: `10001` (US), `SW1A 1AA` (UK)

---

## 🏗️ Project Structure

```
Weather App/
│
├── weather_app.py          # Main GUI application
├── weather_api.py          # API integration module
├── config.json             # API key configuration
├── requirements.txt        # Python dependencies
├── run_weather_app.bat     # Windows launcher script
└── README.md              # This file
```

### File Descriptions

- **weather_app.py**: Contains the `WeatherApp` class with Tkinter GUI implementation
- **weather_api.py**: Contains the `WeatherAPI` class for handling API requests and data parsing
- **config.json**: Stores your OpenWeatherMap API key securely
- **requirements.txt**: Lists all Python package dependencies
- **run_weather_app.bat**: Automated launcher for Windows users

---

## 🎨 GUI Overview

### Main Components

1. **Header Section**: App title and subtitle
2. **Search Section**: 
   - Location input field
   - Search button with hover effects
   - Unit toggle (Celsius/Fahrenheit)
3. **Current Weather Section**:
   - Location and date
   - Large temperature display
   - Weather description with emoji
   - Detailed metrics (humidity, wind, pressure, visibility, sunrise/sunset)
4. **Forecast Section**: 5-day forecast cards with icons and temperature ranges

### Color Scheme
- Background: Dark blue theme (#1a1a2e)
- Cards: Navy blue (#16213e)
- Accents: Deep blue (#0f3460)
- Highlights: Coral red (#e94560)
- Text: Light gray (#eaeaea)

---

## 🔧 Troubleshooting

### Common Issues

**Problem**: "API key not found" error
- **Solution**: Make sure your `config.json` file exists and contains your valid API key

**Problem**: "Location not found" error
- **Solution**: Check the spelling of your city name. Try adding the country code (e.g., "Springfield,US")

**Problem**: "Connection error"
- **Solution**: Check your internet connection. Make sure you're not behind a restrictive firewall

**Problem**: "Invalid API key"
- **Solution**: Verify your API key is correct and has been activated (can take 10-15 minutes after signup)

**Problem**: App window is blank or frozen
- **Solution**: Check your Python version (3.7+) and ensure tkinter is installed

**Problem**: "Module not found: requests"
- **Solution**: Run `pip install requests` or `pip install -r requirements.txt`

---

## 📊 API Information

This application uses the **OpenWeatherMap API**:

- **Current Weather API**: `/data/2.5/weather`
- **5-Day Forecast API**: `/data/2.5/forecast`

### Free Tier Limits
- 60 calls/minute
- 1,000,000 calls/month
- Current weather data
- 5-day/3-hour forecast

For more information, visit [OpenWeatherMap API Documentation](https://openweathermap.org/api)

---

## 🎯 Key Concepts Implemented

### API Integration
- REST API calls using `requests` library
- JSON data parsing
- Error handling for various API response codes
- Timeout handling for network issues

### User Input Handling
- Input validation
- Support for multiple location formats
- Real-time feedback with loading states

### GUI Design
- Modern card-based layout
- Responsive components
- Hover effects and visual feedback
- Color-coded information display
- Emoji icons for weather conditions

### Error Handling
- Network connectivity errors
- Invalid API keys
- Location not found
- Timeout handling
- Graceful degradation (forecast fails silently)

### Data Visualization
- Large, easy-to-read temperature display
- Weather condition emojis (☀, ☁, 🌧, ⛈, ❄, 🌫)
- Color-coded information cards
- Daily forecast cards with min/max temperatures

### Unit Conversion
- Metric (Celsius, m/s, km)
- Imperial (Fahrenheit, mph, miles)
- Real-time unit switching

---

## 🌐 Future Enhancements (Optional)

- GPS/IP-based automatic location detection
- Hourly forecast view
- Weather alerts and warnings
- Historical weather data
- Weather maps and radar
- Save favorite locations
- Desktop notifications
- Theme customization

---

## 📝 Assignment Requirements Checklist

✅ **API Integration**: Connected to OpenWeatherMap API with proper JSON parsing

✅ **User Input Handling**: Validated location input with error messages

✅ **GUI Design**: Professional Tkinter interface with modern styling

✅ **Error Handling**: Comprehensive error handling for API and user input

✅ **Data Visualization**: Weather icons, color-coded cards, and clear data display

✅ **Unit Conversion**: Temperature unit toggle (Celsius/Fahrenheit)

✅ **Advanced Features**:
- Detailed weather information (temperature, humidity, wind, pressure, visibility)
- Sunrise/sunset times
- 5-day weather forecast
- User-friendly interface with visual elements
- Loading states and feedback

---

## 📄 License

This project is created for educational purposes as part of the OASIS Infobyte internship program.

---

## 🙋 Support

If you encounter any issues:

1. Check the **Troubleshooting** section above
2. Verify your API key is valid and activated
3. Ensure all dependencies are installed
4. Check your internet connection

---

## 👨‍💻 Author

Created as part of OASIS Infobyte Web Development Internship

---

## 🎓 Learning Outcomes

By completing this project, you will have learned:

- How to integrate external APIs in Python applications
- Building professional GUI applications with Tkinter
- Handling asynchronous data and user interactions
- Error handling and input validation
- JSON data parsing and manipulation
- Creating user-friendly interfaces
- Working with datetime and timezone conversions
- Project structure and modular programming

---

**Enjoy using Weather Pro! ☀️🌧️❄️**
