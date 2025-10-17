#!/usr/bin/env python3
"""
BMI Calculator Pro - Professional Health Analytics & Management
A comprehensive BMI calculator with advanced features including
data visualization, health analytics, and detailed reporting.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta
from bmi_engine import BMICalculatorPro


class BMICalculatorProGUI:
    def __init__(self, root):
        self.root = root
        self.bmi_engine = BMICalculatorPro()
        
        self.setup_window()
        self.setup_styles()
        self.create_interface()
        self.animate_startup()
    
    def setup_window(self):
        """Configure the main window."""
        self.root.title("BMI Calculator Pro - Professional Health Analytics")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")
        
        # Configure colors
        self.root.configure(bg='#f8f9fa')
        
        # Window icon (optional)
        try:
            self.root.iconname("BMI Calculator Pro")
        except:
            pass
    
    def setup_styles(self):
        """Configure custom styles."""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Custom styles for better appearance
        self.style.configure('Title.TLabel', 
                           font=('Arial', 16, 'bold'), 
                           foreground='#2c3e50')
        
        self.style.configure('Header.TLabel', 
                           font=('Arial', 12, 'bold'), 
                           foreground='#34495e')
    
    def create_interface(self):
        """Create the main interface."""
        # Status bar first
        self.create_status_bar(self.root)
        
        # Create main container
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Header
        self.create_header(main_frame)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True, pady=(10, 0))
        
        # Create tabs
        self.create_calculator_tab()
        self.create_records_tab()
        self.create_analytics_tab()
        self.create_reports_tab()
    
    def create_header(self, parent):
        """Create the application header."""
        header_frame = tk.Frame(parent, bg='#f8f9fa', height=80)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Left side - Title
        left_frame = tk.Frame(header_frame, bg='#f8f9fa')
        left_frame.pack(side='left', fill='y', padx=20)
        
        title_label = tk.Label(
            left_frame,
            text="BMI Calculator Pro",
            font=('Arial', 24, 'bold'),
            fg='#2c3e50',
            bg='#f8f9fa'
        )
        title_label.pack(anchor='w', pady=(10, 0))
        
        subtitle = tk.Label(
            left_frame,
            text="Professional Health Analytics & BMI Management",
            font=('Arial', 12),
            fg='#7f8c8d',
            bg='#f8f9fa'
        )
        subtitle.pack(anchor='w', pady=(0, 10))
    
    def create_calculator_tab(self):
        """Create the BMI calculator tab."""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="🧮 BMI Calculator")
        
        # Main container
        container = ttk.Frame(calc_frame)
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Left panel - Input form
        left_panel = tk.Frame(container, bg='white', relief='solid', bd=1)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Form header
        form_header = tk.Frame(left_panel, bg='#3498db', height=50)
        form_header.pack(fill='x')
        form_header.pack_propagate(False)
        
        header_label = tk.Label(
            form_header,
            text="BMI Calculation",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#3498db'
        )
        header_label.pack(expand=True)
        
        # Form content
        form_content = tk.Frame(left_panel, bg='white', padx=20, pady=20)
        form_content.pack(fill='both', expand=True)
        
        # Personal Information
        personal_frame = tk.LabelFrame(
            form_content, 
            text="Personal Information", 
            font=('Arial', 11, 'bold'),
            bg='white',
            padx=10,
            pady=10
        )
        personal_frame.pack(fill='x', pady=(0, 15))
        
        # Name
        tk.Label(personal_frame, text="Full Name:", bg='white', 
                font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        self.name_var = tk.StringVar()
        name_entry = tk.Entry(personal_frame, textvariable=self.name_var, 
                             font=('Arial', 11), width=25)
        name_entry.grid(row=0, column=1, sticky='ew', padx=(10, 0), pady=5)
        
        # Age
        tk.Label(personal_frame, text="Age:", bg='white', 
                font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        self.age_var = tk.StringVar()
        age_entry = tk.Entry(personal_frame, textvariable=self.age_var, 
                            font=('Arial', 11), width=25)
        age_entry.grid(row=1, column=1, sticky='ew', padx=(10, 0), pady=5)
        
        # Gender
        tk.Label(personal_frame, text="Gender:", bg='white', 
                font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=5)
        self.gender_var = tk.StringVar(value='Select')
        gender_combo = ttk.Combobox(personal_frame, textvariable=self.gender_var,
                                   values=['Male', 'Female', 'Other'], 
                                   state='readonly', width=22)
        gender_combo.grid(row=2, column=1, sticky='ew', padx=(10, 0), pady=5)
        
        personal_frame.columnconfigure(1, weight=1)
        
        # Measurements
        measurements_frame = tk.LabelFrame(
            form_content, 
            text="Body Measurements", 
            font=('Arial', 11, 'bold'),
            bg='white',
            padx=10,
            pady=10
        )
        measurements_frame.pack(fill='x', pady=(0, 15))
        
        # Weight
        weight_frame = tk.Frame(measurements_frame, bg='white')
        weight_frame.grid(row=0, column=0, columnspan=3, sticky='ew', pady=5)
        
        tk.Label(weight_frame, text="Weight:", bg='white', 
                font=('Arial', 10)).pack(side='left')
        
        self.weight_var = tk.StringVar()
        weight_entry = tk.Entry(weight_frame, textvariable=self.weight_var, 
                               font=('Arial', 11), width=15)
        weight_entry.pack(side='left', padx=(10, 5))
        
        self.weight_unit_var = tk.StringVar(value='kg')
        weight_unit_combo = ttk.Combobox(weight_frame, textvariable=self.weight_unit_var,
                                        values=['kg', 'lbs', 'stone'], 
                                        state='readonly', width=8)
        weight_unit_combo.pack(side='left')
        
        # Height
        height_frame = tk.Frame(measurements_frame, bg='white')
        height_frame.grid(row=1, column=0, columnspan=3, sticky='ew', pady=5)
        
        tk.Label(height_frame, text="Height:", bg='white', 
                font=('Arial', 10)).pack(side='left')
        
        self.height_var = tk.StringVar()
        height_entry = tk.Entry(height_frame, textvariable=self.height_var, 
                               font=('Arial', 11), width=15)
        height_entry.pack(side='left', padx=(10, 5))
        
        self.height_unit_var = tk.StringVar(value='m')
        height_unit_combo = ttk.Combobox(height_frame, textvariable=self.height_unit_var,
                                        values=['m', 'cm', 'ft', 'in'], 
                                        state='readonly', width=8)
        height_unit_combo.pack(side='left')
        
        measurements_frame.columnconfigure(0, weight=1)
        
        # Action buttons
        button_frame = tk.Frame(form_content, bg='white')
        button_frame.pack(fill='x', pady=(15, 0))
        
        calc_button = tk.Button(
            button_frame,
            text="🧮 Calculate BMI",
            font=('Arial', 12, 'bold'),
            bg='#2ecc71',
            fg='white',
            activebackground='#27ae60',
            activeforeground='white',
            relief='flat',
            padx=30,
            pady=12,
            cursor='hand2',
            command=self.calculate_bmi
        )
        calc_button.pack(side='left', padx=(0, 10))
        
        clear_button = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            relief='flat',
            padx=30,
            pady=12,
            cursor='hand2',
            command=self.clear_form
        )
        clear_button.pack(side='left')
        
        # Right panel - Results
        right_panel = tk.Frame(container, bg='white', relief='solid', bd=1)
        right_panel.pack(side='right', fill='both', expand=True)
        
        # Results header
        results_header = tk.Frame(right_panel, bg='#e74c3c', height=50)
        results_header.pack(fill='x')
        results_header.pack_propagate(False)
        
        results_header_label = tk.Label(
            results_header,
            text="📋 Results & Analysis",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#e74c3c'
        )
        results_header_label.pack(expand=True)
        
        # Results content
        self.results_content = tk.Frame(right_panel, bg='white', padx=20, pady=20)
        self.results_content.pack(fill='both', expand=True)
        
        # Initialize with welcome message
        welcome_label = tk.Label(
            self.results_content,
            text="Enter your information and click Calculate BMI\nto get comprehensive health analysis",
            font=('Arial', 12),
            fg='#7f8c8d',
            bg='white',
            justify='center'
        )
        welcome_label.pack(expand=True)
    
    def create_records_tab(self):
        """Create the records management tab."""
        records_frame = ttk.Frame(self.notebook)
        self.notebook.add(records_frame, text="📋 Health Records")
        
        # Container
        container = ttk.Frame(records_frame)
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Controls
        controls_frame = ttk.Frame(container)
        controls_frame.pack(fill='x', pady=(0, 15))
        
        # Search
        search_frame = ttk.Frame(controls_frame)
        search_frame.pack(side='left')
        
        ttk.Label(search_frame, text="Search:").pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side='left', padx=(5, 10))
        
        # Action buttons
        button_frame = ttk.Frame(controls_frame)
        button_frame.pack(side='right')
        
        ttk.Button(button_frame, text="🔄 Refresh", 
                  command=self.refresh_records).pack(side='left', padx=(0, 5))
        ttk.Button(button_frame, text="📊 Export CSV", 
                  command=self.export_csv).pack(side='left')
        
        # Records treeview
        tree_frame = ttk.Frame(container)
        tree_frame.pack(fill='both', expand=True)
        
        columns = ('Date', 'Name', 'Age', 'Gender', 'Weight', 'Height', 'BMI', 'Category')
        self.records_tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        for col in columns:
            self.records_tree.heading(col, text=col)
            self.records_tree.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', 
                                command=self.records_tree.yview)
        self.records_tree.configure(yscrollcommand=scrollbar.set)
        
        self.records_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Load initial records (defer to avoid status bar issue)
        self.root.after(100, self.refresh_records)
    
    def create_analytics_tab(self):
        """Create the analytics tab."""
        analytics_frame = ttk.Frame(self.notebook)
        self.notebook.add(analytics_frame, text="📈 Analytics")
        
        # Container
        container = ttk.Frame(analytics_frame)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Controls
        controls_frame = ttk.Frame(container)
        controls_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(controls_frame, text="Chart Type:").pack(side='left')
        self.chart_type_var = tk.StringVar(value='BMI Distribution')
        chart_combo = ttk.Combobox(controls_frame, textvariable=self.chart_type_var,
                                 values=['BMI Distribution', 'Category Analysis'],
                                 state='readonly', width=20)
        chart_combo.pack(side='left', padx=(5, 20))
        
        ttk.Button(controls_frame, text="📊 Generate Chart", 
                  command=self.generate_chart).pack(side='left')
        
        # Chart area
        chart_frame = ttk.LabelFrame(container, text="Data Visualization")
        chart_frame.pack(fill='both', expand=True)
        
        self.fig = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, chart_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=10, pady=10)
        
        # Generate initial chart (defer to avoid status bar issue)
        self.root.after(200, self.generate_chart)
    
    def create_reports_tab(self):
        """Create the reports tab."""
        reports_frame = ttk.Frame(self.notebook)
        self.notebook.add(reports_frame, text="📄 Reports")
        
        # Container
        container = ttk.Frame(reports_frame)
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Controls
        controls_frame = ttk.Frame(container)
        controls_frame.pack(fill='x', pady=(0, 15))
        
        ttk.Button(controls_frame, text="📄 Generate Report", 
                  command=self.generate_report).pack(side='left', padx=(0, 10))
        ttk.Button(controls_frame, text="💾 Save Report", 
                  command=self.save_report).pack(side='left')
        
        # Report display
        self.report_text = scrolledtext.ScrolledText(
            container, 
            wrap=tk.WORD, 
            font=('Consolas', 10),
            state='disabled'
        )
        self.report_text.pack(fill='both', expand=True)
        
        # Generate initial report (defer to avoid status bar issue)
        self.root.after(300, self.generate_report)
    
    def create_status_bar(self, parent):
        """Create the status bar."""
        self.status_bar = tk.Frame(parent, bg='#34495e', height=25)
        self.status_bar.pack(fill='x', side='bottom')
        self.status_bar.pack_propagate(False)
        
        self.status_label = tk.Label(
            self.status_bar,
            text="Ready - BMI Calculator Pro",
            bg='#34495e',
            fg='white',
            font=('Arial', 9),
            anchor='w'
        )
        self.status_label.pack(side='left', padx=10, fill='y')
        
        version_label = tk.Label(
            self.status_bar,
            text="v2.0 Pro",
            bg='#34495e',
            fg='#bdc3c7',
            font=('Arial', 9)
        )
        version_label.pack(side='right', padx=10)
    
    def update_status(self, message):
        """Update status bar message."""
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def animate_startup(self):
        """Simple startup animation."""
        self.root.attributes('-alpha', 0.0)
        self._fade_in(0.0)
    
    def _fade_in(self, alpha):
        """Fade in effect."""
        if alpha < 1.0:
            alpha += 0.1
            self.root.attributes('-alpha', alpha)
            self.root.after(50, lambda: self._fade_in(alpha))
        else:
            self.root.attributes('-alpha', 1.0)
    
    # Calculator Functions
    def calculate_bmi(self):
        """Calculate BMI with comprehensive analysis."""
        try:
            # Get input values
            name = self.name_var.get().strip()
            age_str = self.age_var.get().strip()
            gender = self.gender_var.get()
            weight_str = self.weight_var.get().strip()
            height_str = self.height_var.get().strip()
            weight_unit = self.weight_unit_var.get()
            height_unit = self.height_unit_var.get()
            
            # Validation
            if not all([name, age_str, weight_str, height_str]):
                messagebox.showwarning("Missing Information", 
                                     "Please fill in all required fields.")
                return
            
            if gender == 'Select':
                messagebox.showwarning("Missing Information", 
                                     "Please select your gender.")
                return
            
            # Convert inputs
            try:
                age = int(age_str)
                weight = float(weight_str)
                height = float(height_str)
            except ValueError:
                messagebox.showerror("Invalid Input", 
                                   "Please enter valid numbers for age, weight, and height.")
                return
            
            # Validate ranges
            if age < 1 or age > 120:
                messagebox.showerror("Invalid Age", 
                                   "Age must be between 1 and 120 years.")
                return
            
            # Validate measurements
            is_valid, error_msg = self.bmi_engine.validate_input(weight, height, weight_unit, height_unit)
            if not is_valid:
                messagebox.showerror("Invalid Measurements", error_msg)
                return
            
            # Calculate BMI
            bmi = self.bmi_engine.calculate_bmi(weight, height, weight_unit, height_unit)
            analysis = self.bmi_engine.get_bmi_analysis(bmi)
            
            # Save record
            success = self.bmi_engine.save_record(name, age, gender, weight, height, weight_unit, height_unit)
            
            # Display results
            self.display_results(bmi, analysis)
            
            # Show success message
            if success:
                self.update_status(f"BMI calculated and saved: {bmi:.1f} ({analysis['category_name']})")
                messagebox.showinfo("Success", 
                                  f"BMI calculated: {bmi:.1f}\nCategory: {analysis['category_name']}\nRecord saved successfully!")
            else:
                self.update_status(f"BMI calculated: {bmi:.1f} ({analysis['category_name']}) - Save failed")
                messagebox.showwarning("Calculation Complete", 
                                     f"BMI calculated: {bmi:.1f}\nCategory: {analysis['category_name']}\n\nNote: Failed to save record.")
            
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            self.update_status("Error during BMI calculation")
    
    def display_results(self, bmi, analysis):
        """Display BMI results."""
        # Clear previous results
        for widget in self.results_content.winfo_children():
            widget.destroy()
        
        # BMI Value display
        bmi_frame = tk.Frame(self.results_content, bg='white')
        bmi_frame.pack(fill='x', pady=(0, 15))
        
        bmi_card = tk.Frame(bmi_frame, bg=analysis['color'], relief='solid', bd=2)
        bmi_card.pack(fill='x', padx=20)
        
        bmi_inner = tk.Frame(bmi_card, bg=analysis['color'], padx=20, pady=15)
        bmi_inner.pack(fill='x')
        
        # BMI value
        bmi_label = tk.Label(
            bmi_inner,
            text=f"BMI: {bmi:.1f}",
            font=('Arial', 24, 'bold'),
            fg='white',
            bg=analysis['color']
        )
        bmi_label.pack()
        
        # Category
        category_label = tk.Label(
            bmi_inner,
            text=f"{analysis['emoji']} {analysis['category_name']}",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg=analysis['color']
        )
        category_label.pack()
        
        # Risk level
        risk_label = tk.Label(
            bmi_inner,
            text=f"Risk Level: {analysis['risk_level']}",
            font=('Arial', 12),
            fg='white',
            bg=analysis['color']
        )
        risk_label.pack(pady=(5, 0))
        
        # Health advice
        advice_frame = tk.Frame(self.results_content, bg='white')
        advice_frame.pack(fill='both', expand=True, padx=20, pady=(0, 10))
        
        advice_header = tk.Label(
            advice_frame,
            text="💡 Health Advice",
            font=('Arial', 12, 'bold'),
            bg='white',
            anchor='w'
        )
        advice_header.pack(fill='x', pady=(0, 5))
        
        advice_text = tk.Text(
            advice_frame,
            height=4,
            wrap=tk.WORD,
            font=('Arial', 11),
            bg='#f8f9fa',
            fg='#2c3e50',
            relief='flat',
            state='disabled'
        )
        advice_text.pack(fill='both', expand=True)
        
        # Insert advice
        advice_text.configure(state='normal')
        advice_text.insert('1.0', analysis['advice'])
        advice_text.configure(state='disabled')
    
    def clear_form(self):
        """Clear all form fields."""
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("Select")
        self.weight_var.set("")
        self.height_var.set("")
        
        # Clear results
        for widget in self.results_content.winfo_children():
            widget.destroy()
        
        welcome_label = tk.Label(
            self.results_content,
            text="Enter your information and click Calculate BMI\nto get comprehensive health analysis",
            font=('Arial', 12),
            fg='#7f8c8d',
            bg='white',
            justify='center'
        )
        welcome_label.pack(expand=True)
        
        self.update_status("Form cleared")
    
    # Records Management
    def refresh_records(self):
        """Refresh the records display."""
        # Clear existing items
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        
        # Load records
        records = self.bmi_engine.load_records()
        
        # Sort by timestamp (newest first)
        records.sort(key=lambda x: x['timestamp'], reverse=True)
        
        # Insert records
        for record in records:
            date = record['timestamp'][:10]
            name = record.get('name', 'Unknown')
            age = record.get('age', 'N/A')
            gender = record.get('gender', 'N/A')
            weight = f"{record.get('weight_input', record.get('weight_kg', 0)):.1f} {record.get('weight_unit', 'kg')}"
            height = f"{record.get('height_input', record.get('height_m', 0)):.1f} {record.get('height_unit', 'm')}"
            bmi = f"{record['bmi']:.1f}"
            category = record.get('category_name', 'Unknown')
            
            self.records_tree.insert('', 'end', values=(
                date, name, age, gender, weight, height, bmi, category
            ))
        
        self.update_status(f"Loaded {len(records)} records")
    
    def export_csv(self):
        """Export records to CSV file."""
        records = self.bmi_engine.load_records()
        if not records:
            messagebox.showinfo("No Data", "No records available to export.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Export Records"
        )
        
        if filename:
            try:
                csv_data = self.bmi_engine.export_data('csv', records)
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    f.write(csv_data)
                
                messagebox.showinfo("Export Complete", f"Records exported to {filename}")
                self.update_status(f"Exported {len(records)} records to CSV")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export records: {str(e)}")
    
    # Analytics Functions
    def generate_chart(self):
        """Generate selected chart type."""
        chart_type = self.chart_type_var.get()
        
        # Clear previous chart
        self.fig.clear()
        
        # Load records
        records = self.bmi_engine.load_records()
        
        if not records:
            ax = self.fig.add_subplot(111)
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', transform=ax.transAxes,
                   fontsize=14, color='gray')
            ax.set_title('No Data Available')
            self.canvas.draw()
            return
        
        try:
            if chart_type == 'BMI Distribution':
                self.create_bmi_distribution_chart(records)
            elif chart_type == 'Category Analysis':
                self.create_category_analysis_chart(records)
            
            self.fig.tight_layout()
            self.canvas.draw()
            self.update_status(f"Generated {chart_type} chart with {len(records)} records")
            
        except Exception as e:
            messagebox.showerror("Chart Error", f"Failed to generate chart: {str(e)}")
            self.update_status("Chart generation failed")
    
    def create_bmi_distribution_chart(self, records):
        """Create BMI distribution histogram."""
        bmis = [r['bmi'] for r in records]
        
        ax = self.fig.add_subplot(111)
        n, bins, patches = ax.hist(bmis, bins=15, edgecolor='black', alpha=0.7)
        
        # Color bars by BMI category
        for i, (patch, bin_center) in enumerate(zip(patches, (bins[:-1] + bins[1:]) / 2)):
            if bin_center < 18.5:
                patch.set_facecolor('#3498db')
            elif bin_center < 25:
                patch.set_facecolor('#2ecc71')
            elif bin_center < 30:
                patch.set_facecolor('#f39c12')
            else:
                patch.set_facecolor('#e74c3c')
        
        ax.set_xlabel('BMI Value', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title('BMI Distribution', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Add statistics
        mean_bmi = np.mean(bmis)
        ax.axvline(mean_bmi, color='red', linestyle='--', alpha=0.8, 
                  label=f'Mean: {mean_bmi:.1f}')
        ax.legend()
    
    def create_category_analysis_chart(self, records):
        """Create BMI category distribution pie chart."""
        categories = {}
        for record in records:
            cat = record.get('category_name', 'Unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        if not categories:
            return
        
        ax = self.fig.add_subplot(111)
        
        colors = ['#3498db', '#2ecc71', '#f39c12', '#e67e22', '#e74c3c', '#c0392b']
        
        wedges, texts, autotexts = ax.pie(
            categories.values(), 
            labels=categories.keys(), 
            colors=colors[:len(categories)],
            autopct='%1.1f%%',
            startangle=90
        )
        
        ax.set_title('BMI Category Distribution', fontsize=14, fontweight='bold')
    
    # Reports Functions
    def generate_report(self):
        """Generate comprehensive report."""
        try:
            report_content = self.bmi_engine.generate_report()
            
            # Display report
            self.report_text.configure(state='normal')
            self.report_text.delete('1.0', tk.END)
            self.report_text.insert('1.0', report_content)
            self.report_text.configure(state='disabled')
            
            self.update_status("Generated comprehensive report")
            
        except Exception as e:
            messagebox.showerror("Report Error", f"Failed to generate report: {str(e)}")
    
    def save_report(self):
        """Save the current report."""
        content = self.report_text.get('1.0', tk.END).strip()
        if not content:
            messagebox.showwarning("No Report", "Please generate a report first.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Report"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Success", f"Report saved as {filename}")
                self.update_status(f"Report saved to {filename}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save report: {str(e)}")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = BMICalculatorProGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication closed by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()