import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and add widgets to the window
frame = ttk.Frame(window, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

weight_label = ttk.Label(frame, text="Weight (kg):")
weight_label.grid(column=0, row=0, sticky=tk.W)

weight_entry = ttk.Entry(frame)
weight_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

height_label = ttk.Label(frame, text="Height (m):")
height_label.grid(column=0, row=1, sticky=tk.W)

height_entry = ttk.Entry(frame)
height_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(column=0, row=2, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2)

# Run the Tkinter event loop
window.mainloop()