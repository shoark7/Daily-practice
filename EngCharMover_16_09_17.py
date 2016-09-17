import string
"""
This function is for changing every english character in a english sentence with given number.
if n == 1
'a' -> 'b'
'c' -> 'd'
'this' -> 'uijt'

n is integer and can be lower than 0.

Start date = 2016/09/17
End date = 2016/09/17

"""

# input argument type and value test.
def english_mover(text, n = 1):
    """It moves every english character unicode order with a given number."""
    if isinstance(text, str):
        pass
    elif isinstance(text, int):
        text = str(text)
    else:
        raise TypeError("First argument must be string.")

    if not isinstance(n, int):
        raise ValueError("Second argument must be a integer.")

    # lower = string.ascii_lowercase
    # upper = string.ascii_uppercase
    number = n % 26
    result = ''

    for c in text:
        if c.islower():
            result += chr(ord('a') + ( ord(c) - ord('a') + number) % 26)
        elif c.isupper():
            result += chr(ord('A') + ( ord(c) - ord('A') + number) % 26)
        else:
            result += c

    return result

#example
print(english_mover("I have my own dinner and it's lonely", 2))
print(english_mover("I don't know why, people believe in buddhism", 1000))


"""
In a sentence if a character is a english character, we move a character's order with a given number.
It's not that hard. But I wonder if the chaning process could be more simpler than mine.
"""
