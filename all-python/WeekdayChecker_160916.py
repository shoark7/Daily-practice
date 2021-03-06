import sys
"""
This function is designed to calculate weekdays with given year, month, day.
No modules used but only the fact that 0001.01.01 AC is Monday.

Start date = 2016/09/16
End date = 2016/09/17

"""

def weekday_checker(year, month, day):
    """Tell which wekkday given date is."""
    # Tell if given year is a lunatic year or not
    def is_lunatic(year):
        if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            return True
        else:
            return False

    days_counter = 0
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    days_of_month = [31, 28, 31, 30, 31, 30,31,31,30, 31,30,31] # Jan to Feb
    if is_lunatic(year):
        days_of_month[1] = 29
    # If year is lunatic, days of Feb changes to 29.

    # Input type and value test.
    if any(map(lambda x: type(x) != type(int(3)), [year,month,day])):
        raise TypeError("Year, month and day only accepts integers.")
    elif year < 1:
        raise ValueError("Year must be over 0.")
    elif month < 1 or month > 12:
        raise ValueError("Month must be between 0 and 13.")
    elif day < 1 or day > days_of_month[month -1]:
        raise ValueError("Day must be between 0 and "+\
                         str(days_of_month[month -1] + 1 + (1 if is_lunatic(year) and month == 2 else 0)) +\
                         " with given month.")
        # This statement would be difficult. It considers lunatic years so day range would change.

    """
    Now we have to count days. If given date is 2004/03/02,
    1. we count year days from 1 to 2003
    2. we count month days from Jan to Feb(right before March
    3. we count given day - 1  because day of start date is 1.
    4. finally we get the remainder of days_counter divided by 7.
    5. We get the day.
    """

    # Year count. Non-lunatic year % 7 = 1, and lunatic year is 2. So we count 1 or 2 until the given year.
    for y in range(1, year):
        if is_lunatic(y):
            days_counter += 2
        else:
            days_counter += 1

    for m in range(month -1):
        days_counter += days_of_month[m]

    days_counter += (day - 1)
    # Until part 3 is done.

    days_counter %= 7
    return weekdays[days_counter]



# example
print(weekday_checker(2020,3,2))
print(weekday_checker(3000, 1, 1))

"""
comment : This works quite well. But I wonder if is too long although it contains some
comment code. Can it be shorter? Anyway input type and value test is satisfying.
And it goes my mind that lunatic year cycle is (1, 1, 1, 2). If I had grouped those and
calculated, year counting would have been more convenient.
"""

