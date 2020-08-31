from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):

        winFrame = ttk.Frame(master, height=650, width=850)
        winFrame.grid()

        # creating the title frame and its contents
        title = ttk.Label(
            winFrame, text="Welcome to my portolio", justify="center", padding=(20, 0),
        ).grid(row=0, column=0)

        # # creating the menu frame and its content
        # menuFrame = ttk.Frame(winFrame, width=25, relief=SUNKEN, border=5,).grid(
        #     row=1, column=0
        # )
        actionButton = ttk.Button(winFrame, text="Settings").grid(
            row=1, column=0, sticky="w"
        )
        closeButton = ttk.Button(winFrame, text="Exit").grid(
            row=2, column=0, sticky="w"
        )

        # creating the display area text and its content
        # dispAreaFrame = ttk.Frame(winFrame, width=825).grid(
        #     row=1, column=1, columnspan=2
        # )

        displayArea = ttk.Label(
            winFrame, text="hello world world", justify="left"
        ).grid(row=1, column=1)
        # # displayArea.pack()

        #


def main():
    pass


if __name__ == "__main__":
    main()

