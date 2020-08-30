from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):
        title = ttk.Label(
            master, text="Welcome to my portolio", background="white", justify="right",
        )
        title.pack()

        displayArea = Message(
            master,
            text="hello \
            world\
                world",
        )
        displayArea.pack()

        actionButton = ttk.Button(master, text="Settings")
        actionButton.pack()
        closeButton = ttk.Button(master, text="Exit")
        closeButton.pack()


def main():
    pass


if __name__ == "__main__":
    main()

