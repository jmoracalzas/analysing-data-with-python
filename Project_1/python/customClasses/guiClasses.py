from email import message
from logging import root
from sys import hexversion
from textwrap import wrap
from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):

        # creating the menu frame and its content
        menuFrame = ttk.Frame(master, width=100, height=200, border=1)
        menuFrame.place(x=15, y=15)

        settingsButton = ttk.Button(menuFrame, text="Settings")
        settingsButton.pack(pady=5, padx=5)

        getDataButton = ttk.Button(menuFrame, text="Get Data")
        getDataButton.pack(padx=5, pady=5)

        exportButton = ttk.Button(menuFrame, text="Export")
        exportButton.pack(padx=5, pady=5)

        closeButton = ttk.Button(master, text="Exit", command=exit)
        closeButton.place(x=15, y=240)

        # creating the display area text and its content
        dispAreaFrame = ttk.Frame(master, width=385, border=5, relief=SOLID)
        dispAreaFrame.place(x=115, y=15)

        welcomeMsg = "This project generates a set of random data based on the user input, stores the result and facilitates its export. \n\n It has been built using the Python Standard Library and the Tkinter modules"
        displayArea = ttk.Label(
            dispAreaFrame,
            text=welcomeMsg,
            justify="left",
            background="yellow",
            wraplength=375,
        )
        displayArea.pack(fill="both")

    def exit():
        root.destroy()


def main():
    pass


if __name__ == "__main__":
    main()

