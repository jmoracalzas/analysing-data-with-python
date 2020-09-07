#!/usr/bin/env python
from tkinter import *
from sys import path

path.append("./Project_1/python/customClasses")
from guiLayout import GuiWindow


def main():
    # Generating the GUI and setting up its properties
    root = Tk()

    root.geometry("600x280+25+25")
    # root.resizable(False, False)
    root.title("Project 1: Data Generation and Data Export")
    welcomeWin = GuiWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
