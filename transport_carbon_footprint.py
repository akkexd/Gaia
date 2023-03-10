import tkinter as tk
from tkinter import messagebox
import re
import requests
def TransportCarbonFootprintCalculator(root):
    # Hide the main window
    root.withdraw()

    # Create a new Toplevel window
    window = tk.Toplevel(root)
    window.title("Transport Carbon Footprint Calculator")

    # Set background image
    background_image = tk.PhotoImage(file="background.jpg")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create label and input for distance
    distance_label = tk.Label(window, text="Distance (km):", bg="SystemButtonFace")
    distance_label.grid(row=0, column=0, padx=10, pady=10)
    distance_entry = tk.Entry(window)
    distance_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create label and input for fuel efficiency
    efficiency_label = tk.Label(window, text="Fuel Efficiency (l/100km):", bg="SystemButtonFace")
    efficiency_label.grid(row=1, column=0, padx=10, pady=10)
    efficiency_entry = tk.Entry(window)
    efficiency_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create label and input for fuel type
    fuel_label = tk.Label(window, text="Fuel Type:", bg="SystemButtonFace")
    fuel_label.grid(row=2, column=0, padx=10, pady=10)
    fuel_var = tk.StringVar()
    fuel_dropdown = tk.OptionMenu(window, fuel_var, "Gasoline", "Diesel", "Electricity")
    fuel_dropdown.grid(row=2, column=1, padx=10, pady=10)

    # Create function to calculate carbon emission and save user data
    def calculate_emission():
        # Get inputs from user
        distance = distance_entry.get()
        efficiency = efficiency_entry.get()
        fuel_type = fuel_var.get()

        # Validate input for distance
        if not re.match(r"^\d+(\.\d+)?$", distance):
            messagebox.showerror("Error", "Distance must be a number")
            return

        # Validate input for fuel efficiency
        if not re.match(r"^\d+(\.\d+)?$", efficiency):
            messagebox.showerror("Error", "Fuel efficiency must be a number")
            return

        # Calculate carbon emission based on fuel type
        if fuel_type == "Gasoline":
            emission = 2.31 * float(distance) * float(efficiency) / 100
        elif fuel_type == "Diesel":
            emission = 2.68 * float(distance) * float(efficiency) / 100
        else:
            emission = 0

        # Save user data to file
        with open('user_data.txt', 'a') as f:
            f.write(fuel_type + 'Fuel type:' + distance + ', Distance:' + efficiency + ', Efficiency:' + str(emission) + '\n')

        # Show result in another GUI window
        result_window = tk.Toplevel(window)
        result_window.title("Result")
        result_label = tk.Label(result_window, text=f"Carbon Emission: {emission:.2f} kg")
        result_label.pack(padx=10, pady=10)

    # Create calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate_emission)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create home button and function
    def go_home():
        # Destroy the current window
        window.destroy()

        # Show the main window
        root.deiconify()

    home_button = tk.Button(window, text="Home", command=go_home)
    home_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    # Run Tkinter main loop
    window.mainloop()
