#!usr/bin/env python3

# This part of the code will :
# it will generate a list of transactions (income and expenditure) based the input obtained from the user
# it will store the dataset


class Rules:
    def __init__(self):
        self.__setNoYears = int(input("How many years does the data need to reflect?"))
        self.__setIncLines = int(
            input("How many lines of income would you like to generate every month:")
        )

        self.__setExpLines = int(
            input(
                "How many lines of expenditure would you like to generate every month:"
            )
        )

    def getNumYears(self, years):
        return years

    def getNumIncEntries(self, years, lines):
        incLines = years * 12 * lines
        return incLines

    def getNumExpEntries(self, years, lines):
        expLines = years * 12 * lines
        return expLines


def main():
    newRules = Rules()

    # Generating the total number of income and expenditure lines The default
    # values of the parameters shown in the getNumIncEntries and the getNumExpEntries
    # refer to private variables initiated when the class Rules is instantiated

    totalNumYears = newRules.getNumYears(newRules._Rules__setNoYears)

    totalIncEntries = newRules.getNumIncEntries(
        years=newRules._Rules__setNoYears, lines=newRules._Rules__setIncLines
    )

    totalExpLines = newRules.getNumExpEntries(
        years=newRules._Rules__setNoYears, lines=newRules._Rules__setExpLines
    )
    # Testing, testing, testing
    print(totalNumYears)
    print(totalIncEntries)
    print(totalExpLines)


if __name__ == "__main__":
    main()
