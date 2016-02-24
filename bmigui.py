#!/usr/bin/env python3
import tkinter as tk
from bmimodule import bmiwindows


root = tk.Tk()
app = bmiwindows.BmiWindow(root)
app.mainloop()
