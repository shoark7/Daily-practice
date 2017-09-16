"""Change excel column's name to integer and vice versa.

You know Microsoft's excel. It's an awesome problem of the earth.
No one denies it. You would also know that excel's columns have names, only alphabet letters.

You might want to know the number of column names and vice versa.
This problem exactly does what you want to.

Let's get it on.


Start Date : 2017/09/16
End Date   : 2017/09/16
"""
import re
from string import ascii_uppercase as upper_letters


def _parse_token(text, src_type='name'):
    """Parse given a token to an alphabet letter or an integer.

    You know I like input validation on every method and function I make.
    This function is a helper function for that. 
    I have 2 main jobs:
        1. alphabet -> column number
        2. column number -> alphabet

    Case 1. Strip text and check it if is a valid column name. src_type is 'name'. DEFAULT
    Case 2. check if it is a valid integer type. src_type is 'number'

    :input:
        text: A token. English letters or an integer.
    :return:
        A valid column number to use if src_type is default value. or
        a valid column name if src_type is 'number'.
    """
    text = str(text)

    if src_type == 'name':
        text = text.strip().lower()
        if re.search('[^a-z]', text):
            raise ValueError("Excel column names don't contain any non-alphabetic values")
        return text
    elif src_type == 'number':
        if re.search('[^0-9]', text):
            raise ValueError("Target column number must contain only numeric values")
        return int(text)


def name_to_integer(name):
    """Change an Excel column name to an integer

    With this function you can know number of the column.
    Type checking is done in advance.
    """
    name = _parse_token(name)
    result = 0
    digit = 0

    for n in name[::-1]:
        result += 26 ** digit * upper_letters.find(n)
        digit += 1

    return result


def integer_to_name(number):
    """Change an integer to a valid Excel column name.

    With this function you can know name of the column.
    Type checking is done in advance.
    """
    number = _parse_token(number, src_type='number')
    result = ''

    while number >= 26:
        number, left = divmod(number, 26)
        result = upper_letters[left] + result

    result = upper_letters[number] + result

    return result
