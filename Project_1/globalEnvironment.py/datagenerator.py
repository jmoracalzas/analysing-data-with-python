#!usr/bin/env python3

#This part of the code will :
    #Ask the user to input some parameters
    #Set variables to define how the data will be generated

from datetime import date

def main():
    thisDay = date.today()
    currentYear = thisDay.year
    
    #Storing the number of transactions
    noYears = int(input("How many years does the data need to reflect?"))
    expTrans = int(input("How many lines of expenditure would you like to generate every month:"))
    incTrans = int(input("How many lines of income would you like to generate every month:"))

    print(currentYear)
    print(noYears)
    print(expTrans)
    print(incTrans)

if __name__=="__main__":    main()
