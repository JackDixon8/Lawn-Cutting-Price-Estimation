import tkinter as tk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def estimate_cost():
    shape = shape_var.get()
    length = float(length_entry.get())
    width = float(width_entry.get())
    home_address = home_address_entry.get()
    lawn_address = lawn_address_entry.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    home_location = geolocator.geocode(home_address)
    lawn_location = geolocator.geocode(lawn_address)
    distance = geodesic((home_location.latitude, home_location.longitude), (lawn_location.latitude, lawn_location.longitude)).km

    if shape.lower() == "rectangle":
        area = length * width
        cost = area * 0.1 # Assume cost is $0.1 per square foot
        cost += distance * 0.5 # Assume a cost of $0.5 per km for distance
    elif shape.lower() == "circle":
        radius = min(length, width) / 2
        area = 3.14 * (radius ** 2)
        cost = area * 0.1 # Assume cost is $0.1 per square foot
        cost += distance * 0.5 # Assume a cost of $0.5 per km for distance
    else:
        cost = "Invalid shape"

    cost_label.config(text="Estimated cost: $" + str(cost))

root = tk.Tk()
root.title("Lawn Cost Estimator")

shape_var = tk.StringVar(value="rectangle")
rectangle_radio = tk.Radiobutton(root, text="Rectangle", variable=shape_var, value="rectangle")
circle_radio = tk.Radiobutton(root, text="Circle", variable=shape_var, value="circle")
rectangle_radio.grid(row=0, column=0, sticky="w")
circle_radio.grid(row=0, column=1, sticky="w")

length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0, sticky="w")
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1)

width_label = tk.Label(root, text="Width:")
width_label.grid(row=2, column=0, sticky="w")
width_entry = tk.Entry(root)
width_entry.grid(row=2, column=1)

home_address_label = tk.Label(root, text="Home Address:")
home_address_label.grid(row=3, column=0, sticky="w")
home_address_entry = tk.Entry(root)
home_address_entry.grid(row=3, column=1)

lawn_address_label = tk.Label(root, text="Lawn Address:")
lawn_address_label.grid(row=4, column=0, sticky="w")
lawn_address_entry = tk.Entry(root)
lawn_address_entry.grid(row=4, column=1)

estimate_button = tk.Button(root, text="Estimate Cost", command=estimate_cost)
estimate_button.grid(row=5, column=0, columnspan=2, pady=10)

cost_label = tk.Label(root, text="")
cost_label.grid(row=6, column=0, columnspan=2)

root.mainloop()