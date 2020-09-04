from tkinter import *
from tkinter import ttk


class DataAnalysisApp:
    def __init__(self, master):

        # creating the menu frame and its content
        self.menuFrame = ttk.Frame(master, width=100, height=200, border=1)
        self.menuFrame.place(x=15, y=15)

        self.settingsButton = ttk.Button(
            self.menuFrame, text="Settings", command=self.userInputLayout
        )
        self.settingsButton.pack(pady=5, padx=5)

        self.getDataButton = ttk.Button(self.menuFrame, text="Get Data")
        self.getDataButton.pack(padx=5, pady=5)

        self.exportButton = ttk.Button(self.menuFrame, text="Export")
        self.exportButton.pack(padx=5, pady=5)

        self.closeButton = ttk.Button(master, text="Exit", command=self.exitApp)
        self.closeButton.place(x=15, y=240)

        # creating the display area text and its content
        self.dispAreaFrame = ttk.Frame(master, width=385, border=5, relief=SOLID)
        self.dispAreaFrame.place(x=115, y=15)

        welcomeMsg = "This project generates a set of random data based on the user input, stores the result and facilitates its export. \n\n It has been built using the Python Standard Library and the Tkinter modules"
        self.dispAreaLabel = ttk.Label(
            self.dispAreaFrame,
            text=welcomeMsg,
            justify="left",
            background="yellow",
            wraplength=375,
        )
        self.dispAreaLabel.pack()

    def userInputLayout(self):
        #     # hides the display label and inserts the widgets
        #     # to collect the user input
        self.dispAreaLabel.forget()

    def exitApp(self):
        exit()


def main():
    # Generating the GUI and setting up its properties
    pass


if __name__ == "__main__":
    main()

