#!/usr/bin/env python3
from tkinter import ttk
import tkinter as tk
from . import bmiutils


class BmiWindow(ttk.Frame):
    def __init__(self, master):
        super(BmiWindow, self).__init__(master)
        master.wm_title('BMI Calculator')
        # Bind Return to calculate
        master.bind('<Return>', self.calculate)

        # Create UI widgets
        # Lables
        self.weight_lable = ttk.Label(master, text='Weight(kg)', background='white')
        self.height_lable = ttk.Label(master, text='Height(cm)', background='white')
        self.result_lable = ttk.Label(master)
        self.verdict_lable = ttk.Label(master)

        # Entrys
        self.weight_entry = ttk.Entry(master, justify=tk.RIGHT)
        self.height_entry = ttk.Entry(master, justify=tk.RIGHT)

        # Buttons
        self.calculate_button = ttk.Button(master, text='Calculate', command=self.calculate)

        # Layout widgets
        self.weight_lable.grid(row=0, column=0, sticky=tk.NW, padx=14, pady=10)
        self.weight_entry.grid(row=0, column=1, sticky=tk.NE, padx=10, pady=10)
        self.height_lable.grid(row=1, column=0, sticky=tk.NW, padx=14)
        self.height_entry.grid(row=1, column=1, sticky=tk.NE, padx=10)
        self.calculate_button.grid(row=2, column=0, sticky=tk.SW, pady=18)
        self.result_lable.grid(row=2, column=1, sticky=tk.SE, padx=10, pady=18)
        self.verdict_lable.grid(row=3, rowspan=2, columnspan=2, sticky=tk.SW, padx=14)

    def calculate(self, event=None):
        bmi = bmiutils.bmi_calculate(self.weight_entry.get(), self.height_entry.get())
        verdict = bmiutils.bmi_verdict(bmi)
        self.result_lable.config(text='BMI: {0:.2f}'.format(bmi), foreground='red')
        self.verdict_lable.config(text='{0}'.format(verdict), foreground='blue')
