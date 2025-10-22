"""
Professional Weather App with Tkinter GUI - DEMO MODE
OASIS Infobyte Internship Project
This version works with sample data (no API key required)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class WeatherAppDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Pro - Real-Time Weather Information [DEMO MODE]")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Temperature unit (default Celsius)
        self.unit = tk.StringVar(value="metric")
        
        # Color scheme
        self.bg_color = "#1a1a2e"
        self.card_bg = "#16213e"
        self.accent_color = "#0f3460"
        self.text_color = "#eaeaea"
        self.highlight_color = "#e94560"
        
        # Sample data for different cities
        self.sample_data = {
            "london": {
                "name": "London",
                "country": "GB",
                "temperature_c": 15.5,
                "temperature_f": 59.9,
                "feels_like_c": 13.2,
                "feels_like_f": 55.8,
                "humidity": 72,
                "pressure": 1013,
                "visibility": 10000,
                "wind_speed_ms": 5.5,
                "wind_speed_mph": 12.3,
                "description": "partly cloudy",
                "sunrise": "06:45 AM",
                "sunset": "06:30 PM"
            },
            "new york": {
                "name": "New York",
                "country": "US",
                "temperature_c": 22.3,
                "temperature_f": 72.1,
                "feels_like_c": 21.8,
                "feels_like_f": 71.2,
                "humidity": 65,
                "pressure": 1015,
                "visibility": 16000,
                "wind_speed_ms": 4.2,
                "wind_speed_mph": 9.4,
                "description": "clear sky",
                "sunrise": "06:20 AM",
                "sunset": "07:45 PM"
            },
            "tokyo": {
                "name": "Tokyo",
                "country": "JP",
                "temperature_c": 18.7,
                "temperature_f": 65.7,
                "feels_like_c": 17.9,
                "feels_like_f": 64.2,
                "humidity": 78,
                "pressure": 1010,
                "visibility": 10000,
                "wind_speed_ms": 3.8,
                "wind_speed_mph": 8.5,
                "description": "light rain",
                "sunrise": "05:30 AM",
                "sunset": "05:50 PM"
            },
            "paris": {
                "name": "Paris",
                "country": "FR",
                "temperature_c": 16.8,
                "temperature_f": 62.2,
                "feels_like_c": 15.5,
                "feels_like_f": 59.9,
                "humidity": 68,
                "pressure": 1012,
                "visibility": 12000,
                "wind_speed_ms": 4.5,
                "wind_speed_mph": 10.1,
                "description": "scattered clouds",
                "sunrise": "07:00 AM",
                "sunset": "06:15 PM"
            },
            "sydney": {
                "name": "Sydney",
                "country": "AU",
                "temperature_c": 24.5,
                "temperature_f": 76.1,
                "feels_like_c": 23.8,
                "feels_like_f": 74.8,
                "humidity": 60,
                "pressure": 1018,
                "visibility": 15000,
                "wind_speed_ms": 6.2,
                "wind_speed_mph": 13.9,
                "description": "clear sky",
                "sunrise": "05:45 AM",
                "sunset": "07:30 PM"
            }
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main user interface"""
        self.root.configure(bg=self.bg_color)
        
        # Main container with padding
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ===== HEADER SECTION =====
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        title_label = tk.Label(
            header_frame,
            text="☀ Weather Pro [DEMO MODE]",
            font=("Segoe UI", 28, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Real-time weather information worldwide - Try: London, New York, Tokyo, Paris, Sydney",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg="#a0a0a0"
        )
        subtitle_label.pack()
        
        demo_label = tk.Label(
            header_frame,
            text="⚠️ Using sample data - Configure your API key in config.json for real weather",
            font=("Segoe UI", 9, "italic"),
            bg=self.bg_color,
            fg="#ffa500"
        )
        demo_label.pack(pady=(5, 0))
        
        # ===== SEARCH SECTION =====
        search_card = tk.Frame(main_frame, bg=self.card_bg, relief=tk.RAISED, bd=2)
        search_card.pack(fill=tk.X, pady=(0, 20))
        
        search_inner = tk.Frame(search_card, bg=self.card_bg)
        search_inner.pack(padx=20, pady=20)
        
        # Location input
        location_label = tk.Label(
            search_inner,
            text="Enter City Name:",
            font=("Segoe UI", 12, "bold"),
            bg=self.card_bg,
            fg=self.text_color
        )
        location_label.grid(row=0, column=0, sticky="w", pady=(0, 10))
        
        input_frame = tk.Frame(search_inner, bg=self.card_bg)
        input_frame.grid(row=1, column=0, sticky="ew")
        
        self.location_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 14),
            width=30,
            relief=tk.FLAT,
            bg="#ffffff",
            fg="#000000"
        )
        self.location_entry.pack(side=tk.LEFT, ipady=8, padx=(0, 10))
        self.location_entry.bind("<Return>", lambda e: self.search_weather())
        
        # Search button
        self.search_btn = tk.Button(
            input_frame,
            text="🔍 Search Weather",
            font=("Segoe UI", 12, "bold"),
            bg=self.highlight_color,
            fg="#ffffff",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.search_weather,
            padx=20,
            pady=10
        )
        self.search_btn.pack(side=tk.LEFT)
        self.search_btn.bind("<Enter>", lambda e: self.search_btn.config(bg="#d63850"))
        self.search_btn.bind("<Leave>", lambda e: self.search_btn.config(bg=self.highlight_color))
        
        # Unit toggle
        unit_frame = tk.Frame(search_inner, bg=self.card_bg)
        unit_frame.grid(row=2, column=0, pady=(15, 0))
        
        tk.Label(
            unit_frame,
            text="Units:",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.text_color
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        celsius_radio = tk.Radiobutton(
            unit_frame,
            text="Celsius (°C)",
            variable=self.unit,
            value="metric",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.text_color,
            selectcolor=self.accent_color,
            activebackground=self.card_bg,
            activeforeground=self.text_color
        )
        celsius_radio.pack(side=tk.LEFT, padx=5)
        
        fahrenheit_radio = tk.Radiobutton(
            unit_frame,
            text="Fahrenheit (°F)",
            variable=self.unit,
            value="imperial",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.text_color,
            selectcolor=self.accent_color,
            activebackground=self.card_bg,
            activeforeground=self.text_color
        )
        fahrenheit_radio.pack(side=tk.LEFT, padx=5)
        
        # ===== CURRENT WEATHER SECTION =====
        current_card = tk.Frame(main_frame, bg=self.card_bg, relief=tk.RAISED, bd=2)
        current_card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        current_inner = tk.Frame(current_card, bg=self.card_bg)
        current_inner.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Current weather title
        tk.Label(
            current_inner,
            text="Current Weather",
            font=("Segoe UI", 16, "bold"),
            bg=self.card_bg,
            fg=self.text_color
        ).pack(anchor="w", pady=(0, 15))
        
        # Current weather display frame
        self.current_display = tk.Frame(current_inner, bg=self.card_bg)
        self.current_display.pack(fill=tk.BOTH, expand=True)
        
        # Initial message
        self.initial_label = tk.Label(
            self.current_display,
            text="Enter a location and search to view weather information\nTry: London, New York, Tokyo, Paris, or Sydney",
            font=("Segoe UI", 12),
            bg=self.card_bg,
            fg="#808080"
        )
        self.initial_label.pack(expand=True)
        
        # ===== FORECAST SECTION =====
        forecast_card = tk.Frame(main_frame, bg=self.card_bg, relief=tk.RAISED, bd=2)
        forecast_card.pack(fill=tk.X)
        
        forecast_inner = tk.Frame(forecast_card, bg=self.card_bg)
        forecast_inner.pack(padx=20, pady=20, fill=tk.X)
        
        tk.Label(
            forecast_inner,
            text="5-Day Forecast",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_bg,
            fg=self.text_color
        ).pack(anchor="w", pady=(0, 10))
        
        self.forecast_frame = tk.Frame(forecast_inner, bg=self.card_bg)
        self.forecast_frame.pack(fill=tk.X)
        
    def search_weather(self):
        """Search and display weather for the entered location"""
        location = self.location_entry.get().strip().lower()
        
        if not location:
            messagebox.showwarning("Input Required", "Please enter a city name")
            return
        
        # Show loading state
        self.search_btn.config(text="Loading...", state=tk.DISABLED)
        self.root.update()
        
        try:
            # Get sample data
            if location in self.sample_data:
                data = self.sample_data[location]
                unit_system = self.unit.get()
                
                # Display weather
                self.display_current_weather(data, unit_system)
                self.display_forecast(data, unit_system)
            else:
                messagebox.showinfo(
                    "Demo Mode",
                    f"City '{location}' not available in demo mode.\n\n"
                    "Available cities:\n• London\n• New York\n• Tokyo\n• Paris\n• Sydney\n\n"
                    "Configure your API key in config.json for real weather data!"
                )
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.search_btn.config(text="🔍 Search Weather", state=tk.NORMAL)
    
    def display_current_weather(self, data, unit_system):
        """Display current weather information"""
        # Clear previous display
        for widget in self.current_display.winfo_children():
            widget.destroy()
        
        # Create display layout
        display_frame = tk.Frame(self.current_display, bg=self.card_bg)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - main info
        left_frame = tk.Frame(display_frame, bg=self.card_bg)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Location and date
        location_text = f"{data['name']}, {data['country']}"
        tk.Label(
            left_frame,
            text=location_text,
            font=("Segoe UI", 20, "bold"),
            bg=self.card_bg,
            fg=self.text_color
        ).pack(anchor="w")
        
        date_text = datetime.now().strftime("%A, %B %d, %Y")
        tk.Label(
            left_frame,
            text=date_text,
            font=("Segoe UI", 11),
            bg=self.card_bg,
            fg="#a0a0a0"
        ).pack(anchor="w", pady=(5, 20))
        
        # Temperature
        if unit_system == "metric":
            temp = data['temperature_c']
            feels_like = data['feels_like_c']
            unit_symbol = "°C"
        else:
            temp = data['temperature_f']
            feels_like = data['feels_like_f']
            unit_symbol = "°F"
        
        temp_text = f"{temp:.1f}{unit_symbol}"
        tk.Label(
            left_frame,
            text=temp_text,
            font=("Segoe UI", 56, "bold"),
            bg=self.card_bg,
            fg=self.highlight_color
        ).pack(anchor="w")
        
        # Feels like
        feels_like_text = f"Feels like {feels_like:.1f}{unit_symbol}"
        tk.Label(
            left_frame,
            text=feels_like_text,
            font=("Segoe UI", 12),
            bg=self.card_bg,
            fg="#a0a0a0"
        ).pack(anchor="w", pady=(5, 15))
        
        # Weather description
        description = data['description'].title()
        tk.Label(
            left_frame,
            text=f"☁ {description}",
            font=("Segoe UI", 14),
            bg=self.card_bg,
            fg=self.text_color
        ).pack(anchor="w")
        
        # Right side - additional info
        right_frame = tk.Frame(display_frame, bg=self.card_bg)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(20, 0))
        
        # Create info grid
        wind_speed = data['wind_speed_ms'] if unit_system == 'metric' else data['wind_speed_mph']
        wind_unit = 'm/s' if unit_system == 'metric' else 'mph'
        
        info_items = [
            ("💧 Humidity", f"{data['humidity']}%"),
            ("💨 Wind Speed", f"{wind_speed} {wind_unit}"),
            ("🎯 Pressure", f"{data['pressure']} hPa"),
            ("👁 Visibility", f"{data['visibility'] / 1000:.1f} km"),
            ("🌅 Sunrise", data['sunrise']),
            ("🌇 Sunset", data['sunset'])
        ]
        
        for i, (label, value) in enumerate(info_items):
            item_frame = tk.Frame(right_frame, bg=self.accent_color)
            item_frame.pack(fill=tk.X, pady=5)
            
            tk.Label(
                item_frame,
                text=label,
                font=("Segoe UI", 10, "bold"),
                bg=self.accent_color,
                fg="#a0a0a0",
                anchor="w"
            ).pack(fill=tk.X, padx=15, pady=(8, 2))
            
            tk.Label(
                item_frame,
                text=value,
                font=("Segoe UI", 12, "bold"),
                bg=self.accent_color,
                fg=self.text_color,
                anchor="w"
            ).pack(fill=tk.X, padx=15, pady=(2, 8))
    
    def display_forecast(self, data, unit_system):
        """Display 5-day forecast"""
        # Clear previous forecast
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()
        
        # Generate sample forecast
        forecast_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        
        base_temp_c = data['temperature_c']
        base_temp_f = data['temperature_f']
        
        for i, day in enumerate(forecast_days):
            day_frame = tk.Frame(self.forecast_frame, bg=self.accent_color, relief=tk.RAISED, bd=1)
            day_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            
            # Day name
            tk.Label(
                day_frame,
                text=day,
                font=("Segoe UI", 11, "bold"),
                bg=self.accent_color,
                fg=self.text_color
            ).pack(pady=(10, 5))
            
            # Weather icon representation
            icons = ["☀", "🌤", "☁", "🌧", "⛈"]
            icon_text = icons[i % len(icons)]
            tk.Label(
                day_frame,
                text=icon_text,
                font=("Segoe UI", 28),
                bg=self.accent_color
            ).pack(pady=5)
            
            # Temperature range (vary by +/- 3 degrees)
            if unit_system == "metric":
                temp_max = base_temp_c + (i - 2)
                temp_min = base_temp_c - (3 + i % 3)
            else:
                temp_max = base_temp_f + (i - 2)
                temp_min = base_temp_f - (3 + i % 3)
            
            temp_text = f"{temp_max:.0f}° / {temp_min:.0f}°"
            tk.Label(
                day_frame,
                text=temp_text,
                font=("Segoe UI", 11, "bold"),
                bg=self.accent_color,
                fg=self.highlight_color
            ).pack(pady=5)
            
            # Description
            descriptions = ["Clear", "Partly cloudy", "Cloudy", "Rain", "Storms"]
            tk.Label(
                day_frame,
                text=descriptions[i],
                font=("Segoe UI", 9),
                bg=self.accent_color,
                fg="#a0a0a0",
                wraplength=100
            ).pack(pady=(0, 10))


def main():
    root = tk.Tk()
    app = WeatherAppDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
