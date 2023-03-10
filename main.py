import tkinter as tk
import webbrowser
from tkinter import messagebox
from transport_carbon_footprint import TransportCarbonFootprintCalculator
from waste_carbon_footprint import WasteEmissionCalculator
from electricity_footprint import ElectricityFootprintCalculator
import subprocess


def display_health_benefits():
    messagebox.showinfo("Health Benefits", "Reducing your carbon footprint has many health benefits, including lower risk of heart disease and respiratory illnesses. By reducing your carbon footprint, you can help improve air and water quality, reduce pollution, and support a healthier environment for all.")


def exit_program():
    root.destroy()

def open_eco_teaching():
    EcoTeaching(root)


def open_vision():
    root.withdraw()  # hide the main window
    subprocess.Popen(['python', 'vision.py'])

# Create the main window
root = tk.Tk()
root.title("Carbon Footprint Calculator")

# Load the background image
bg_image = tk.PhotoImage(file="background.jpg")

# Create a label for the background image and place it behind other widgets
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the instruction
instruction_label = tk.Label(root, text="Please choose the type of carbon footprint to calculate:", bg='white')
instruction_label.pack(padx=10, pady=10)

# Create a button to calculate transport carbon footprint
transport_button = tk.Button(root, text="Transport Carbon Footprint", command=lambda: TransportCarbonFootprintCalculator(root))
transport_button.pack(padx=10, pady=10)

# Create a button to calculate waste carbon footprint
waste_button = tk.Button(root, text="Waste Carbon Footprint", command=lambda: WasteEmissionCalculator(root))
waste_button.pack(padx=10, pady=10)

# Create a button to calculate electricity carbon footprint
electricity_button = tk.Button(root, text="Electricity Carbon Footprint", command=lambda: ElectricityFootprintCalculator(root))
electricity_button.pack(padx=10, pady=10)

# Create a button to learn about health benefits
health_button = tk.Button(root, text="Learn about Health Benefits", command=display_health_benefits)
health_button.pack(padx=10, pady=10)

# Create a button to open vision.py
vision_button = tk.Button(root, text="Vision", command=open_vision)
vision_button.pack(padx=10, pady=10)

# Create a button to open the About Us page
about_button = tk.Button(root, text="About Us", command=lambda: webbrowser.open("file:///C:/Users/User/PycharmProjects/pythonProject/index.html"))
about_button.pack(padx=10, pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(padx=10, pady=10)


# Run the main event loop
root.mainloop()
