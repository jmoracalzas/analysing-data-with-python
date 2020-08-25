#!/usr/bin/env python
from datetime import date, timedelta
from random import choice, randint


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

    def getIncLinesMonth(self):
        return self.__setIncLines

    def getExpLinesMonth(self):
        return self.__setExpLines

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
    expenditureType = (
        "Purchase of materials",
        "Rent",
        "Electricity",
        "Salaries",
    )

    incomeType = ("Sale of products", "Rendering of services")

    costCentre = (
        "Sales",
        "Distribution",
        "Production",
        "Administration",
    )
    intData = []

    def __init__(self, years, incLines, expLines):
        super().__init__(years, incLines, expLines)

    def generateIncData(self):
        print("income lines:", self.getNumYears() * 12 * self.getIncLinesMonth())
        print("----------------------")
        rowData = []
        for i in self.generateReportingDates():
            for j in range(12):
                for inc in range(self.getIncLinesMonth()):
                    period = i[j]
                    incType = choice(self.incomeType)
                    row = (
                        period
                        + "-"
                        + "Actual"
                        + "-"
                        + "Income"
                        + "-"
                        + incType
                        + "-"
                        + self.costCentre[0]
                        + "-"
                        + incType
                        + "-"
                        + "monthly transactions"
                        + "-"
                        + str(randint(1, 10000000) / 100)
                    )
                    rowData.append(row)
                    print(rowData)


def main():
    print()


if __name__ == "__main__":
    main()
