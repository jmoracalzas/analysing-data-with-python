#!usr/bin/env python3
import customDataGenClasses as customClasses

# This part of the code will :
# it will generate a list of transactions (income and expenditure) based the input obtained from the user
# it will store the dataset


def main():
    newRules = customClasses.Rules()

    # Generating the total number of income and expenditure lines
    totalIncEntries = newRules.getNumIncEntries(
        years=newRules.setNoYears, lines=newRules.setIncLines
    )

    totalExpLines = newRules.getNumExpEntries(
        years=newRules.setNoYears, lines=newRules.setExpLines
    )


if __name__ == "__main__":
    main()
