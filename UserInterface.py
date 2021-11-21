#
# Abdurakhmon Abdulatipov
# 21 AUG 2021, CSC 256
# UI of Full Retirement Age Calculator
#

from RetirementCalculator import *


def main():
    while True:
        print("Social Security Full Retirement Age Calculator")
        birth_year = input("Enter the year of birth: ")
        if birth_year == '':
            break
        birth_month = int(input("Enter the month of birth: "))
        retirement_age, retirement_months, retirement_date = retirement_calculator(int(birth_year), birth_month)
        print(f"Your full retirement age is {retirement_age} and {retirement_months} months.")
        print(f"This will be in {retirement_date[0]} of {retirement_date[1]}")


main()
