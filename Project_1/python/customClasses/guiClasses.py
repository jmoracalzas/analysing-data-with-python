from tkinter import *
from tkinter import ttk

from click.decorators import command


class DataAnalysisApp:
    def __init__(self, master):

        # creating the menu frame and its content
        self.menuFrame = ttk.Frame(master, width=100, height=200, border=1)
        self.menuFrame.place(x=15, y=15)

        self.settingsButton = ttk.Button(
            self.menuFrame, text="Settings", command=self.userInputLayout
        )
        self.settingsButton.pack(pady=10, padx=10)

        self.getDataButton = ttk.Button(self.menuFrame, text="Create Data")
        self.getDataButton.pack(padx=10, pady=10)

        self.exportButton = ttk.Button(self.menuFrame, text="Export")
        self.exportButton.pack(padx=10, pady=10)

        self.closeButton = ttk.Button(master, text="Exit", command=self.exitApp)
        self.closeButton.place(x=20, y=240)

        # creating the display area (notebook) text and its content
        self.dispAreaFrame = ttk.Frame(master, width=485)
        self.dispAreaFrame.place(x=115, y=15)

        welcomeMsg = "This project generates a set of random data based on the user input, stores the result and facilitates its export. \n\n It has been built using the Python Standard Library and the Tkinter modules"
        self.dispAreaLabel = ttk.Label(
            self.dispAreaFrame,
            text=welcomeMsg,
            justify="left",
            wraplength=375,
            padding=10,
        )
        self.dispAreaLabel.pack(padx=10)

        # Creating the settings display notebook
        self.settingsDisplay = ttk.Notebook(self.dispAreaFrame, padding=15)
        self.settingsDisplay.pack()

        self.basicSettings = ttk.Frame(self.settingsDisplay)
        self.settingsDisplay.add(
            self.basicSettings, text="Basic Settings",
        )

        self.dataTypeSet = ttk.Frame(self.settingsDisplay)
        self.settingsDisplay.add(self.dataTypeSet, text="Data Type")

        self.incSettings = ttk.Frame(self.settingsDisplay)
        self.settingsDisplay.add(self.incSettings, text="Income Settings")

        self.expSettings = ttk.Frame(self.settingsDisplay)
        self.settingsDisplay.add(self.expSettings, text="Expenditure Settings")

        # hidding the sections of the notebook
        for i in range(self.settingsDisplay.index("end")):
            self.settingsDisplay.tab(i, state="hidden")

    def userInputLayout(self):
        #     # hides the display label, unhides the display notebook
        #     and inserts the widgets to collect the user input

        self.dispAreaLabel.forget()
        self.settingsDisplay.select(0)

        for i in range(self.settingsDisplay.index("end")):
            self.settingsDisplay.tab(i, state="normal")

        self.settingsButton.config(text="Set", command="")

        # Number of years section
        self.yearsLabel = ttk.Label(
            self.basicSettings,
            text="Enter the desired number of years you would like to generate data for:",
            wraplength=255,
            justify="left",
        ).grid(row=0, column=0, pady=10, padx=10)

        self.yearsInput = ttk.Entry(self.basicSettings).grid(
            row=0, column=1, pady=10, padx=10
        )

        # Income section
        self.incLinesLabel = ttk.Label(
            self.basicSettings,
            text="How many income transactions would you like to generate every month?",
            wraplength=255,
            justify="left",
        ).grid(row=1, column=0, padx=10, pady=10)

        self.incLinesInput = ttk.Entry(self.basicSettings).grid(
            row=1, column=1, padx=10, pady=10
        )

        # Expenditure sections
        self.expLinesLabel = ttk.Label(
            self.basicSettings,
            text="How many expenditure transactions would you like to generate every month?",
            wraplength=255,
            justify="left",
        ).grid(row=2, column=0, padx=10, pady=10)

        self.expLinesInput = ttk.Entry(self.basicSettings).grid(
            row=2, column=1, padx=10, pady=10
        )

    def exitApp(self):
        exit()


def main():
    pass


if __name__ == "__main__":
    main()

