#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from sys import path

path.append("./Project_1/python/customClasses")
from guiClasses import DataAnalysisApp

# Generating the GUI
root = Tk()
welcomeWin = DataAnalysisApp(root)


root.mainloop()

