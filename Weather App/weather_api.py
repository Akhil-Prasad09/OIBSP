"""
Weather API Module - Handles all API interactions with OpenWeatherMap
"""

import requests
import json
from datetime import datetime
import os


class WeatherAPI:
    def __init__(self, api_key=None):
        """Initialize the Weather API client"""
        # Try to load API key from config or environment
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = self.load_api_key()
        
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.geocoding_url = "http://api.openweathermap.org/geo/1.0"
    
    def load_api_key(self):
        """Load API key from config file or environment variable"""
        # Try to load from config.json
        if os.path.exists("config.json"):
            try:
                with open("config.json", "r") as f:
                    config = json.load(f)
                    return config.get("api_key", "")
            except:
                pass
        
        # Try environment variable
        api_key = os.environ.get("OPENWEATHER_API_KEY", "")
        
        if not api_key:
            raise ValueError(
                "API key not found. Please:\n"
                "1. Create a config.json file with your API key, OR\n"
                "2. Set OPENWEATHER_API_KEY environment variable\n\n"
                "Get your free API key at: https://openweathermap.org/api"
            )
        
        return api_key
    
    def get_current_weather(self, location, units="metric"):
        """
        Fetch current weather for a location
        
        Args:
            location: City name or ZIP code
            units: 'metric' for Celsius, 'imperial' for Fahrenheit
        
        Returns:
            Dictionary with weather data
        """
        try:
            # Build API URL
            url = f"{self.base_url}/weather"
            params = {
                "q": location,
                "appid": self.api_key,
                "units": units
            }
            
            # Make API request
            response = requests.get(url, params=params, timeout=10)
            
            # Check for errors
            if response.status_code == 401:
                raise Exception("Invalid API key. Please check your configuration.")
            elif response.status_code == 404:
                raise Exception(f"Location '{location}' not found. Please check the spelling.")
            elif response.status_code != 200:
                raise Exception(f"API Error: {response.status_code}")
            
            data = response.json()
            
            # Parse and return formatted data
            return self.parse_current_weather(data)
            
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Please check your internet connection.")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error. Please check your internet connection.")
        except Exception as e:
            raise Exception(f"Error fetching weather: {str(e)}")
    
    def parse_current_weather(self, data):
        """Parse current weather API response"""
        return {
            "name": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "visibility": data.get("visibility", 0),
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"].get("deg", 0),
            "description": data["weather"][0]["description"],
            "main": data["weather"][0]["main"],
            "icon": data["weather"][0]["icon"],
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def get_forecast(self, location, units="metric"):
        """
        Fetch 5-day weather forecast
        
        Args:
            location: City name or ZIP code
            units: 'metric' for Celsius, 'imperial' for Fahrenheit
        
        Returns:
            List of daily forecast data
        """
        try:
            # Build API URL
            url = f"{self.base_url}/forecast"
            params = {
                "q": location,
                "appid": self.api_key,
                "units": units
            }
            
            # Make API request
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code != 200:
                # If forecast fails, return empty list (optional feature)
                return []
            
            data = response.json()
            
            # Parse and return formatted forecast
            return self.parse_forecast(data)
            
        except Exception as e:
            # Return empty list if forecast fails (don't block main weather)
            print(f"Forecast error: {e}")
            return []
    
    def parse_forecast(self, data):
        """Parse forecast API response into daily summaries"""
        daily_data = {}
        
        # Group forecast data by day
        for item in data["list"]:
            # Get date
            dt = datetime.fromtimestamp(item["dt"])
            date_key = dt.strftime("%Y-%m-%d")
            day_name = dt.strftime("%a")  # Short day name (Mon, Tue, etc.)
            
            # Skip today, start from tomorrow
            if date_key == datetime.now().strftime("%Y-%m-%d"):
                continue
            
            if date_key not in daily_data:
                daily_data[date_key] = {
                    "day": day_name,
                    "temps": [],
                    "descriptions": [],
                    "date": date_key
                }
            
            # Collect temperature and description data
            daily_data[date_key]["temps"].append(item["main"]["temp"])
            daily_data[date_key]["descriptions"].append(item["weather"][0]["description"])
        
        # Calculate daily summaries
        forecast_list = []
        for date_key in sorted(daily_data.keys())[:5]:  # Get next 5 days
            day_info = daily_data[date_key]
            
            # Calculate min/max temps
            temps = day_info["temps"]
            temp_min = min(temps)
            temp_max = max(temps)
            
            # Get most common description
            descriptions = day_info["descriptions"]
            description = max(set(descriptions), key=descriptions.count)
            
            forecast_list.append({
                "day": day_info["day"],
                "date": date_key,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "description": description
            })
        
        return forecast_list
    
    def get_location_by_ip(self):
        """Get approximate location based on IP address (optional feature)"""
        try:
            response = requests.get("http://ip-api.com/json/", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get("city", "")
        except:
            pass
        return None
