"""
DO you know the powre of string format?
There are so many ones, like ' {:,}.format(100000000) '
I like this function very much. We implement this function from scratch.

Start date = 2016/10/07
End date = 2016/10/07
"""

def number_separator(num, sep=','):
    """Add separators into number."""
    if not str(num).isnumeric():
        raise TypeError("Only integer-format is allowed.")
    else:
        num = int(num)

    dividen_list = []
    while num >= 1000:
        dividen_list.insert(0, str(num)[-3:])
        num //= 1000
    dividen_list.insert(0, str(num))
    return ','.join(dividen_list)

print(number_separator(123456789))
print(number_separator(1932087419028734012837))