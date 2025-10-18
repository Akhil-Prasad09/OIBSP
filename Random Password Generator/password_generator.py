import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
import threading
import time

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Advanced Password Generator - Oasis Infobyte Project")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Variables
        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=False)
        self.exclude_similar_var = tk.BooleanVar(value=False)
        
        self.password_history = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 Advanced Password Generator",
            font=("Helvetica", 20, "bold"),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Oasis Infobyte Internship Project",
            font=("Helvetica", 12),
            bg='#2c3e50',
            fg='#bdc3c7'
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Password length section
        length_frame = tk.LabelFrame(
            main_frame,
            text="Password Length",
            font=("Helvetica", 12, "bold"),
            bg='#34495e',
            fg='#ecf0f1',
            relief='groove',
            bd=2
        )
        length_frame.pack(fill='x', padx=15, pady=10)
        
        length_scale = tk.Scale(
            length_frame,
            from_=4,
            to=50,
            orient='horizontal',
            variable=self.length_var,
            font=("Helvetica", 10),
            bg='#34495e',
            fg='#ecf0f1',
            highlightthickness=0,
            troughcolor='#2c3e50',
            activebackground='#3498db'
        )
        length_scale.pack(fill='x', padx=10, pady=10)
        
        # Character options section
        options_frame = tk.LabelFrame(
            main_frame,
            text="Character Options",
            font=("Helvetica", 12, "bold"),
            bg='#34495e',
            fg='#ecf0f1',
            relief='groove',
            bd=2
        )
        options_frame.pack(fill='x', padx=15, pady=10)
        
        # Checkboxes with better styling
        checkbox_options = [
            ("Include Uppercase Letters (A-Z)", self.uppercase_var),
            ("Include Lowercase Letters (a-z)", self.lowercase_var),
            ("Include Numbers (0-9)", self.numbers_var),
            ("Include Symbols (!@#$%^&*)", self.symbols_var),
            ("Exclude Similar Characters (0,O,1,l,I)", self.exclude_similar_var)
        ]
        
        for text, var in checkbox_options:
            cb = tk.Checkbutton(
                options_frame,
                text=text,
                variable=var,
                font=("Helvetica", 10),
                bg='#34495e',
                fg='#ecf0f1',
                selectcolor='#2c3e50',
                activebackground='#34495e',
                activeforeground='#ecf0f1',
                relief='flat'
            )
            cb.pack(anchor='w', padx=15, pady=5)
        
        # Generate button
        generate_frame = tk.Frame(main_frame, bg='#34495e')
        generate_frame.pack(pady=20)
        
        self.generate_btn = tk.Button(
            generate_frame,
            text="🚀 GENERATE PASSWORD",
            command=self.generate_password,
            font=("Helvetica", 14, "bold"),
            bg='#e74c3c',
            fg='white',
            relief='raised',
            bd=3,
            padx=30,
            pady=10,
            cursor='hand2',
            activebackground='#c0392b'
        )
        self.generate_btn.pack()
        
        # Output section
        output_frame = tk.LabelFrame(
            main_frame,
            text="Generated Password",
            font=("Helvetica", 12, "bold"),
            bg='#34495e',
            fg='#ecf0f1',
            relief='groove',
            bd=2
        )
        output_frame.pack(fill='x', padx=15, pady=10)
        
        # Password display
        self.password_text = tk.Text(
            output_frame,
            height=3,
            font=("Courier", 12, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='sunken',
            bd=2,
            wrap='word',
            selectbackground='#3498db'
        )
        self.password_text.pack(fill='x', padx=10, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(output_frame, bg='#34495e')
        button_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        # Copy button
        self.copy_btn = tk.Button(
            button_frame,
            text="📋 Copy to Clipboard",
            command=self.copy_password,
            font=("Helvetica", 11, "bold"),
            bg='#27ae60',
            fg='white',
            relief='raised',
            bd=2,
            padx=15,
            pady=5,
            cursor='hand2',
            activebackground='#229954'
        )
        self.copy_btn.pack(side='left', padx=(0, 10))
        
        # Clear button
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_password,
            font=("Helvetica", 11, "bold"),
            bg='#f39c12',
            fg='white',
            relief='raised',
            bd=2,
            padx=15,
            pady=5,
            cursor='hand2',
            activebackground='#e67e22'
        )
        self.clear_btn.pack(side='left')
        
        # Password strength section
        strength_frame = tk.LabelFrame(
            main_frame,
            text="Password Strength",
            font=("Helvetica", 12, "bold"),
            bg='#34495e',
            fg='#ecf0f1',
            relief='groove',
            bd=2
        )
        strength_frame.pack(fill='x', padx=15, pady=10)
        
        self.strength_label = tk.Label(
            strength_frame,
            text="Generate a password to see strength analysis",
            font=("Helvetica", 10),
            bg='#34495e',
            fg='#bdc3c7'
        )
        self.strength_label.pack(padx=10, pady=5)
        
        self.progress_var = tk.DoubleVar()
        self.strength_progress = ttk.Progressbar(
            strength_frame,
            variable=self.progress_var,
            maximum=100,
            length=400
        )
        self.strength_progress.pack(padx=10, pady=(0, 10))
        
        # Quick presets
        preset_frame = tk.LabelFrame(
            main_frame,
            text="Quick Presets",
            font=("Helvetica", 12, "bold"),
            bg='#34495e',
            fg='#ecf0f1',
            relief='groove',
            bd=2
        )
        preset_frame.pack(fill='x', padx=15, pady=10)
        
        preset_buttons_frame = tk.Frame(preset_frame, bg='#34495e')
        preset_buttons_frame.pack(pady=10)
        
        presets = [
            ("Weak", 8, True, True, False, False),
            ("Medium", 12, True, True, True, False),
            ("Strong", 16, True, True, True, True),
            ("Ultra", 24, True, True, True, True)
        ]
        
        for name, length, upper, lower, nums, syms in presets:
            btn = tk.Button(
                preset_buttons_frame,
                text=name,
                command=lambda l=length, u=upper, lo=lower, n=nums, s=syms: self.apply_preset(l, u, lo, n, s),
                font=("Helvetica", 10, "bold"),
                bg='#9b59b6',
                fg='white',
                relief='raised',
                bd=2,
                padx=10,
                pady=5,
                cursor='hand2',
                activebackground='#8e44ad'
            )
            btn.pack(side='left', padx=5)
    
    def apply_preset(self, length, upper, lower, nums, syms):
        self.length_var.set(length)
        self.uppercase_var.set(upper)
        self.lowercase_var.set(lower)
        self.numbers_var.set(nums)
        self.symbols_var.set(syms)
        self.generate_password()
    
    def generate_password(self):
        # Validate selections
        if not any([self.uppercase_var.get(), self.lowercase_var.get(), 
                   self.numbers_var.get(), self.symbols_var.get()]):
            messagebox.showwarning("Warning", "Please select at least one character type!")
            return
        
        # Build character set
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Exclude similar characters if selected
        if self.exclude_similar_var.get():
            similar = "0O1lI"
            characters = ''.join(c for c in characters if c not in similar)
        
        # Generate password
        length = self.length_var.get()
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display password
        self.password_text.delete('1.0', tk.END)
        self.password_text.insert('1.0', password)
        
        # Add to history
        if password not in self.password_history:
            self.password_history.append(password)
            if len(self.password_history) > 10:  # Keep only last 10
                self.password_history.pop(0)
        
        # Calculate and display strength
        self.calculate_strength(password)
        
        # Animate progress bar
        self.animate_progress()
    
    def calculate_strength(self, password):
        score = 0
        feedback = []
        
        # Length scoring
        if len(password) >= 8:
            score += 25
        if len(password) >= 12:
            score += 25
        if len(password) >= 16:
            score += 25
        else:
            feedback.append("Consider using 16+ characters")
        
        # Character variety
        if any(c.isupper() for c in password):
            score += 10
        else:
            feedback.append("Add uppercase letters")
            
        if any(c.islower() for c in password):
            score += 10
        else:
            feedback.append("Add lowercase letters")
            
        if any(c.isdigit() for c in password):
            score += 10
        else:
            feedback.append("Add numbers")
            
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 15
        else:
            feedback.append("Add special characters")
        
        # Determine strength level
        if score >= 85:
            level = "Very Strong"
            color = "#27ae60"
        elif score >= 70:
            level = "Strong"
            color = "#f39c12"
        elif score >= 50:
            level = "Medium"
            color = "#e67e22"
        else:
            level = "Weak"
            color = "#e74c3c"
        
        self.progress_var.set(score)
        
        feedback_text = f"Strength: {level} ({score}%)"
        if feedback:
            feedback_text += f" - Tips: {', '.join(feedback[:2])}"
        
        self.strength_label.config(text=feedback_text, fg=color)
    
    def animate_progress(self):
        """Animate the progress bar filling up"""
        target = self.progress_var.get()
        current = 0
        step = target / 20
        
        def update_progress():
            nonlocal current
            if current < target:
                current += step
                self.progress_var.set(min(current, target))
                self.root.after(50, update_progress)
        
        self.progress_var.set(0)
        self.root.after(100, update_progress)
    
    def copy_password(self):
        password = self.password_text.get('1.0', tk.END).strip()
        if password:
            try:
                pyperclip.copy(password)
                # Show feedback
                original_text = self.copy_btn.config('text')[-1]
                self.copy_btn.config(text="✅ Copied!", bg='#2ecc71')
                self.root.after(1500, lambda: self.copy_btn.config(text=original_text, bg='#27ae60'))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def clear_password(self):
        self.password_text.delete('1.0', tk.END)
        self.strength_label.config(text="Generate a password to see strength analysis", fg='#bdc3c7')
        self.progress_var.set(0)

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()