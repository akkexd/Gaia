import tkinter as tk
from tkinter import messagebox
import re

class ElectricityFootprintCalculator:
    def __init__(self, master):
        self.master = master
        self.master.withdraw()

        # Create a new window for the electricity footprint calculator
        self.top_level = tk.Toplevel(self.master)
        self.top_level.title("Electricity Carbon Footprint Calculator")

        # Load the background image
        bg_image = tk.PhotoImage(file="background.jpg")

        # Create a label for the background image and place it behind other widgets
        bg_label = tk.Label(self.top_level, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a label for the instruction
        instruction_label = tk.Label(self.top_level, text="Please enter the amount of electricity used (kWh):", bg='SystemButtonFace')
        instruction_label.pack(padx=10, pady=10)

        # Create an entry widget for the user to input the amount of electricity used
        self.electricity_entry = tk.Entry(self.top_level)
        self.electricity_entry.pack(padx=10, pady=10)

        # Create a button to calculate the carbon footprint
        calculate_button = tk.Button(self.top_level, text="Calculate", command=self.calculate_footprint)
        calculate_button.pack(padx=10, pady=10)

        # Create a button to return to the home screen
        home_button = tk.Button(self.top_level, text="Home", command=self.go_home)
        home_button.pack(padx=10, pady=10)

    def calculate_footprint(self):
        # Get the amount of electricity used from the entry widget
        electricity_used = self.electricity_entry.get()

        # Validate that the input is a number
        if not re.match(r"^\d+(\.\d+)?$", electricity_used):
            messagebox.showerror("Error", "Please enter a valid number for electricity used.")
            return

        # Calculate the carbon footprint of the electricity usage
        carbon_footprint = float(electricity_used) * 0.4

        # Show the result in a message box
        messagebox.showinfo("Carbon Footprint", f"The carbon footprint of {electricity_used} kWh of electricity is {carbon_footprint} kg CO2e.")


    def go_home(self):
        # Destroy the current window
        self.top_level.destroy()

        # Show the main window
        self.master.deiconify()
