#!/usr/bin/env python3


class Rules:

    # To store the initial parameters set by the user
    # used to determine the total number of lines to generate
    def __init__(self, years, incLines, expLines):
        self.__setNoYears = int(years)
        self.__setIncLines = int(incLines)
        self.__setExpLines = int(expLines)

    def getNumYears(self):
        return self.__setNoYears

    def getNumIncEntries(self):  # total number of income lines
        incLines = self.__setNoYears * 12 * self.__setIncLines
        return incLines

    def getNumExpEntries(self):  # total number of expenditure lines
        expLines = self.__setNoYears * 12 * self.__setExpLines
        return expLines


class interimData(Rules):
    def __init__(self, years, incLines, expLines):
        super().__init__(years, incLines, expLines)
        self.__setNoIncEntries = self.getNumIncEntries()
        self.__setNoExpEntries = self.getNumExpEntries()


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
