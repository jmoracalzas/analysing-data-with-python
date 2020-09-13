#!/usr/bin/env python
from datetime import date, timedelta
from random import choice, randint, random


class Rules:

    # To store the initial parameters set by the user
    # used to determine the total number of lines to generate
    def __init__(self, years, incLines, expLines, infoType):
        self.__setNoYears = years
        self.__setIncLines = incLines
        self.__setExpLines = int(expLines)
        self.infoType = infoType
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

    def __init__(self, years, incLines, expLines, infoType):
        super().__init__(years, incLines, expLines, infoType)

    # calculates the no of income lines to generate and creates the income dataset
    def generateIncData(self):
        print("income lines:", self.getNumYears() * 12 * self.getIncLinesMonth())
        print("----------------------")
        # to temporary store the income lines generated by the function before they are inserted
        # into the intData class variable

        incData = []
        rowData = []

        for i in self.generateReportingDates():
            for j in range(12):  # inserting income lines every month
                for inc in range(self.getIncLinesMonth()):
                    period = i[j]
                    incType = choice(self.incomeType)
                    row = (
                        period
                        + "\t"
                        + self.infoType
                        + "\t"
                        + "Income"
                        + "\t"
                        + incType
                        + "\t"
                        + self.costCentre[0]
                        + "\t"
                        + incType
                        + " "
                        + "monthly transactions"
                        + "\t"
                        + str(-1 * (randint(1, 10000000) / 100))
                    )
                    rowData.append(row)

        del incData[::]
        incData += rowData

        # transferring data to the class storage
        self.intData += incData
        return None

    def generateExpData(self):
        print("Expenditure Lines: ", self.getNumYears() * 12 * self.getExpLinesMonth())
        print("----------------------")
        rowData = []
        for i in self.generateReportingDates():
            for j in range(12):
                for inc in range(self.getExpLinesMonth()):
                    period = i[j]

                    # to exclude salaries as they will be added separately
                    expType = choice(self.expenditureType)

                    while expType == "Salaries":
                        expType = choice(self.expenditureType)

                    # to generate a cost centre different than "Sales"
                    costCentre = choice(self.costCentre)

                    while costCentre == "Sales":
                        costCentre = choice(self.costCentre)

                    # preparing the data
                    row = (
                        period
                        + ","
                        + "Actual"
                        + ","
                        + "Expenses"
                        + ","
                        + expType
                        + ","
                        + costCentre
                        + ","
                        + expType
                        + "-"
                        + "monthly transactions"
                        + ","
                        + str(randint(1, 3000000) / 100)
                    )
                    rowData.append(row)

                    # row = []
                    # for ic in range(self.getExpLinesMonth()):
                    #     period = i[j]

                    # # to exclude salaries as they will be added separately
                    #     expType = "Salaries"

                    # # to generate a cost centre different than "Sales"
                    #     # costCentre = choice(self.costCentre)

                    #     # while costCentre == "Sales":
                    #     #     costCentre = choice(self.costCentre)

                    # # preparing the data
                    #     row = (
                    #         period
                    #         + "-"
                    #         + "Actual"
                    #         + "-"
                    #         + "Expenses"
                    #         + "-"
                    #         + expType
                    #         + "-"
                    #         + costCentre
                    #         + "-"
                    #         + expType
                    #         + "-"
                    #         + "monthly transactions"
                    #         + "-"
                    #         + str(5000)

        return rowData

    def createDataSet(self):
        # deleting any previous stored data
        del self.intData[::]

        if self.infoType == "Both":
            pass
            # # generating actual amounts
            # self.infoType = "Actual"
            # self.generateIncData()

            # # generating budget amounts
            # self.infoType = "Budget"
            # self.generateIncData()
            #
        else:
            self.generateIncData()

        return self.intData
        # return None


def main():
    print()


if __name__ == "__main__":
    main()
