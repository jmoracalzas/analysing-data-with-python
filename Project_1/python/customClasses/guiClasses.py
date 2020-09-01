from sys import hexversion
from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):

        # creating the menu frame and its content
        menuFrame = ttk.Frame(master, width=25, relief=SOLID, border=5).grid(
            row=0, column=0
        )

        actionButton = ttk.Button(menuFrame, text="Settings", padding=(2, 2)).grid(
            row=0, column=0
        )

        closeButton = ttk.Button(menuFrame, text="Exit", padding=(2, 2)).grid(
            row=1, column=0
        )

        # creating the display area text and its content
        dispAreaFrame = ttk.Frame(master, height=50, width=200, relief=RIDGE).grid(
            row=0, column=1, rowspan=2
        )

        displayArea = ttk.Label(
            dispAreaFrame, text="hello \world \world", justify="center"
        ).grid(row=0, column=1, rowspan=2, sticky="nsew")


def main():
    pass


if __name__ == "__main__":
    main()

