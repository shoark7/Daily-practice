"""Convert decimal number to another radix notation.

You can choose which radix to use.
Default is 10.

And you can choose return's length.
But it's not mandatory but just strongly recommended.
For example, if answer is '333333' and length is 3,
length is too short. So length is ignored.
"""


def to_radix_notation(number, radix=2, length=None):
    """Convert decimal number to another radix notation's format.

    :input:
        number: Target number to be changed. Must be an integer.
        radix: Wanted radix. Default is 2 and should be over 1.
        length: Recommend length of the output. May be ignored if too short.
                Default is None. Should be an integer also.
    :return:
        Number of target radix notatinon.
        String format.
    """

    # Input validation
    if not isinstance(number, int):
        raise TypeError("Target number must be an integer")
    elif not isinstance(radix, int) or radix <= 1:
        raise TypeError("Radix must be an integer and equals to and greater than 2")
    elif length and not isinstance(length, int):
        raise TypeError("Length of changed number must be an integer")

    answer = ''

    # Main algorithm part
    while(number >= radix):
        number, left = divmod(number, radix)
        answer = str(left) + answer
    answer = str(number) + answer

    if length:
        answer = int(answer)
        # you have to change answer to integer because of string format specifier.
        # '{:10}'.format(33) is '33        ', left justified.
        # There is no space to fill zeros up.
        # Do you follow me?
        answer = '{:0{}}'.format(answer, length)

    return answer
