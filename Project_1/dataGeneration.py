#!usr/bin/env python3

#This part of the code will :
    #Ask the user the number of year to generate transactions for
    #I will calculate the total number of transactions for income and expenditure
    #it will generate a list of transactions (income and expenditure) based the input obtained from the user
    #it will store the dataset

from datetime import date

class Rules:
    def __init__(self):
        self.__noYears = int(input("How many years does the data need to reflect?"))
        self.__expLines = int(input("How many lines of expenditure would you like to generate every month:"))
        self.__incLines =  int(input("How many lines of income would you like to generate every month:"))

def main():
    #thisDay = date.today()
    #currentYear = thisDay.year
    
    values = Rules()
    print(values)

if __name__=="__main__":    main()
