import math
import tkinter as tk
from tkinter import messagebox


def circle_center_distance(x2, x1, y2, y1):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


def clear_entry_background():
    entry_x1.config(bg="white")
    entry_y1.config(bg="white")
    entry_r1.config(bg="white")
    entry_x2.config(bg="white")
    entry_y2.config(bg="white")
    entry_r2.config(bg="white")


def handle_button_click():
    clear_entry_background()
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())

        validate_radius_values(r1, r2)

        d = circle_center_distance(x2, x1, y2, y1)

        canvas.delete("all")
        scale = calculate_scale(canvas_width, canvas_height, x1, y1, r1, x2, y2, r2)
        x1_scaled, y1_scaled, r1_scaled = calculate_scaled_values(canvas_width, canvas_height, x1, y1, r1, scale)
        x2_scaled, y2_scaled, r2_scaled = calculate_scaled_values(canvas_width, canvas_height, x2, y2, r2, scale)

        draw_circles(canvas, x1_scaled, y1_scaled, r1_scaled, x2_scaled, y2_scaled, r2_scaled)

        if d < abs(r1 - r2):
            inside_circle_color = "green"
            if r1 > r2:
                canvas.create_oval(x2_scaled - r2_scaled, y2_scaled - r2_scaled, x2_scaled + r2_scaled,
                                   y2_scaled + r2_scaled,
                                   outline=inside_circle_color, width=2)
            else:
                canvas.create_oval(x1_scaled - r1_scaled, y1_scaled - r1_scaled, x1_scaled + r1_scaled,
                                   y1_scaled + r1_scaled,
                                   outline=inside_circle_color, width=2)
            intersection_label.config(
                text="No intersection points. One of the circles is inside the other.", bg="red")
        elif d > r1 + r2:
            intersection_label.config(text="No Intersection. Separate Circles.", bg="red")
        elif d == 0 and r1 == r2:
            inside_circle_color = "green"
            canvas.create_oval(x1_scaled - r1_scaled, y1_scaled - r1_scaled, x1_scaled + r1_scaled,
                               y1_scaled + r1_scaled,
                               outline=inside_circle_color, width=2)
            canvas.create_oval(x2_scaled - r2_scaled, y2_scaled - r2_scaled, x2_scaled + r2_scaled,
                               y2_scaled + r2_scaled,
                               outline=inside_circle_color, width=2)
            intersection_label.config(
                text="No intersection points. The circles overlap each other.", bg="red")
        else:
            a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
            h = math.sqrt(r1 ** 2 - a ** 2)
            x3 = x1 + a * (x2 - x1) / d
            y3 = y1 + a * (y2 - y1) / d
            x4 = x3 + h * (y2 - y1) / d
            y4 = y3 - h * (x2 - x1) / d
            x5 = x3 - h * (y2 - y1) / d
            y5 = y3 + h * (x2 - x1) / d

            intersection_label.config(
                text=f"Intersection Points: ({round(x4, 2)}, {round(y4, 2)}), ({round(x5, 2)}, {round(y5, 2)})",
                bg="yellow")
            draw_intersection_points(canvas, [(x4, y4), (x5, y5)], scale)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def validate_radius_values(r1, r2):
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


def calculate_scale(canvas_width, canvas_height, x1, y1, r1, x2, y2, r2):
    max_value = max(abs(x1), abs(y1), abs(x2), abs(y2), r1, r2)
    scale = min(canvas_width, canvas_height) / (4 * max_value)
    return scale


def calculate_scaled_values(canvas_width, canvas_height, x, y, r, scale):
    x_scaled = canvas_width / 2 + x * scale
    y_scaled = canvas_height / 2 - y * scale
    r_scaled = r * scale
    return x_scaled, y_scaled, r_scaled


def draw_circles(canvas, x1_scaled, y1_scaled, r1_scaled, x2_scaled, y2_scaled, r2_scaled):
    canvas.create_oval(x1_scaled - r1_scaled, y1_scaled - r1_scaled, x1_scaled + r1_scaled, y1_scaled + r1_scaled,
                       outline="red")
    canvas.create_oval(x2_scaled - r2_scaled, y2_scaled - r2_scaled, x2_scaled + r2_scaled, y2_scaled + r2_scaled,
                       outline="blue")


def draw_intersection_points(canvas, result, scale):
    for point in result:
        x_scaled, y_scaled = scale_coordinates(canvas, point, scale)
        canvas.create_oval(x_scaled - 3, y_scaled - 3, x_scaled + 3, y_scaled + 3, fill="black")


def scale_coordinates(canvas, point, scale):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    x_scaled = canvas_width / 2 + point[0] * scale
    y_scaled = canvas_height / 2 - point[1] * scale
    return x_scaled, y_scaled


def clear_entry():
    canvas.delete("all")
    intersection_label.config(text="", bg="white")
    entry_x1.delete(0, tk.END)
    entry_y1.delete(0, tk.END)
    entry_r1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_y2.delete(0, tk.END)
    entry_r2.delete(0, tk.END)


window = tk.Tk()
window.title("Circle Intersection Calculator")

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

canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.grid(row=0, column=2, rowspan=9, padx=10, pady=5)

intersection_label = tk.Label(window, text="", bg="white")
intersection_label.grid(row=9, column=0, columnspan=3, padx=5, pady=5, sticky="W")

button_calculate = tk.Button(window, text="Calculate", command=handle_button_click)
button_calculate.grid(row=8, column=0, padx=5, pady=5)

# Create the Clear button
button_clear = tk.Button(window, text="Clear", command=clear_entry)
button_clear.grid(row=8, column=1, padx=5, pady=5)

window.mainloop()
