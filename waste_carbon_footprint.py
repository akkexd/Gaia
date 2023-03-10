import tkinter as tk
from tkinter import messagebox
import re

def WasteEmissionCalculator(root):
    # Destroy the main window
    root.withdraw()

    # Create a new Toplevel window
    window = tk.Toplevel(root)
    window.title("Waste Carbon Footprint Calculator")

    # Set background image
    background_image = tk.PhotoImage(file="background.jpg")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    class WasteEmissionCalculator:
        def __init__(self, root):
            self.root = root
            self.create_widgets()

        def create_widgets(self):
            # Create a label for the instruction
            instruction_label = tk.Label(self.root, text="Please enter the weight of waste produced (in kg):")
            instruction_label.pack(padx=10, pady=10)

            # Create an entry for the weight of waste produced
            self.weight_entry = tk.Entry(self.root)
            self.weight_entry.pack(padx=10, pady=10)

            # Create a button to calculate the carbon footprint
            calculate_button = tk.Button(self.root, text="Calculate Carbon Footprint", command=self.calculate_carbon_footprint)
            calculate_button.pack(padx=10, pady=10)

        def calculate_carbon_footprint(self):
            # Get the weight of waste produced from the entry
            weight = self.weight_entry.get()

            # Check if the weight is a valid number
            if not re.match("^[0-9]*\.?[0-9]+$", weight):
                messagebox.showerror("Error", "Please enter a valid weight")
                return

            # Calculate the carbon footprint
            carbon_footprint = float(weight) * 0.2

            # Show result in another GUI window
            result_window = tk.Toplevel(window)
            result_window.title("Result")
            result_label = tk.Label(result_window, text=f"The carbon footprint of {weight} kg of waste produced is {carbon_footprint:.2f} kgCO2e")
            result_label.pack(padx=10, pady=10)

    # Create an instance of the WasteEmissionCalculator class
    calculator = WasteEmissionCalculator(window)

    # Create home button and function
    def go_home():
        # Destroy the current window
        window.destroy()

        # Show the main window
        root.deiconify()

    home_button = tk.Button(window, text="Home", command=go_home)
    home_button.pack(padx=10, pady=10)

    # Run Tkinter main loop
    window.mainloop()
