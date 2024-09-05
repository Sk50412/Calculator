import tkinter as tk
from math import sqrt

# Function to evaluate expressions
def evaluate_expression(event=None):
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle percentage
def calculate_percentage():
    try:
        current_value = float(entry.get())
        result = current_value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle square
def calculate_square():
    try:
        current_value = float(entry.get())
        result = current_value ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle square root
def calculate_sqrt():
    try:
        current_value = float(entry.get())
        result = sqrt(current_value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear_field():
    entry.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#2c3e50")
root.geometry("400x500")

# Styling options
button_config = {
    "font": ("Helvetica", 18),
    "bg": "#34495e",
    "fg": "#ecf0f1",
    "activebackground": "#2980b9",
    "activeforeground": "#ecf0f1",
    "relief": "flat",
    "borderwidth": 0,
    "highlightthickness": 0,
    "highlightbackground": "#2c3e50",
    "padx": 10,
    "pady": 10,
}

# Entry widget for the input and result
entry = tk.Entry(root, font=("Helvetica", 24), borderwidth=2, relief="flat", bg="#34495e", fg="#ecf0f1", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Button creation with layout configuration
buttons = [
    ('%', 1, 0, calculate_percentage),
    ('√', 1, 1, calculate_sqrt),
    ('x²', 1, 2, calculate_square),
    ('C', 1, 3, clear_field),
    ('7', 2, 0, lambda: entry.insert(tk.END, '7')),
    ('8', 2, 1, lambda: entry.insert(tk.END, '8')),
    ('9', 2, 2, lambda: entry.insert(tk.END, '9')),
    ('/', 2, 3, lambda: entry.insert(tk.END, '/')),
    ('4', 3, 0, lambda: entry.insert(tk.END, '4')),
    ('5', 3, 1, lambda: entry.insert(tk.END, '5')),
    ('6', 3, 2, lambda: entry.insert(tk.END, '6')),
    ('*', 3, 3, lambda: entry.insert(tk.END, '*')),
    ('1', 4, 0, lambda: entry.insert(tk.END, '1')),
    ('2', 4, 1, lambda: entry.insert(tk.END, '2')),
    ('3', 4, 2, lambda: entry.insert(tk.END, '3')),
    ('-', 4, 3, lambda: entry.insert(tk.END, '-')),
    ('0', 5, 0, lambda: entry.insert(tk.END, '0')),
    ('.', 5, 1, lambda: entry.insert(tk.END, '.')),
    ('+', 5, 2, lambda: entry.insert(tk.END, '+')),
    ('=', 5, 3, evaluate_expression),
]

# Grid layout configuration for responsiveness
for (text, row, col, command) in buttons:
    btn = tk.Button(root, text=text, command=command, **button_config)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure weight for responsive resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

# Bind the Enter key to evaluate the expression
root.bind('<Return>', evaluate_expression)

# Start the main loop
root.mainloop()
