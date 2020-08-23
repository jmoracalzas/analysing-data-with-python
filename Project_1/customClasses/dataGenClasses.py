#!/usr/bin/env python
from datetime import date, timedelta


class Rules:

    # To store the initial parameters set by the user
    # used to determine the total number of lines to generate
    def __init__(self, years, incLines, expLines):
        self.__setNoYears = int(years)
        self.__setIncLines = int(incLines)
        self.__setExpLines = int(expLines)
        self.startDate = date.today()

    def getNumYears(self):
        return self.__setNoYears

    def getNumIncEntries(self):  # total number of income lines
        incLines = self.__setNoYears * 12 * self.__setIncLines
        return incLines

    def getNumExpEntries(self):  # total number of expenditure lines
        expLines = self.__setNoYears * 12 * self.__setExpLines
        return expLines

    def generateReportingDates(self):
        # To generate the reporting periods based on the user input
        calendar = tuple(
            [
                [
                    str(self.startDate.day)
                    + "/"
                    + str(i + 1)
                    + "/"
                    + str((self.startDate - timedelta(days=365 * j)).year)
                    for i in range(12)
                ]
                for j in range(self.__setNoYears)
            ]
        )
        return calendar


class interimData(Rules):
    def __init__(self, years, incLines, expLines):
        super().__init__(years, incLines, expLines)
        self.__setNoIncEntries = self.getNumIncEntries()
        self.__setNoExpEntries = self.getNumExpEntries()
        self.__expenditureType = (
            "Purchase of materials",
            "Rent",
            "Electricity",
            "Salaries",
        )
        self.__incomeType = ["Sale of products", "Rendering of services"]

    def generateDataSet(self, incLines, expLines):
        pass


def main():
    print()


if __name__ == "__main__":
    main()
