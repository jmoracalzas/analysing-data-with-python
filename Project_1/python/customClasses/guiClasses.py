from textwrap import wrap
from tkinter import *
from tkinter import ttk

from PIL.ImageOps import pad


class DataAnalysisApp:
    def __init__(self, master):

        # creating the menu frame and its content
        self.menuFrame = ttk.Frame(master, width=100, height=200, border=1)
        self.menuFrame.place(x=15, y=15)

        self.settingsButton = ttk.Button(
            self.menuFrame, text="Settings", command=self.userInputLayout
        )
        self.settingsButton.pack(pady=10, padx=10)

        self.getDataButton = ttk.Button(self.menuFrame, text="Get Data")
        self.getDataButton.pack(padx=10, pady=10)

        self.exportButton = ttk.Button(self.menuFrame, text="Export")
        self.exportButton.pack(padx=10, pady=10)

        self.closeButton = ttk.Button(master, text="Exit", command=self.exitApp)
        self.closeButton.place(x=20, y=240)

        # creating the display area text and its content
        self.dispAreaFrame = ttk.Frame(master, width=485)
        self.dispAreaFrame.place(x=115, y=15)

        welcomeMsg = "This project generates a set of random data based on the user input, stores the result and facilitates its export. \n\n It has been built using the Python Standard Library and the Tkinter modules"
        self.dispAreaLabel = ttk.Label(
            self.dispAreaFrame,
            text=welcomeMsg,
            justify="left",
            background="yellow",
            wraplength=375,
        )
        self.dispAreaLabel.pack(padx=10)

    def userInputLayout(self):
        #     # hides the display label and inserts the widgets
        #     # to collect the user input
        self.dispAreaLabel.forget()

        # Number of years section
        self.yearsLabel = ttk.Label(
            self.dispAreaFrame,
            text="Enter the desired number of years you would like to generate data for:",
            wraplength=255,
            justify="left",
        ).grid(row=0, column=0, pady=10, padx=10)

        self.yearsInput = ttk.Entry(self.dispAreaFrame).grid(
            row=0, column=1, pady=10, padx=10
        )

        # Income section
        self.incLinesLabel = ttk.Label(
            self.dispAreaFrame,
            text="How many income transactions would you like to generate every month?",
            wraplength=255,
            justify="left",
        ).grid(row=1, column=0, padx=10, pady=10)

        self.incLinesInput = ttk.Entry(self.dispAreaFrame).grid(
            row=1, column=1, padx=10, pady=10
        )

        # Expenditure sections
        self.expLinesLabel = ttk.Label(
            self.dispAreaFrame,
            text="How many expenditure transactions would you like to generate every month?",
            wraplength=255,
            justify="left",
        ).grid(row=2, column=0, padx=10, pady=10)

        self.expLinesInput = ttk.Entry(self.dispAreaFrame).grid(
            row=2, column=1, padx=10, pady=10
        )

        # settings button
        self.settingsButton = ttk.Button(self.dispAreaFrame, text="Set").grid(
            row=3, column=1, columnspan=2, sticky="e", padx=10
        )

    def exitApp(self):
        exit()


def main():
    # Generating the GUI and setting up its properties
    pass


if __name__ == "__main__":
    main()

