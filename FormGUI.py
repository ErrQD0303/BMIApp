from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from settings import UISettings
import math


class UI(Tk):
    bmi: float
    body_state: str

    def __init__(self):
        super().__init__()

        self.__init_widget()

    def __init_widget(self):

        self.height = 1.5
        self.height_unit = "m"
        self.weight = 50
        self.weight_unit = "kg"
        # setting title
        self.title(UISettings.APP_TITLE)
        # setting window size
        width = UISettings.APP_WIDTH
        height = UISettings.APP_HEIGHT
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg=UISettings.APP_BACKGROUND_COLOR)

        self.header_label = Label(self)
        ft = tkFont.Font(family='Times', size=30)
        self.header_label["font"] = ft
        self.header_label["fg"] = "#333333"
        self.header_label.configure(bg="#%02x%02x%02x" %
                                    (self.winfo_rgb(self.cget('bg'))))
        self.header_label["justify"] = "center"
        self.header_label["text"] = "BMI Kiểm Tra Sức Khỏe"
        self.header_label["relief"] = "ridge"
        self.header_label.place(x=40, y=30, width=410, height=69)

        self.height_label = Label(self)
        ft = tkFont.Font(family='Times', size=12)
        self.height_label["font"] = ft
        self.height_label["fg"] = "#333333"
        self.height_label.configure(bg="#%02x%02x%02x" %
                                    (self.winfo_rgb(self.cget('bg'))))
        self.height_label["justify"] = "center"
        self.height_label["text"] = "Chiều cao"
        self.height_label.place(x=30, y=120, width=98, height=30)

        self.weight_label = Label(self)
        ft = tkFont.Font(family='Times', size=12)
        self.weight_label["font"] = ft
        self.weight_label["fg"] = "#333333"
        self.weight_label.configure(bg="#%02x%02x%02x" %
                                    (self.winfo_rgb(self.cget('bg'))))
        self.weight_label["justify"] = "center"
        self.weight_label["text"] = "Cân nặng"
        self.weight_label.place(x=40, y=190, width=70, height=25)

        self.bmi_result_label = Label(self)
        ft = tkFont.Font(family='Times', size=24)
        self.bmi_result_label["font"] = ft
        self.bmi_result_label["fg"] = "#333333"
        self.bmi_result_label.configure(bg="#%02x%02x%02x" %
                                        (self.winfo_rgb(self.cget('bg'))))
        self.bmi_result_label["justify"] = "center"
        self.bmi_result_label["text"] = "label"
        self.bmi_result_label.place(x=170, y=280, width=150, height=25)

        self.body_state_label = Label(self)
        ft = tkFont.Font(family='Times', size=26)
        self.body_state_label["font"] = ft
        self.body_state_label["fg"] = "#51cf66"
        self.body_state_label.configure(
            bg="#%02x%02x%02x" % (self.winfo_rgb(self.cget('bg'))))
        self.body_state_label["justify"] = "center"
        self.body_state_label["text"] = "Bình thường"
        self.body_state_label.place(x=0, y=310, width=496, height=58)

        self.current_height_label = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        self.current_height_label["font"] = ft
        self.current_height_label["fg"] = "#333333"
        self.current_height_label.configure(
            bg="#%02x%02x%02x" % (self.winfo_rgb(self.cget('bg'))))
        self.current_height_label["justify"] = "center"
        self.current_height_label["text"] = "label"
        self.current_height_label.place(x=410, y=150, width=70, height=25)

        self.current_weight_label = Label(self)
        ft = tkFont.Font(family='Times', size=10)
        self.current_weight_label["font"] = ft
        self.current_weight_label["fg"] = "#333333"
        self.current_weight_label.configure(
            bg="#%02x%02x%02x" % (self.winfo_rgb(self.cget('bg'))))
        self.current_weight_label["justify"] = "center"
        self.current_weight_label["text"] = "label"
        self.current_weight_label.place(x=410, y=220, width=70, height=25)

        self.height_slider = self.__create_slider(
            x=45, y=155, width=360, height=20, label=self.current_height_label, unit="m", from_=0, to=2.5, resolution=0.01, length=100, inital_value=1.5)

        self.weight_slider = self.__create_slider(
            x=45, y=225, width=360, height=20, label=self.current_weight_label, unit="kg", from_=0, to=300, resolution=1, length=100, inital_value=50)

    def __update_value(self, value, label: Label, unit: str):
        # Update the label text with the current value of the slider
        label.configure(text=f"{value} {unit}")
        self.__update_value_and_unit(value, unit)
        self.__calculate_bmi()
        self.__calculate_body_state()
        self.__show_bmi_and_body_state()

    def __update_value_and_unit(self, value, unit):
        if "m" in unit:
            self.height = float(value)
            self.height_unit = unit
        else:
            self.weight = float(value)
            self.weight_unit = unit

    def __calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def __calculate_body_state(self):
        if self.bmi < 18.5:
            self.body_state = "Thiếu cân"
        elif self.bmi < 24.9:
            self.body_state = "Bình thường"
        elif self.bmi < 29.9:
            self.body_state = "Thừa cân"
        elif self.bmi < 34.9:
            self.body_state = "Béo phì"
        else:
            self.body_state = "Siêu béo phì"

    def __show_bmi_and_body_state(self):
        self.bmi_result_label['text'] = "{:.2f}".format(self.bmi)
        self.body_state_label['text'] = self.body_state

    def __create_slider(self, x, y, width, height, label, unit, from_=0, to=10,
                        resolution=0.1, length=100, inital_value=0):

        # Create a scale widget (range slider) as the handle
        new_slider = Scale(self, from_=from_, to=to, resolution=resolution,
                           orient="horizontal", length=length, command=lambda value: self.__update_value(value, label, unit), showvalue=False, cursor="hand2", bd=0, bg="#%02x%02x%02x" %
                           (self.winfo_rgb(self.cget('bg'))), sliderlength=20)

        new_slider.set(inital_value)

        new_slider.place(x=x, y=y, width=width, height=height)

        self.__update_value(value=inital_value, label=label, unit=unit)

        return new_slider
