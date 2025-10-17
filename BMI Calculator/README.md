# BMI Calculator Pro 🏥

> **Professional Health Analytics & BMI Management System**

A comprehensive, feature-rich BMI (Body Mass Index) calculator built with Python that provides advanced health analytics, data visualization, and professional reporting capabilities.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 🌟 Features

### 📊 Advanced BMI Calculation
- **WHO Standard Categories**: Complete BMI categorization following World Health Organization guidelines
- **Multiple Unit Support**: Convert between kg/lbs/stone (weight) and m/cm/ft/in (height)
- **Comprehensive Analysis**: Detailed health risk assessment with personalized advice
- **Input Validation**: Robust error checking and user-friendly feedback

### 📋 Health Records Management
- **Persistent Storage**: Automatic saving of all BMI calculations in JSON format
- **Historical Tracking**: View and manage all previous BMI records
- **Search & Filter**: Find specific records quickly
- **Data Export**: Export health records to CSV format

### 📈 Data Visualization & Analytics
- **BMI Distribution Charts**: Histogram showing BMI distribution across records
- **Category Analysis**: Pie charts displaying BMI category breakdowns
- **Interactive Charts**: Professional matplotlib-based visualizations
- **Export Charts**: Save charts as PNG, JPEG, or PDF files

### 📄 Professional Reporting
- **Comprehensive Reports**: Generate detailed health analytics reports
- **Statistical Analysis**: Mean, median, trends, and demographic breakdowns
- **Export Reports**: Save reports as text files
- **Print Ready**: Formatted reports ready for printing or sharing

### 🎨 Modern User Interface
- **Professional Design**: Clean, modern GUI built with Tkinter
- **Tabbed Interface**: Organized sections for different functionalities
- **Responsive Layout**: Adapts to different screen sizes
- **Smooth Animations**: Professional fade-in effects and transitions
- **Status Updates**: Real-time feedback and progress indicators

## 🚀 Quick Start

### Windows Users (Recommended)
1. **Download the Repository**
   ```bash
   git clone https://github.com/yourusername/bmi-calculator-pro.git
   cd bmi-calculator-pro
   ```

2. **Run with Batch File**
   ```bash
   # Double-click or run from command line
   run.bat
   ```
   The batch file will automatically:
   - Check Python installation
   - Install required dependencies
   - Launch the application

### Manual Installation (All Platforms)

#### Prerequisites
- **Python 3.7 or higher** (download from [python.org](https://python.org/downloads/))
- **pip** (comes with Python)

#### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bmi-calculator-pro.git
   cd bmi-calculator-pro
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python bmi_calculator_pro_clean.py
   ```

## 📁 Project Structure

```
BMI Calculator Pro/
├── bmi_calculator_pro_clean.py    # Main GUI application
├── bmi_engine.py                  # Core BMI calculation engine
├── run.bat                        # Windows batch launcher
├── requirements.txt               # Python dependencies
├── README.md                      # Documentation
└── bmi_records.json              # Health records (created automatically)
```

## 💻 Usage Guide

### 1. BMI Calculation
- Enter your **full name**, **age**, and **gender**
- Input your **weight** and **height** with preferred units
- Click **"🧮 Calculate BMI"** to get instant results
- View detailed analysis including:
  - BMI value and WHO category
  - Health risk assessment
  - Personalized health advice
  - Ideal weight range

### 2. Health Records
- All calculations are automatically saved
- View historical BMI data in a sortable table
- Search records by name, category, or risk level
- Export data to CSV for external analysis

### 3. Analytics & Charts
- Generate various chart types:
  - **BMI Distribution**: Histogram showing BMI spread
  - **Category Analysis**: Pie chart of BMI categories
- Interactive matplotlib charts with professional styling
- Save charts in multiple formats (PNG, JPEG, PDF)

### 4. Reports
- Generate comprehensive health reports
- Statistical analysis of all records
- Formatted text reports ready for printing
- Save reports as text files

## 🔧 Technical Details

### Core Technologies
- **Python 3.7+**: Main programming language
- **Tkinter**: GUI framework (built-in with Python)
- **Matplotlib**: Data visualization and charting
- **NumPy**: Numerical computations
- **Seaborn**: Enhanced statistical plots

### BMI Categories (WHO Standard)
| BMI Range | Category | Risk Level |
|-----------|----------|------------|
| < 16.0 | Severe Underweight | High |
| 16.0 - 18.4 | Underweight | Moderate |
| 18.5 - 24.9 | Normal Weight | Low |
| 25.0 - 29.9 | Overweight | Moderate |
| 30.0 - 34.9 | Obese Class I | High |
| 35.0 - 39.9 | Obese Class II | Very High |
| ≥ 40.0 | Obese Class III | Extreme |

### Data Storage
- **Format**: JSON for structured data storage
- **Location**: `bmi_records.json` in application directory
- **Backup**: Manual backup recommended for important data
- **Privacy**: All data stored locally on your machine

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found a bug? Open an issue with details
- 💡 **Feature Requests**: Suggest new features or improvements
- 📝 **Documentation**: Help improve documentation
- 🔧 **Code Contributions**: Submit pull requests

### Development Setup
1. **Fork the Repository**
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Development Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Make Changes and Test**
5. **Submit a Pull Request**

## 📋 Roadmap

### Planned Features
- [ ] **Multi-language Support**: Internationalization
- [ ] **Cloud Sync**: Optional cloud storage for records
- [ ] **Mobile App**: Companion mobile application
- [ ] **Advanced Analytics**: Machine learning insights
- [ ] **Diet Integration**: Meal planning and nutrition tracking
- [ ] **Exercise Integration**: Activity tracking and recommendations
- [ ] **Medical Integration**: Healthcare provider sharing
- [ ] **Custom Themes**: User interface customization

## 🐛 Troubleshooting

### Common Issues

#### "Python is not installed or not in PATH"
- **Solution**: Install Python from [python.org](https://python.org/downloads/)
- **Windows**: Check "Add Python to PATH" during installation
- **Verify**: Run `python --version` in command prompt

#### "No module named 'matplotlib'"
- **Solution**: Install dependencies with `pip install -r requirements.txt`
- **Alternative**: Run `pip install matplotlib numpy seaborn`

#### Charts not displaying correctly
- **Solution**: Ensure matplotlib backend is properly configured
- **Linux**: May need to install `python3-tk` package

#### Application won't start
- **Check**: Python version (3.7+ required)
- **Check**: All dependencies installed
- **Check**: File permissions

### Getting Help
- 📖 Check the [Issues](../../issues) page for known problems
- 💬 Open a new issue with detailed error messages
- 🔍 Include system information (OS, Python version)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 BMI Calculator Pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 👨‍💻 Authors

- **Your Name** - *Initial work* - [YourUsername](https://github.com/yourusername)

## 🙏 Acknowledgments

- **World Health Organization** for BMI category standards
- **Python Community** for excellent libraries and frameworks
- **Matplotlib Team** for powerful visualization capabilities
- **Contributors** who help improve this project

## 📊 Statistics

- **Lines of Code**: ~1,500+
- **Functions**: 50+
- **Classes**: 2 main classes
- **Features**: 15+ major features
- **Supported Platforms**: Windows, macOS, Linux

## 🔗 Links

- 📖 **Documentation**: [Wiki](../../wiki)
- 🐛 **Bug Reports**: [Issues](../../issues)
- 💡 **Feature Requests**: [Discussions](../../discussions)
- 📧 **Contact**: [your.email@example.com](mailto:your.email@example.com)

---

**⭐ If this project helped you, please consider giving it a star!**

*Made with ❤️ for health and wellness*