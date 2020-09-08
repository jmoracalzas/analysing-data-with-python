from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from click.decorators import command
from dataGenClasses import Rules, interimData


class GuiWindow:
    def __init__(self, master):
        # creating the pain window
        self.painWindow = ttk.PanedWindow(master, orient=HORIZONTAL)
        self.painWindow.pack(fill=BOTH, expand=True)

        # creating the menuFrame and the dispAreaFrame
        self.menuFrame = ttk.Frame(
            self.painWindow, width=150, height=280, border=2, relief=RIDGE
        )
        self.dispAreaFrame = ttk.Frame(master, width=450, height=280)

        self.painWindow.add(self.menuFrame, weight=1)
        self.painWindow.add(self.dispAreaFrame, weight=4)

        # creating the menuFrame content
        self.settingsButton = ttk.Button(
            self.menuFrame, text="Settings", command=self.userInputCallBack,
        )
        self.settingsButton.pack(pady=10)

        self.getDataButton = ttk.Button(
            self.menuFrame, text="Build Data", command=self.buildDataCallBack
        )
        self.getDataButton.pack(pady=10)

        self.exportButton = ttk.Button(
            self.menuFrame, text="Export", command=self.exportCallBack
        )
        self.exportButton.pack(pady=10)

        self.closeButton = ttk.Button(self.menuFrame, text="Exit", command=self.exitApp)
        self.closeButton.pack(pady=10)

        # creating the display area introductory label
        welcomeMsg = "This project generates a set of random data based on the user input, stores the result and facilitates its export. \n\n It has been built using the Python Standard Library and the Tkinter modules"
        self.dispAreaLabel = ttk.Label(
            self.dispAreaFrame, text=welcomeMsg, wraplength=425
        )
        self.dispAreaLabel.pack(anchor="w", padx=10, pady=10)

        # Creating the settings display notebook
        self.settingsDisplay = ttk.Notebook(self.dispAreaFrame)
        self.settingsDisplay.pack(pady=10)

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

    # The method shown below hides the display label, unhides the display notebook
    # and inserts the widgets to collect the user input
    def userInputCallBack(self):

        self.dispAreaLabel.forget()
        self.settingsDisplay.select(0)

        for i in range(self.settingsDisplay.index("end")):
            self.settingsDisplay.tab(i, state="normal")

        # Number of years section

        self.yearsLabel = ttk.Label(
            self.basicSettings,
            text="Enter the desired number of years you would like to generate data for:",
            wraplength=250,
            justify="left",
        ).grid(row=0, column=0, sticky="w", pady=10, padx=5)

        self.yearsEntered = StringVar()

        self.yearsInput = ttk.Entry(
            self.basicSettings, textvariable=self.yearsEntered,
        ).grid(row=0, column=1)

        # Income section
        self.incLinesLabel = ttk.Label(
            self.basicSettings,
            text="How many income transactions would you like to generate every month?",
            wraplength=250,
        ).grid(row=1, column=0, sticky="w", pady=10, padx=5)

        self.incLinesEntered = StringVar()

        self.incLinesInput = ttk.Entry(
            self.basicSettings, textvariable=self.incLinesEntered
        ).grid(row=1, column=1)

        # Expenditure sections
        self.expLinesLabel = ttk.Label(
            self.basicSettings,
            text="How many expenditure transactions would you like to generate every month?",
            wraplength=250,
            justify="left",
        ).grid(row=2, column=0, sticky="w", pady=10, padx=5)

        self.expLinesEntered = StringVar()
        self.expLinesInput = ttk.Entry(
            self.basicSettings, textvariable=self.expLinesEntered
        ).grid(row=2, column=1)

        self.settingsButton.config(text="Set", command=self.setDataCallBack)

    # This method passes the user input to start generating the data
    def setDataCallBack(self):
        try:
            self.yearsPassed = int(self.yearsEntered.get())
            self.incLinesPassed = int(self.incLinesEntered.get())
            self.expLinesPassed = int(self.expLinesEntered.get())

            userData = interimData(
                self.yearsPassed, self.incLinesPassed, self.expLinesPassed
            )
            # These two lines have been added for testing purposes
            print(userData.generateExpData())
            print(userData.generateIncData())

        except ValueError:
            messagebox.showinfo(
                title="Error", message="Incorrect input. Please try again."
            )

    def buildDataCallBack(self):
        messagebox.showinfo(title="Build Data", message="Work in progress")

    def exportCallBack(self):
        messagebox.showinfo(title="Build Data", message="Work in progress")

    def exitApp(self):
        exit()


def main():
    pass


if __name__ == "__main__":
    main()
