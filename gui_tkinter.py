#!/usr/bin/env python3
"""
Simple GUI version using tkinter for non-technical users
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import json
import csv
from pathlib import Path
from generators import generate_mixed_aliases

class EmailAliasGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Alias Generator v0.1.0")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🌟 Email Alias Generator", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Email input
        ttk.Label(main_frame, text="📧 Your Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar()
        email_entry = ttk.Entry(main_frame, textvariable=self.email_var, width=40)
        email_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Count input
        ttk.Label(main_frame, text="🔢 Number of Aliases:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.count_var = tk.StringVar(value="5")
        count_entry = ttk.Entry(main_frame, textvariable=self.count_var, width=10)
        count_entry.grid(row=2, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Generate button
        generate_btn = ttk.Button(main_frame, text="✨ Generate Aliases", 
                                command=self.generate_aliases, style='Accent.TButton')
        generate_btn.grid(row=3, column=0, columnspan=2, pady=20, sticky=tk.W)
        
        # Results area
        ttk.Label(main_frame, text="📋 Generated Aliases:", font=('Arial', 10, 'bold')).grid(
            row=4, column=0, columnspan=3, sticky=tk.W, pady=(0, 5))
        
        self.results_text = scrolledtext.ScrolledText(main_frame, width=60, height=15, 
                                                     wrap=tk.WORD, font=('Consolas', 10))
        self.results_text.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), 
                              pady=(0, 10))
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Save buttons
        ttk.Button(buttons_frame, text="💾 Save as Text", 
                  command=lambda: self.save_aliases('text')).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="📄 Save as JSON", 
                  command=lambda: self.save_aliases('json')).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="📊 Save as CSV", 
                  command=lambda: self.save_aliases('csv')).pack(side=tk.LEFT, padx=(0, 10))
        
        # Copy button
        ttk.Button(buttons_frame, text="📋 Copy All", 
                  command=self.copy_aliases).pack(side=tk.RIGHT)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to generate aliases!")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.aliases = []
    
    def generate_aliases(self):
        email = self.email_var.get().strip().lower()
        
        # Validate email
        if not email or '@' not in email or '.' not in email.split('@')[1]:
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        # Validate count
        try:
            count = int(self.count_var.get())
            if count <= 0 or count > 100:
                messagebox.showerror("Error", "Please enter a number between 1 and 100")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        # Generate aliases
        try:
            self.status_var.set("⏳ Generating aliases...")
            self.root.update()
            
            self.aliases = generate_mixed_aliases(email, count)
            
            # Display results
            self.results_text.delete(1.0, tk.END)
            
            # Add header info
            domain = email.split('@')[1]
            is_gmail = domain in ['gmail.com', 'googlemail.com']
            
            header = f"Generated {len(self.aliases)} aliases for: {email}\n"
            if is_gmail:
                header += "✨ Gmail detected - all aliases will forward to your inbox!\n"
            else:
                header += f"📌 {domain} - using plus addressing (check provider support)\n"
            header += "\n" + "="*50 + "\n\n"
            
            self.results_text.insert(tk.END, header)
            
            # Add aliases
            for i, alias in enumerate(self.aliases, 1):
                # Determine alias type
                if '+' in alias:
                    alias_type = " (plus address)"
                elif is_gmail and alias.split('@')[0].replace('.', '') == email.split('@')[0].replace('.', ''):
                    alias_type = " (Gmail dot variation)"
                else:
                    alias_type = " (variation)"
                
                self.results_text.insert(tk.END, f"{i:2}. {alias}{alias_type}\n")
            
            self.status_var.set(f"✅ Generated {len(self.aliases)} aliases successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate aliases: {str(e)}")
            self.status_var.set("❌ Generation failed")
    
    def copy_aliases(self):
        if not self.aliases:
            messagebox.showwarning("Warning", "No aliases to copy. Generate some first!")
            return
        
        alias_text = '\n'.join(self.aliases)
        self.root.clipboard_clear()
        self.root.clipboard_append(alias_text)
        self.status_var.set("📋 Copied to clipboard!")
    
    def save_aliases(self, format_type):
        if not self.aliases:
            messagebox.showwarning("Warning", "No aliases to save. Generate some first!")
            return
        
        # File dialog
        extensions = {
            'text': '.txt',
            'json': '.json',
            'csv': '.csv'
        }
        
        filename = filedialog.asksaveasfilename(
            defaultextension=extensions[format_type],
            filetypes=[(f"{format_type.upper()} files", f"*{extensions[format_type]}")])
        
        if not filename:
            return
        
        try:
            if format_type == 'json':
                with open(filename, 'w') as f:
                    json.dump(self.aliases, f, indent=2)
            elif format_type == 'csv':
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['email'])
                    for alias in self.aliases:
                        writer.writerow([alias])
            else:  # text
                with open(filename, 'w') as f:
                    for alias in self.aliases:
                        f.write(f"{alias}\n")
            
            self.status_var.set(f"💾 Saved to {Path(filename).name}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def main():
    root = tk.Tk()
    app = EmailAliasGeneratorGUI(root)
    
    # Center window
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == '__main__':
    main()
