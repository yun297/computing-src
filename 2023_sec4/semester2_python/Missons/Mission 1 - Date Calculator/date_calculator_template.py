#######################################
# Mission 1: Date Calculator Template #
#######################################

#############################
# Task 1 - Helper Functions #
#############################

###########
# Task 1a #
###########
def is_leap_year(year):
    """
    is_leap_year (year) -> boolean
    Function takes in a specific year.
    Returns True if it is a leap year, False otherwise.
    """
    ## Your Code Here ##

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


# print (is_leap_year(2000)) # True
# print (is_leap_year(1900)) # False
# print (is_leap_year(1984)) # True
# print (is_leap_year(2015)) # False

###########
# Task 1b #
###########


def days_in_month(month):
    """
    days_in_month (month) -> int
    Function takes in a specific month.
    Returns number of days in that month for a normal year.

    Note: This function needs not to consider leap year.
    """
    ## Your Code Here ##

    month_days = {
        1: 31,  # January
        2: 28,  # February
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31  # December
    }

    return month_days[month]


# Print out number of days in each month:
# for i in range (1, 13):
#     print (i, days_in_month(i))

###########
# Task 1c #
###########


def num_of_leap_years(start_year, end_year):
    """
    num_of_leap_years (start_year, end_year) -> int
    Function takes in 2 years: start_year (inclusive) and end_year (exclusive).
    Returns number of leap years in between the 2 years.
    """
    ## Define num_of_leap_years using iterative loop ##
    ## Your Code Here ##

    num_of_leap_years = 0
    for i in range(start_year, end_year):
        if is_leap_year(i):
            num_of_leap_years += 1

    return num_of_leap_years

# print (num_of_leap_years(2010, 2016)) # 1
# print (num_of_leap_years(2008, 2013)) # 2
# print (num_of_leap_years(1900, 2016)) # 28

###########
# Task 1d #
###########


def is_valid_date(date):
    """
    is_valid_date (date) -> boolean
    Function checks if the date entered is a valid date.
    Returns True if it's valid, False otherwise.
    """
    ## Your Code Here ##

    # Check if date is 8 digits
    if len(date) != 8:
        return False

    # print("Passed 8 digits")

    # Split date into day, month, year
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:8])

    # print(day, month, year)

    # Check if month is valid
    if month < 1 or month > 12:
        return False

    # print("Passed month")
    
    # Check for leap year
    if is_leap_year(year) and month == 2:
        if day < 1 or day > 29:
            return False
        
    # Check if day is valid
    elif day < 1 or day > days_in_month(month):
        return False
    
    return True


# print(is_valid_date("29022016"))  # True
# print(is_valid_date("31042015"))  # False
# print(is_valid_date("29022015"))  # False

###########################
# Task 2 - Main Functions #
###########################

###########
# Task 2a #
###########


def num_of_days_from_1900(date):
    """
    num_of_days_from_1900 (date) -> int
    Function takes in a date.
    Returns the number of days of the input date after "01011900".
    """
    ## Your Code Here ##
    
    days = 0
    
    for i in range(1900, int(date[4:8])):
        if is_leap_year(i):
            days += 366
        else:
            days += 365
    
    for i in range(1, int(date[2:4])):
        if i == 2 and is_leap_year(int(date[4:8])):
            days += 29
        else:
            days += days_in_month(i)
        
    days += int(date[0:2]) - 1
    
    return days

# print (num_of_days_from_1900("30011900")) # 29
# print (num_of_days_from_1900("28021900")) # 58
# print (num_of_days_from_1900("01031904")) # 1520
# print (num_of_days_from_1900("31012016")) # 42398

# Peronsal test cases
# print (num_of_days_from_1900("01011900")) # 0
# print (num_of_days_from_1900("01012000")) # 36524

###########
# Task 2b #
###########


def days_between_2_dates(date1, date2):
    """
    days_between_2_dates (date1, date2) -> int
    Function takes in 2 dates.
    Returns the number of days in between the 2 dates.
    """
    ## Your Code Here ##
    
    if num_of_days_from_1900(date1) > num_of_days_from_1900(date2):
        temp = date1
        date1 = date2
        date2 = temp
    
    day1 = int(date1[:2])
    month1 = int(date1[2:4])
    year1 = int(date1[4:])
    
    day2 = int(date2[:2])
    month2 = int(date2[2:4])
    year2 = int(date2[4:])
    
    days = 0
    
    # Calculate days for years between year1 and year2
    for year in range(year1 + 1, year2):
        if is_leap_year(year):
            days += 366
        else:
            days += 365
    
    # Calculate days for remaining months in year1
    for month in range(month1, 13):
        if month == month1:
            if is_leap_year(year1) and month == 2:
                days += 29 - day1
            else:
                days += days_in_month(month) - day1
        else:
            if is_leap_year(year1) and month == 2:
                days += 29
            else:
                days += days_in_month(month)
    
    # Calculate days for remaining months in year2
    for month in range(1, month2):
        if month == 2 and is_leap_year(year2):
            days += 29
        else:
            days += days_in_month(month)
    
    # Add remaining days in year2
    days += day2
    
    return days

    
    return days

# print (days_between_2_dates("15041984", "26102000")) # 6038
# print (days_between_2_dates("26102000", "15041984")) # 6038
# print (days_between_2_dates("26102000", "31012016")) # 5575

###########
# Task 2c #
###########


def add_n_days_after_1900(days):
    """
    add_n_days_after_1900 (days) -> date
    Function takes in a specific number of days.
    Returns the date after adding the input number of days to "01011900".
    """
    ## Your Code Here ##
    
    # Base no. of days, months, years
    outputDay = 1
    outputMonth = 1
    outputYear = 1900
    
    while days > 0:
        days_in_outputMonth = days_in_month(outputMonth)
        
        # Account for leap year
        if outputMonth == 2 and is_leap_year(outputYear):
            days_in_outputMonth += 1

        if outputDay + days > days_in_outputMonth:
            days -= (days_in_outputMonth - outputDay + 1)
            outputDay = 1
            outputMonth += 1

            if outputMonth > 12:
                outputMonth = 1
                outputYear += 1
        else:
            outputDay += days
            days = 0
    
    date = str(outputDay).zfill(2) + str(outputMonth).zfill(2) + str(outputYear)
    return date

# print (add_n_days_after_1900(30)) # "31011900"
# print (add_n_days_after_1900(31)) # "01021900"
# print (add_n_days_after_1900(59)) # "01031900"
# print (add_n_days_after_1900(1519)) # "29021904"
# print (add_n_days_after_1900(1520)) # "01031904"

###########
# Task 2d #
###########


def add_n_days_from_a_date(date, days):
    """
    add_n_days_from_a_date (date, days) -> date
    Function takes in a date and a specific number of days.
    Returns the date after adding the input number of days to the input date.
    """
    ## Your Code Here ##
    
    outputDay = int(date[:2])
    outputMonth = int(date[2:4])
    outputYear = int(date[4:])
    
    while days > 0:
        days_in_outputMonth = days_in_month(outputMonth)
        
        # Account for leap year
        if outputMonth == 2 and is_leap_year(outputYear):
            days_in_outputMonth += 1

        if outputDay + days > days_in_outputMonth:
            days -= (days_in_outputMonth - outputDay + 1)
            outputDay = 1
            outputMonth += 1

            if outputMonth > 12:
                outputMonth = 1
                outputYear += 1
        else:
            outputDay += days
            days = 0
    
    date = str(outputDay).zfill(2) + str(outputMonth).zfill(2) + str(outputYear)
    return date

# print (add_n_days_from_a_date ("15041984", 6038)) # 26102000
# print (add_n_days_from_a_date ("26102000", 6038)) # 08052017

###########
# Task 2e #
###########


def weekday_of_date(date):
    """
    weekday_of_date (date) -> str
    Function takes in a date.
    Returns the weekday of the input date.
    """
    ## Your Code Here ##
    
    days = num_of_days_from_1900(date)
    # 1st Jan 1900 is a Monday
    
    daysOfTheWeek = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    return daysOfTheWeek[(days % 7) + 1]

# print (weekday_of_date("01011900")) # "Monday"
# print (weekday_of_date("02011900")) # "Tuesday"
# print (weekday_of_date("31012016")) # "Sunday"

############################
# Task 3 - Date Calculator #
############################


def date_calculator():
    """
    date_calculator ()
    Function takes in an input from user and performs the functions accordingly.
    """
    done = False
    while not done:
        # Prepare Menu
        print("-----------------------------------------")
        print("Welcome to date calculator")
        print("  1. Calculate number of days between 2 dates.")
        print("  2. Add n days from a date.")
        print("  3. Find weekday of a date.")
        print("  4. Exit the programme.\n")
        print("**Please note the format of date should follow the format of 'DDMMYYYY'\n")

        # Get Input
        option = int(input("Select a function: "))

        ## Your Code Here ##
        if option == 1:
            print("-----------------------------------------")
            date1 = input("Enter date 1: ")
            date2 = input("Enter date 2: ")
            print(days_between_2_dates(date1, date2))
        elif option == 2:
            print("-----------------------------------------")
            date = input("Enter date: ")
            days = int(input("Enter number of days: "))
            print(add_n_days_from_a_date(date, days))
        elif option == 3:
            print("-----------------------------------------")
            date = input("Enter date: (Date cannot be before 01011900)")
            print(weekday_of_date(date))
        elif option == 4:
            print("-----------------------------------------")
            print("Thank you for using date calculator, terminating program...")
            exit()

date_calculator()