def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Get user input
year = int(input("Please input a year: "))

# Check and print result
if is_leap_year(year):
    print("That's a leap year!")
else:
    print("That's not a leap year.")