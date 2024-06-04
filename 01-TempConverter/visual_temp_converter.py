import tkinter as tk
from tkinter import ttk

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()
        
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                converted_temp = (temp * 9/5) + 32
            elif to_unit == 'Kelvin':
                converted_temp = temp + 273.15
            else:
                converted_temp = temp
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                converted_temp = (temp - 32) * 5/9
            elif to_unit == 'Kelvin':
                converted_temp = (temp - 32) * 5/9 + 273.15
            else:
                converted_temp = temp
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                converted_temp = temp - 273.15
            elif to_unit == 'Fahrenheit':
                converted_temp = (temp - 273.15) * 9/5 + 32
            else:
                converted_temp = temp

        result_label.config(text=f"Converted Temperature: {converted_temp:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Please enter a valid temperature")

# Set up the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Input field
entry_label = ttk.Label(root, text="Enter Temperature:")
entry_label.grid(column=0, row=0, padx=10, pady=10)
entry = ttk.Entry(root)
entry.grid(column=1, row=0, padx=10, pady=10)

# Dropdown for 'from' unit
from_var = tk.StringVar()
from_label = ttk.Label(root, text="From:")
from_label.grid(column=0, row=1, padx=10, pady=10)
from_dropdown = ttk.Combobox(root, textvariable=from_var)
from_dropdown['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
from_dropdown.grid(column=1, row=1, padx=10, pady=10)
from_dropdown.current(0)

# Dropdown for 'to' unit
to_var = tk.StringVar()
to_label = ttk.Label(root, text="To:")
to_label.grid(column=0, row=2, padx=10, pady=10)
to_dropdown = ttk.Combobox(root, textvariable=to_var)
to_dropdown['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
to_dropdown.grid(column=1, row=2, padx=10, pady=10)
to_dropdown.current(1)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Result label
result_label = ttk.Label(root, text="Converted Temperature:")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
