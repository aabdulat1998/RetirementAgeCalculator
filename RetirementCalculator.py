#
# Abdurakhmon Abdulatipov
# 21 Aug 2021
# This module is used to perform the calculations using the data provided by the UserInterface module
#

def month_calculator(birth_month, retirement_year):
    while birth_month > 12:
        birth_month -= 12
        retirement_year += 1

    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    return month_dict[birth_month], retirement_year


def retirement_calculator(birth_year, birth_month):
    if 1900 <= birth_year <= 1937:
        retirement_month, retirement_year = month_calculator(birth_month, birth_year + 65)
        return 65, 0, [retirement_month, retirement_year]
    elif birth_year == 1938:
        retirement_month, retirement_year = month_calculator(birth_month + 2, birth_year + 65)
        return 65, 2, [retirement_month, retirement_year]
    elif birth_year == 1939:
        retirement_month, retirement_year = month_calculator(birth_month + 4, birth_year + 65)
        return 65, 4, [retirement_month, retirement_year]
    elif birth_year == 1940:
        retirement_month, retirement_year = month_calculator(birth_month + 6, birth_year + 65)
        return 65, 6, [retirement_month, retirement_year]
    elif birth_year == 1941:
        retirement_month, retirement_year = month_calculator(birth_month + 8, birth_year + 65)
        return 65, 8, [retirement_month, retirement_year]
    elif birth_year == 1942:
        retirement_month, retirement_year = month_calculator(birth_month + 10, birth_year + 65)
        return 65, 10, [retirement_month, retirement_year]
    elif 1954 >= birth_year >= 1943:
        retirement_month, retirement_year = month_calculator(birth_month, birth_year + 66)
        return 66, 0, [retirement_month, retirement_year]
    elif birth_year == 1955:
        retirement_month, retirement_year = month_calculator(birth_month + 2, birth_year + 66)
        return 66, 2, [retirement_month, retirement_year]
    elif birth_year == 1956:
        retirement_month, retirement_year = month_calculator(birth_month + 4, birth_year + 66)
        return 66, 4, [retirement_month, retirement_year]
    elif birth_year == 1957:
        retirement_month, retirement_year = month_calculator(birth_month + 6, birth_year + 66)
        return 66, 6, [retirement_month, retirement_year]
    elif birth_year == 1958:
        retirement_month, retirement_year = month_calculator(birth_month + 8, birth_year + 66)
        return 66, 8, [retirement_month, retirement_year]
    elif birth_year == 1959:
        retirement_month, retirement_year = month_calculator(birth_month + 10, birth_year + 66)
        return 66, 10, [retirement_month, retirement_year]
    elif birth_year >= 1960:
        retirement_month, retirement_year = month_calculator(birth_month, birth_year + 67)
        return 67, 0, [retirement_month, retirement_year]
