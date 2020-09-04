#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from sys import path

path.append("./Project_1/python/customClasses")
from guiClasses import DataAnalysisApp

# # Generating the GUI and setting up its properties
root = Tk()

root.geometry("600x280+25+25")
root.resizable(False, False)
root.title("Project 1: Data Generation and Data Export")

welcomeWin = DataAnalysisApp(root)

root.mainloop()
