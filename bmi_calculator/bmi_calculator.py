#! /usr/bin/local python3
from tkinter import ttk
import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super(MainWindow, self).__init__(master)
        master.wm_title("BMI Calculator")

        self.age_lable = ttk.Label(master, text='1 Age:(Exm:22)', anchor=tk.W, justify=tk.LEFT, width=30)
        self.age_lable.grid(row=0, column=0, stick=tk.W)
        self.age_entry = ttk.Entry(master, foreground='red', width=9)
        self.age_entry.grid(row=0, column=1, stick=tk.W)

        self.weight_lable = ttk.Label(master, text='2 Weight:(Kg)', anchor=tk.W, justify=tk.LEFT, width=30)
        self.weight_lable.grid(row=1, column=0, stick=tk.W)
        self.weight_entry = ttk.Entry(master, foreground='green', width=9)
        self.weight_entry.grid(row=1, column=1, stick=tk.W)

        self.height_lable = ttk.Label(master, text='3 Height:(m)', anchor=tk.W, justify=tk.LEFT, width=30)
        self.height_lable.grid(row=2, column=0, stick=tk.W)
        self.height_entry = ttk.Entry(master, foreground='blue', width=9)
        self.height_entry.grid(row=2, column=1, stick=tk.W)

        self._GENDER_DICT = {
            'Male': 'M',
            'Female': 'F'
        }
        self._gender = tk.StringVar()
        ttk.Radiobutton(master, text='Male', variable=self._gender, value='M').grid(row=4, column=0, stick=tk.W)
        ttk.Radiobutton(master, text='Female', variable=self._gender, value='F').grid(row=4, column=1, stick=tk.W)

        self.calculator_button = ttk.Button(master, text='Check it', width=30, command=lambda: self.bmi_calculator)
        self.calculator_button.grid(row=5, column=0, stick=tk.W)

        self.result_lable = tk.Label(master, text='BMI = ', foreground='brown', anchor=tk.W, width=9)
        self.result_lable.grid(row=5, column=1, stick=tk.W)

        self.advice_lable = tk.Label(master, width=30)
        self.advice_lable.grid(row=6, rowspan=2, stick=tk.W)

    @property
    def bmi_calculator(self):
        w = float(self.weight_entry.get())
        h = float(self.height_entry.get())
        return self.set(w / pow(h, h))

    @property
    def advice(self):
        message = ('Try to keep your BMI equal to 22, Buddy!', 'Try to keep your BMI equal to 22, Lady!')
        if self._gender.get() is 'M':
            return message[0]
        elif self._gender.get() is 'F':
            return message[1]

    def set(self, result):
        self.result_lable.config(text='BMI = %.2f' % result)
        self.advice_lable.config(text=self.advice)


root = tk.Tk()
MainWindow(root).mainloop()
