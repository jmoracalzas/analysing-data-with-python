from sys import hexversion
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

        closeButton = ttk.Button(master, text="Exit")
        closeButton.place(x=15, y=240)

        # creating the display area text and its content
        dispAreaFrame = ttk.Frame(master, width=385, border=5, relief=SOLID)
        dispAreaFrame.place(x=115, y=15)

        displayArea = ttk.Label(
            dispAreaFrame,
            text="Work in progress... \n:)",
            justify="center",
            background="yellow",
        )
        displayArea.pack(fill="both")


def main():
    pass


if __name__ == "__main__":
    main()

