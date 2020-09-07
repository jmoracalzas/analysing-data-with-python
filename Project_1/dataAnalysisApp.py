#!/usr/bin/env python
from tkinter import *
from sys import path

path.append("./Project_1/python/customClasses")
from guiClasses import DataAnalysisApp
from dataGenClasses import Rules, interimData


def main():
    # Generating the GUI and setting up its properties
    root = Tk()

    root.geometry("600x280+25+25")
    # root.resizable(False, False)
    root.title("Project 1: Data Generation and Data Export")
    welcomeWin = DataAnalysisApp(root)
    root.mainloop()

    dataSet = ""


if __name__ == "__main__":
    main()

    # years = input("How many years does the data need to reflect? ")
    # incLines = input("How many lines of income would you like to generate each month? ")
    # expLines = input(
    #     "How many lines of expenditure would you like to generate every month? "
    # )

    # setOne = interimData(years, incLines, expLines)
    # print(setOne.generateExpData())
