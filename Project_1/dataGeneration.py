#!/usr/bin/env python

from sys import path

path.append("./customClasses")
from dataGenClasses import Rules, interimData

# dataGenClasses import Rules, interimData

# This part of the code will :
# - generate a list of transactions (income and expenditure) based the input obtained from the user
# - will store the dataset


def main():

    years = input("How many years does the data need to reflect? ")
    incLines = input("How many lines of income would you like to generate each month? ")
    expLines = input(
        "How many lines of expenditure would you like to generate every month? "
    )

    setOne = interimData(years, incLines, expLines)
    print(setOne.generateIncData())


if __name__ == "__main__":
    main()
