import tkinter as tk
from tkinter import ttk
import ttkbootstrap
import math
from setting_window import SettingWindow
from get_solutions import get_solutions


# * Main Variables & Functionality * #
window = ttkbootstrap.Window(themename="darkly")
window.title("Circular Function")
window.config(padx=12, pady=12)

# * <- Main Variables & Functionality -> * #
angle_type = tk.StringVar(value="Degrees")  # Degrees | Radian
decimal_places = tk.IntVar(value=2)

angle_val = tk.DoubleVar(value=0)  # Value of the given angle


def solve_given():
    """Solves all of the trigonometric values and display it on screen"""

    given_angle = angle_val.get()
    if angle_type.get() == "Degrees":
        given_angle = math.radians(given_angle) # converts to radians for solving purposes


    answer_dict = get_solutions(given_angle,decimal_places.get())

    # -- Update Display -- #
    sine_solution.config(text=f"Sin(θ): {answer_dict["sine"]}")
    cosine_solution.config(text=f"Cos(θ): {answer_dict["cosine"]}")
    tangent_solution.config(text=f"Tan(θ): {answer_dict["tangent"]}")
    cosecant_solution.config(text=f"Csc(θ): {answer_dict["cosecant"]}")
    secant_solution.config(text=f"Sec(θ): {answer_dict["secant"]}")
    cotangent_solution.config(text=f"Cot(θ); {answer_dict["cotangent"]}")


# * <- Setting Functionality -> * #
setting_window = None
def toggle_setting():
    """Opens/Close Setting Window"""
    global setting_window
    if not SettingWindow.currently_exist:
        setting_window = SettingWindow(angle_type,decimal_places)  # This opens the setting window
    else:
        setting_window.close_setting()


# * <- Main Ui Elements -> * #

# -- Header -- #
header = ttk.Label(
    window,
    text="Circular Function Calculator \n Using Angle",
    justify="center",
    font="Calibri 24 bold",
)
header.pack()


# -- Solution -- #
solution_header = ttk.Label(
    window,
    text="Solution",
    justify="center",
    font="Calibri 16 bold",
)
solution_frame = ttk.Frame(window)

sine_solution = ttk.Label(
    solution_frame, text="Sin(θ): ", font="Calibri 16", padding=(40, 5)
)
cosine_solution = ttk.Label(
    solution_frame, text="Cos(θ): ", font="Calibri 16", padding=(40, 5)
)
tangent_solution = ttk.Label(
    solution_frame, text="Tan(θ): ", font="Calibri 16", padding=(40, 5)
)

cosecant_solution = ttk.Label(
    solution_frame, text="Csc(θ): ", font="Calibri 16", padding=(40, 5)
)
secant_solution = ttk.Label(
    solution_frame, text="Sec(θ): ", font="Calibri 16", padding=(40, 5)
)
cotangent_solution = ttk.Label(
    solution_frame, text="Cot(θ): ", font="Calibri 16", padding=(40, 5)
)

solution_header.pack()
solution_frame.pack()

sine_solution.grid(column=0, row=0)
cosine_solution.grid(column=0, row=1)
tangent_solution.grid(column=0, row=2)

cosecant_solution.grid(column=1, row=0)
secant_solution.grid(column=1, row=1)
cotangent_solution.grid(column=1, row=2)

# -- Given Entries -- #

given_header = ttk.Label(
    window,
    text="Given",
    justify="center",
    font="Calibri 16 bold",
)


# Angle Entries
given_angle_frame = ttk.Frame(window, padding=(0, 10))
angle_label = ttk.Label(
    given_angle_frame, text="Angle:", font="Calibri 16", padding=(5, 0)
)
angle_entry = ttk.Entry(given_angle_frame, textvariable=angle_val)
angle_type_label = ttk.Label(
    given_angle_frame, textvariable=angle_type, font="Calibri 8", padding=(5, 0)
)

# Given Positioning
given_header.pack()

given_angle_frame.pack()
angle_label.grid(column=0, row=0)
angle_entry.grid(column=1, row=0)
angle_type_label.grid(column=2, row=0)

# -- Solve Button -- #
solve_button = ttk.Button(window, text="Solve", padding=(0, 10), command=solve_given)
solve_button.pack(fill="x")

# -- Setting -- #
setting_button = ttk.Button(text="setting", command=toggle_setting)
setting_button.pack(anchor="ne", pady=10)

window.mainloop()
