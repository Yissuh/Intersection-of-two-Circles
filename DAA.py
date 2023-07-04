import math
import tkinter as tk
from tkinter import messagebox

# Function to calculate the intersection points of two circles
def circle_intersection(x1, y1, x2, y2, r1, r2):
    # Calculate the distance between the centers of the circles
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Check if the circles are separate
    if d > r1 + r2:
        result = "Separate"
        return result

    # Check if one circle is completely inside the other
    if d < abs(r1 - r2):
        result = "Inside"
        return result

    # Check if the circles are coincident
    if d == 0 and r1 == r2:
        result = "Coincident"
        return result

    # Calculate the intersection points
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d

    x4 = x3 + h * (y2 - y1) / d
    y4 = y3 - h * (x2 - x1) / d

    x5 = x3 - h * (y2 - y1) / d
    y5 = y3 + h * (x2 - x1) / d

    return (x4, y4), (x5, y5)

# Function to clear the background color of entry fields
def clear_entry_background():
    entry_x1.config(bg="white")
    entry_y1.config(bg="white")
    entry_r1.config(bg="white")
    entry_x2.config(bg="white")
    entry_y2.config(bg="white")
    entry_r2.config(bg="white")

# Function to handle button click event
# Function to handle button click event
def calculate_intersection():
    clear_entry_background()

    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())

        # Check if radius values are negative
        if r1 < 0 and r2 < 0:
            entry_r1.config(bg="red")
            entry_r2.config(bg="red")
            raise ValueError("Invalid radius value for the two circles")

        if r1 < 0:
            entry_r1.config(bg="red")
            raise ValueError("Invalid radius value for the first circle")

        if r2 < 0:
            entry_r2.config(bg="red")
            raise ValueError("Invalid radius value for the second circle")

        # Check if input values are integers
        if not all(isinstance(val, int) for val in [x1, y1, x2, y2, r1, r2]):
            raise ValueError("Invalid input. Please enter integer values.")

        result = circle_intersection(x1, y1, x2, y2, r1, r2)

        if result == "Separate":
            messagebox.showinfo("Result", "No intersection points. The circles are separate.")
        elif result == "Inside":
            messagebox.showinfo("Result", "No intersection points. One of the circles is inside the other.")
        elif result == "Coincident":
            messagebox.showinfo("Result", "No intersection points. The circles overlap each other.")
        else:
            messagebox.showinfo("Result", f"Intersection points: {result}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Create the Tkinter GUI window
window = tk.Tk()
window.title("Circle Intersection Calculator")

# Create labels and entry fields for circle A
label_cir1 = tk.Label(window, text="First Circle:")
label_cir1.grid(row=0, column=0, padx=5, pady=5)

label_x1 = tk.Label(window, text="x:")
label_x1.grid(row=1, column=0, padx=5, pady=5)
entry_x1 = tk.Entry(window)
entry_x1.grid(row=1, column=1, padx=5, pady=5)

label_y1 = tk.Label(window, text="y:")
label_y1.grid(row=2, column=0, padx=5, pady=5)
entry_y1 = tk.Entry(window)
entry_y1.grid(row=2, column=1, padx=5, pady=5)

label_r1 = tk.Label(window, text="Radius:")
label_r1.grid(row=3, column=0, padx=5, pady=5)
entry_r1 = tk.Entry(window)
entry_r1.grid(row=3, column=1, padx=5, pady=5)

# Create labels and entry fields for circle B
label_cir2 = tk.Label(window, text="Second Circle:")
label_cir2.grid(row=4, column=0, padx=5, pady=5)

label_x2 = tk.Label(window, text="x:")
label_x2.grid(row=5, column=0, padx=5, pady=5)
entry_x2 = tk.Entry(window)
entry_x2.grid(row=5, column=1, padx=5, pady=5)

label_y2 = tk.Label(window, text="y:")
label_y2.grid(row=6, column=0, padx=5, pady=5)
entry_y2 = tk.Entry(window)
entry_y2.grid(row=6, column=1, padx=5, pady=5)

label_r2 = tk.Label(window, text="Radius:")
label_r2.grid(row=7, column=0, padx=5, pady=5)
entry_r2 = tk.Entry(window)
entry_r2.grid(row=7, column=1, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_intersection)
calculate_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

# Start the Tkinter event loop
window.mainloop()
