#!/user/bin/env python3


class Rules:

    # To store the initial parameters set by the user
    def __init__(self):
        self.setNoYears = int(input("How many years does the data need to reflect?"))

        self.setIncLines = int(
            input("How many lines of income would you like to generate every month:")
        )

        self.setExpLines = int(
            input(
                "How many lines of expenditure would you like to generate every month:"
            )
        )

    def getNumYears(self, years):
        return years

    def getNumIncEntries(self, years, lines):  # total number of income lines
        incLines = years * 12 * lines
        return incLines

    def getNumExpEntries(self, years, lines):  # total number of expenditure lines
        expLines = years * 12 * lines
        return expLines


def main():
    print()


if __name__ == "__main__":
    main()
