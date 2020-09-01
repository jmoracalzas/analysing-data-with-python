from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):

        winFrame = ttk.Frame(master).grid()

        # creating the title frame and its contents
        title = ttk.Label(
            winFrame, text="Welcome to my portolio", justify="center", padding=(0, 2),
        ).grid(row=0, column=0, columnspan=1)

        # creating the menu frame and its content
        menuFrame = ttk.Frame(master, width=25, relief=RIDGE, border=5).grid(
            row=2, column=0
        )

        actionButton = ttk.Button(menuFrame, text="Settings", padding=(2, 2)).grid(
            row=2, column=0, rowspan=1
        )

        closeButton = ttk.Button(menuFrame, text="Exit", padding=(2, 2)).grid(
            row=3, column=0
        )

        # creating the display area text and its content
        dispAreaFrame = ttk.Frame(master, height=50, width=200, relief=RIDGE).grid(
            row=2, column=1
        )

        displayArea = ttk.Label(
            dispAreaFrame, text="hello \world \world", justify="center"
        ).grid(row=2, column=1, sticky="nsew")


def main():
    pass


if __name__ == "__main__":
    main()

