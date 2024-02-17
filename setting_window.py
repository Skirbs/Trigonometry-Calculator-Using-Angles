import tkinter as tk
from tkinter import ttk


# * <- Settings Ui Elements -> * #
class SettingWindow(tk.Toplevel):
    currently_exist = False

    def __init__(self, angle_var, decimal_places_var):
        super().__init__()
        SettingWindow.currently_exist = True
        self.protocol("WM_DELETE_WINDOW", self.close_setting)

        self.config(padx=40, pady=10)

        self.angle_var = angle_var
        self.decimal_places_var = decimal_places_var

        self.build_gui()

    def build_gui(self):
        """Creates the widgets necessary for the settings window"""

        # -- Header -- #
        header = ttk.Label(
            self,
            text="Settings",
            justify="center",
            font="Calibri 16 bold",
        )
        header.pack()

        # -- Angle Type Radiobuttons -- #
        angle_type_frame = ttk.Frame(self)
        angle_header = ttk.Label(angle_type_frame, text="Angle Type", font="Calibri 16")

        degrees_radiobutton = ttk.Radiobutton(
            angle_type_frame,
            variable=self.angle_var,
            value="Degrees",
            text="Degrees",
            padding=(0, 5),
        )
        radians_radiobutton = ttk.Radiobutton(
            angle_type_frame,
            variable=self.angle_var,
            value="Radians",
            text="Radians",
            padding=(0, 5),
        )

        # Positioning
        angle_type_frame.pack()
        angle_header.grid(column=0, row=0, columnspan=2, sticky="WE")

        degrees_radiobutton.grid(column=0, row=1)
        radians_radiobutton.grid(column=0, row=2)

        angle_type_frame.pack()

        # -- Roundoff Radiobuttons -- #
        decimal_places_label = ttk.Label(
            self, text="Decimal Places", font="Calibri 16", padding=(0, 5)
        )
        decimal_places_spinbox = ttk.Spinbox(
            self, from_=1, to=10, textvariable=self.decimal_places_var
        )
        decimal_places_label.pack()
        decimal_places_spinbox.pack()

    def close_setting(self):
        """Executes when closing off setting window"""
        SettingWindow.currently_exist = False
        self.destroy()
