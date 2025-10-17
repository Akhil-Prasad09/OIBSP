"""
BMI Calculator Pro - Core Engine
Unified BMI calculation, data management, and analysis engine.
"""

import json
import os
import datetime
from typing import Dict, List, Optional, Tuple
import statistics


class BMICalculatorPro:
    """Professional BMI Calculator with comprehensive features."""
    
    # WHO BMI Categories
    BMI_CATEGORIES = {
        'severe_underweight': (0, 16),
        'underweight': (16, 18.5),
        'normal': (18.5, 25),
        'overweight': (25, 30),
        'obese_class_1': (30, 35),
        'obese_class_2': (35, 40),
        'obese_class_3': (40, float('inf'))
    }
    
    CATEGORY_INFO = {
        'severe_underweight': {
            'name': 'Severely Underweight',
            'color': '#8e44ad',
            'emoji': '🔴',
            'advice': 'Consult a healthcare provider immediately. This BMI indicates severe undernutrition.',
            'risk': 'Very High'
        },
        'underweight': {
            'name': 'Underweight',
            'color': '#3498db',
            'emoji': '🔵',
            'advice': 'Consider consulting a healthcare provider for a healthy weight gain plan.',
            'risk': 'Moderate'
        },
        'normal': {
            'name': 'Normal Weight',
            'color': '#2ecc71',
            'emoji': '🟢',
            'advice': 'Excellent! Maintain your healthy lifestyle with balanced diet and regular exercise.',
            'risk': 'Low'
        },
        'overweight': {
            'name': 'Overweight',
            'color': '#f39c12',
            'emoji': '🟡',
            'advice': 'Consider adopting a healthier diet and increasing physical activity.',
            'risk': 'Moderate'
        },
        'obese_class_1': {
            'name': 'Obesity Class I',
            'color': '#e67e22',
            'emoji': '🟠',
            'advice': 'Consult a healthcare provider for a comprehensive weight management plan.',
            'risk': 'High'
        },
        'obese_class_2': {
            'name': 'Obesity Class II',
            'color': '#e74c3c',
            'emoji': '🔴',
            'advice': 'Strongly recommend consulting a healthcare provider for medical supervision.',
            'risk': 'Very High'
        },
        'obese_class_3': {
            'name': 'Obesity Class III',
            'color': '#c0392b',
            'emoji': '⚫',
            'advice': 'Immediate medical consultation required. Consider bariatric surgery evaluation.',
            'risk': 'Extreme'
        }
    }
    
    def __init__(self):
        """Initialize the BMI Calculator Pro."""
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.data_file = os.path.join(self.data_dir, 'bmi_records.json')
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Ensure data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Create empty records file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)
    
    def convert_units(self, value: float, from_unit: str, to_unit: str, 
                     measurement_type: str) -> float:
        """Convert between different units."""
        if measurement_type == 'weight':
            conversions = {
                ('kg', 'kg'): 1.0,
                ('lbs', 'kg'): 0.453592,
                ('kg', 'lbs'): 2.20462,
                ('lbs', 'lbs'): 1.0,
                ('stone', 'kg'): 6.35029,
                ('kg', 'stone'): 0.157473
            }
        elif measurement_type == 'height':
            conversions = {
                ('m', 'm'): 1.0,
                ('cm', 'm'): 0.01,
                ('ft', 'm'): 0.3048,
                ('in', 'm'): 0.0254,
                ('m', 'cm'): 100.0,
                ('m', 'ft'): 3.28084,
                ('m', 'in'): 39.3701
            }
        else:
            return value
        
        return value * conversions.get((from_unit, to_unit), 1.0)
    
    def validate_input(self, weight: float, height: float, 
                      weight_unit: str = 'kg', height_unit: str = 'm') -> Tuple[bool, str]:
        """Validate BMI input parameters."""
        # Convert to standard units for validation
        weight_kg = self.convert_units(weight, weight_unit, 'kg', 'weight')
        height_m = self.convert_units(height, height_unit, 'm', 'height')
        
        if weight_kg <= 0:
            return False, "Weight must be a positive number"
        
        if height_m <= 0:
            return False, "Height must be a positive number"
        
        # Reasonable ranges for human measurements
        if weight_kg < 10 or weight_kg > 650:  # 10kg to 650kg
            return False, f"Weight must be between 10-650 kg ({self.convert_units(10, 'kg', weight_unit, 'weight'):.1f}-{self.convert_units(650, 'kg', weight_unit, 'weight'):.1f} {weight_unit})"
        
        if height_m < 0.5 or height_m > 2.8:  # 0.5m to 2.8m
            return False, f"Height must be between 0.5-2.8 meters ({self.convert_units(0.5, 'm', height_unit, 'height'):.1f}-{self.convert_units(2.8, 'm', height_unit, 'height'):.1f} {height_unit})"
        
        return True, ""
    
    def calculate_bmi(self, weight: float, height: float,
                     weight_unit: str = 'kg', height_unit: str = 'm') -> float:
        """Calculate BMI with unit conversion."""
        # Convert to standard units (kg, m)
        weight_kg = self.convert_units(weight, weight_unit, 'kg', 'weight')
        height_m = self.convert_units(height, height_unit, 'm', 'height')
        
        return weight_kg / (height_m ** 2)
    
    def categorize_bmi(self, bmi: float) -> str:
        """Categorize BMI value."""
        for category, (lower, upper) in self.BMI_CATEGORIES.items():
            if lower <= bmi < upper:
                return category
        return 'unknown'
    
    def get_bmi_analysis(self, bmi: float) -> Dict:
        """Get comprehensive BMI analysis."""
        category = self.categorize_bmi(bmi)
        info = self.CATEGORY_INFO.get(category, {})
        
        # Calculate ideal weight range (BMI 18.5-24.9)
        def ideal_weight_range(height_m: float) -> Tuple[float, float]:
            min_weight = 18.5 * (height_m ** 2)
            max_weight = 24.9 * (height_m ** 2)
            return min_weight, max_weight
        
        return {
            'category': category,
            'category_name': info.get('name', 'Unknown'),
            'color': info.get('color', '#95a5a6'),
            'emoji': info.get('emoji', '⚪'),
            'advice': info.get('advice', 'Consult a healthcare professional.'),
            'risk_level': info.get('risk', 'Unknown'),
            'bmi_range': self.BMI_CATEGORIES.get(category, (0, 0))
        }
    
    def save_record(self, name: str, age: int, gender: str, weight: float, height: float,
                   weight_unit: str = 'kg', height_unit: str = 'm') -> bool:
        """Save BMI record with comprehensive data."""
        try:
            # Calculate BMI
            bmi = self.calculate_bmi(weight, height, weight_unit, height_unit)
            analysis = self.get_bmi_analysis(bmi)
            
            # Convert to standard units for storage
            weight_kg = self.convert_units(weight, weight_unit, 'kg', 'weight')
            height_m = self.convert_units(height, height_unit, 'm', 'height')
            
            record = {
                'id': datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f'),
                'name': name.strip(),
                'age': age,
                'gender': gender,
                'weight_kg': round(weight_kg, 2),
                'height_m': round(height_m, 3),
                'weight_input': weight,
                'height_input': height,
                'weight_unit': weight_unit,
                'height_unit': height_unit,
                'bmi': round(bmi, 2),
                'category': analysis['category'],
                'category_name': analysis['category_name'],
                'risk_level': analysis['risk_level'],
                'timestamp': datetime.datetime.now().isoformat(),
                'date': datetime.date.today().isoformat()
            }
            
            # Load existing records
            records = self.load_records()
            records.append(record)
            
            # Save updated records
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(records, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving record: {e}")
            return False
    
    def load_records(self) -> List[Dict]:
        """Load all BMI records."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading records: {e}")
        return []
    
    def get_user_records(self, name: str) -> List[Dict]:
        """Get records for a specific user."""
        all_records = self.load_records()
        return [r for r in all_records if r.get('name', '').lower() == name.lower()]
    
    def get_statistics(self, records: List[Dict] = None) -> Dict:
        """Calculate comprehensive statistics."""
        if records is None:
            records = self.load_records()
        
        if not records:
            return {}
        
        bmis = [r['bmi'] for r in records]
        weights = [r['weight_kg'] for r in records]
        ages = [r['age'] for r in records if 'age' in r]
        
        # BMI statistics
        bmi_stats = {
            'count': len(bmis),
            'mean': statistics.mean(bmis),
            'median': statistics.median(bmis),
            'min': min(bmis),
            'max': max(bmis),
            'stdev': statistics.stdev(bmis) if len(bmis) > 1 else 0
        }
        
        # Category distribution
        categories = {}
        for record in records:
            cat = record.get('category_name', 'Unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        # Gender distribution
        genders = {}
        for record in records:
            gender = record.get('gender', 'Unknown')
            genders[gender] = genders.get(gender, 0) + 1
        
        # Age statistics
        age_stats = {}
        if ages:
            age_stats = {
                'mean': statistics.mean(ages),
                'median': statistics.median(ages),
                'min': min(ages),
                'max': max(ages)
            }
        
        # Recent trends (last 30 days)
        recent_date = datetime.datetime.now() - datetime.timedelta(days=30)
        recent_records = [
            r for r in records 
            if datetime.datetime.fromisoformat(r['timestamp']) > recent_date
        ]
        
        return {
            'total_records': len(records),
            'unique_users': len(set(r.get('name', '') for r in records if r.get('name'))),
            'bmi_statistics': bmi_stats,
            'category_distribution': categories,
            'gender_distribution': genders,
            'age_statistics': age_stats,
            'recent_records_count': len(recent_records),
            'date_range': {
                'first': min(r['timestamp'] for r in records)[:10] if records else None,
                'last': max(r['timestamp'] for r in records)[:10] if records else None
            }
        }
    
    def delete_record(self, record_id: str) -> bool:
        """Delete a specific record by ID."""
        try:
            records = self.load_records()
            original_count = len(records)
            records = [r for r in records if r.get('id') != record_id]
            
            if len(records) < original_count:
                with open(self.data_file, 'w', encoding='utf-8') as f:
                    json.dump(records, f, indent=2, ensure_ascii=False)
                return True
            return False
        except Exception as e:
            print(f"Error deleting record: {e}")
            return False
    
    def export_data(self, format_type: str = 'json', records: List[Dict] = None) -> str:
        """Export data in various formats."""
        if records is None:
            records = self.load_records()
        
        if format_type.lower() == 'json':
            return json.dumps(records, indent=2, ensure_ascii=False)
        
        elif format_type.lower() == 'csv':
            import csv
            import io
            
            output = io.StringIO()
            if records:
                fieldnames = records[0].keys()
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(records)
            
            return output.getvalue()
        
        return ""
    
    def generate_report(self, user_name: str = None) -> str:
        """Generate comprehensive BMI report."""
        if user_name:
            records = self.get_user_records(user_name)
            title = f"BMI Report for {user_name}"
        else:
            records = self.load_records()
            title = "Comprehensive BMI Report"
        
        if not records:
            return f"{title}\n\nNo records found."
        
        stats = self.get_statistics(records)
        latest = max(records, key=lambda x: x['timestamp'])
        
        report = f"""
{title}
{'=' * len(title)}

SUMMARY
-------
Total Records: {stats['total_records']}
Date Range: {stats['date_range']['first']} to {stats['date_range']['last']}
Unique Users: {stats['unique_users']}

LATEST RECORD
-------------
Date: {latest['timestamp'][:10]}
BMI: {latest['bmi']} ({latest['category_name']})
Risk Level: {latest['risk_level']}

BMI STATISTICS
--------------
Average: {stats['bmi_statistics']['mean']:.2f}
Median: {stats['bmi_statistics']['median']:.2f}
Range: {stats['bmi_statistics']['min']:.2f} - {stats['bmi_statistics']['max']:.2f}
Standard Deviation: {stats['bmi_statistics']['stdev']:.2f}

CATEGORY DISTRIBUTION
--------------------
"""
        for category, count in stats['category_distribution'].items():
            percentage = (count / stats['total_records']) * 100
            report += f"{category}: {count} records ({percentage:.1f}%)\n"
        
        if stats['gender_distribution']:
            report += "\nGENDER DISTRIBUTION\n-------------------\n"
            for gender, count in stats['gender_distribution'].items():
                percentage = (count / stats['total_records']) * 100
                report += f"{gender}: {count} records ({percentage:.1f}%)\n"
        
        report += f"\nReport generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return report