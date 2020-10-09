#!/usr/bin/env python
from tkinter import *
from tkinter import ttk, messagebox
import sys

from dataGenClasses import interimData
from exportOutput import TXTFiles, ExcelExport


class GuiWindow:
    # to store setting from the GUI to be passed to other functions
    # choiceCSVExp = ""
    # choiceXMLExp =    ""
    # choiceJSONExp = ""
    # choiceSQLiteExp = ""

    # to store the generated interim data before creating the files
    userData = []
    ccList = []
    incList = []
    expDict = {}
    builtData = None

    def __init__(self, master):
        # creating a tuple to store the user input
        self.userSettings = []

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
        self.settingsDisplay.add(self.dataTypeSet, text="Output Settings")

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

        # executes the functions to created the notebook widgets
        self.basicSettingsLayout()
        self.typeExportSettings()

        # converts the 'settings' button into the 'set' button
        self.settingsButton.config(text="Set", command=self.setDataCallBack)

    # the following functions creates the 'basic settings' widgets
    def basicSettingsLayout(self):
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
            text="How many variable expenditure transactions would you like to generate every month?",
            wraplength=250,
            justify="left",
        ).grid(row=2, column=0, sticky="w", pady=10, padx=5)

        self.expLinesEntered = StringVar()
        self.expLinesInput = ttk.Entry(
            self.basicSettings, textvariable=self.expLinesEntered
        ).grid(row=2, column=1)

    # the following functions creates the 'output settings' widgets
    # data type section
    def typeExportSettings(self):
        self.dataTypeGroup = ttk.LabelFrame(
            self.dataTypeSet, text="Type of data to generate"
        )
        self.dataTypeGroup.pack(anchor="w", padx=15, pady=10, side=LEFT)
        ##########################################################################

        # Creating the export frame options
        self.outputTypeGroup = ttk.LabelFrame(
            self.dataTypeSet, text="Select the type of output"
        )
        self.outputTypeGroup.pack(anchor="e", padx=15, pady=10)

        # .txt export option
        self.choiceTXTExp = BooleanVar()
        # self.choiceTXTExp = False

        ttk.Checkbutton(
            self.outputTypeGroup,
            text=".txt",
            variable=self.choiceTXTExp,
            onvalue=True,
            offvalue=False,
        ).pack(padx=10, pady=5, anchor="w")

        # .CSV export option
        ttk.Checkbutton(self.outputTypeGroup, text=".CSV", variable="").pack(
            padx=10, pady=5, anchor="w"
        )

        # .XML export option
        ttk.Checkbutton(self.outputTypeGroup, text=".XML", variable="").pack(
            padx=10, pady=5, anchor="w"
        )

        # .JSON export option
        ttk.Checkbutton(self.outputTypeGroup, text=".JSON", variable="").pack(
            padx=10, pady=5, anchor="w"
        )

        # .Excel export option
        self.choiceXLSExport = BooleanVar()

        ttk.Checkbutton(
            self.outputTypeGroup, text="Microsoft Excel", variable=self.choiceXLSExport
        ).pack(padx=10, pady=5, anchor="w")

        # .SQLITE export option
        ttk.Checkbutton(self.outputTypeGroup, text="SQLite", variable="").pack(
            padx=10, pady=5, anchor="w"
        )

        ############################################################################
        # Determining the data type to generate
        self.infoType = StringVar()
        self.infoType.set("Actual")

        checkActual = ttk.Radiobutton(
            self.dataTypeGroup,
            variable=self.infoType,
            text="Actual amounts",
            value="Actual",
        ).pack(anchor="w", padx=10, pady=3)

        checkBudget = ttk.Radiobutton(
            self.dataTypeGroup,
            variable=self.infoType,
            text="Budget amounts",
            value="Budget",
        ).pack(anchor="w", padx=10, pady=3)

        checkBoth = ttk.Radiobutton(
            self.dataTypeGroup,
            variable=self.infoType,
            text="Actual and budget amounts",
            value="Both",
        ).pack(anchor="w", padx=10, pady=3)

    #########################################################################
    # Generating the dataset
    # This method passes the user input to start generating the data
    def setDataCallBack(self):
        # This method stores the user settings into a list
        try:
            self.yearsPassed = int(self.yearsEntered.get())
            self.incLinesPassed = int(self.incLinesEntered.get())
            self.expLinesPassed = int(self.expLinesEntered.get())
            self.dataTypePassed = self.infoType.get()

            # emptying previous settings and passing the new parameters
            del self.userSettings[::]

            self.userSettings.append(self.yearsPassed)
            self.userSettings.append(self.incLinesPassed)
            self.userSettings.append(self.expLinesPassed)
            self.userSettings.append(self.dataTypePassed)

        except ValueError:
            messagebox.showinfo(
                title="Error", message="Incorrect input. Please try again."
            )

    # This function create the interimData object and generates the dataset
    # and stores the categories in preparation to create the output files
    def buildDataCallBack(self):
        try:
            dataSet = interimData(
                self.userSettings[0],  # years
                self.userSettings[1],  # noIncLines
                self.userSettings[2],  # no ExpLines
                self.userSettings[3],  # dataType
            )
            # Storing the user data in this class variable before passing it
            self.userData = dataSet.createDataSet()

            # obtaining categories before creating the output files
            self.ccList = tuple(dataSet.getCostCentres())
            self.incList = tuple(dataSet.getIncList())
            self.expDict = dataSet.getExpList()

            # To marked that the interim data has been created
            self.builtData = True

        except IndexError:
            messagebox.showinfo(
                "Basic Settings",
                message=(
                    "Please complete the settings and click 'set' before generating the output"
                ),
            )

    ###########################################################################
    # Exporting the dataset
    def exportCallBack(self):

        if self.builtData:
            # TXT export
            if self.choiceTXTExp.get():
                txtOutput = TXTFiles(
                    self.ccList, self.incList, self.expDict, self.userData
                )
                txtOutput.createTXTfiles()

            # Excel export
            if self.choiceXLSExport.get():
                wb = ExcelExport()  # instance of the MS Excel object
                wb.xlsStructure(wb)

        else:
            messagebox.showinfo(
                title="Export data",
                message='Press "Build Data" before exporting the output.',
            )

    ###########################################################################
    # Exiting the application
    def exitApp(self):
        sys.exit(0)


def main():
    pass


if __name__ == "__main__":
    main()
