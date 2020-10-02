#!/usr/bin/env python
from datetime import date, timedelta
from random import choice, randint


class Rules:

    # To store the initial parameters set by the user
    expenditureType = {
        # data structure--> type:[classification, %_sales,%_dist,%_prod,%_admin, max_cost]
        "Purchase of materials": ["variable", 0, 0, 100, 0],
        "Rent": ["fixed", 10, 10, 30, 50, 4750],
        "Electricity": ["variable", 15, 10, 50, 25],
        "Salaries": ["fixed", 15, 10, 5000, 2500, 6575],
        "Fuel": ["variable", 0, 55, 40, 5],
    }

    incomeType = ["Sale of products", "Rendering of services"]

    costCentre = [
        "Sales",
        "Distribution",
        "Production",
        "Administration",
    ]

    # used to determine the total number of lines to generate
    # and to hold the basic categories needed to generate data
    def __init__(self, years, incLines, expLines, infoType):
        self.__setNoYears = years
        self.__setIncLines = incLines
        self.__setExpLines = int(expLines)
        self.infoType = infoType
        self.startDate = date.today()
        self.__costCentre = self.costCentre
        self.__incList = self.incomeType
        self.__expDict = self.expenditureType

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

    def getCostCentres(self):
        return self.__costCentre

    def getIncList(self):
        return self.__incList

    def getExpList(self):
        return self.__expDict


class interimData(Rules):

    intData = []  # to hold the user's dataset

    def __init__(self, years, incLines, expLines, infoType):
        super().__init__(years, incLines, expLines, infoType)

    # calculates the no of income lines to generate and creates the income dataset
    def generateIncData(self):
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

    def generateVarExp(self):
        varExpData = []
        rowData = []

        # creating a list of variable expenditure
        varExpItems = list(
            filter(lambda elem: elem[1][0] == "variable", self.expenditureType.items(),)
        )

        for i in self.generateReportingDates():
            for j in range(12):
                for inc in range(self.getExpLinesMonth()):
                    period = i[j]

                    randomExpenditure = choice(varExpItems)
                    expType = str(randomExpenditure[0])

                    # to generate a cost centre different than "Sales"
                    costCentre = choice(self.costCentre)
                    while costCentre == "Sales":
                        costCentre = choice(self.costCentre)

                    # preparing the data
                    row = (
                        period
                        + "\t"
                        + self.infoType
                        + "\t"
                        + "Expenditure"
                        + "\t"
                        + expType
                        + "\t"
                        + costCentre
                        + "\t"
                        + expType
                        + " "
                        + "monthly transactions"
                        + "\t"
                        + str(randint(1, 3000000) / 100)
                    )
                    rowData.append(row)

        del varExpData[::]
        varExpData += rowData

        # transferring data to the class storage
        self.intData += varExpData
        return None

    def generateFixExp(self):

        fixedExpData = []
        rowData = []

        # to filter fixed expenditure
        fixedExpItems = list(
            filter(lambda elem: elem[1][0] == "fixed", self.expenditureType.items())
        )
        # print(fixedExpItems[0][0])

        for i in self.generateReportingDates():
            for j in range(12):
                for item in fixedExpItems:

                    period = i[j]

                    costCentre = "Administration"
                    expType = item[0]
                    amount = str(item[-1][-1])

                    # preparing the data
                    row = (
                        period
                        + "\t"
                        + self.infoType
                        + "\t"
                        + "Expenditure"
                        + "\t"
                        + expType
                        + "\t"
                        + costCentre
                        + "\t"
                        + expType
                        + " "
                        + "monthly transactions"
                        + "\t"
                        + amount
                    )
                    rowData.append(row)

        del fixedExpData[::]
        fixedExpData += rowData

        # transferring data to the class storage
        self.intData += fixedExpData

        return None

    def createDataSet(self):
        # deleting any previous stored data
        del self.intData[::]

        if self.infoType == "Both":

            # generating the actual amounts
            self.infoType = "Actual"
            self.appendData()

            # generating budget amounts
            self.infoType = "Budget"
            self.appendData()
        else:
            self.appendData()

        return self.intData

    # to append the lines at the same time
    def appendData(self):
        self.generateIncData()
        self.generateVarExp()
        self.generateFixExp()


def main():
    pass


if __name__ == "__main__":
    main()
