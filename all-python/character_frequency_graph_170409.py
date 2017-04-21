"""Draw a English alphabet frequency histogram.

In January 2016, I studied Java for a month.
There was an challenging assignment to draw a graph with given sting.
I remembered that qustion today, so I rewrote it in Python.
I hope it would be much better than before.


Start date: 2017/04/09
End date  : 2017/04/09
"""


from collections import defaultdict
import math
import string
import sys
import os


def freq_histogram(file_or_string):
    """
    Draw a histogram with a fie name or a string.

    :input:
        file_or_string:
            If it is a file, read it and use it.
            If it is a string, use it as it is.
    :return:
        histogram string:
            You have to print it to make it look nice.
            Each character is a part of a graph including a new line.
    """

    if os.path.exists(file_or_string):
        if os.path.isfile(file_or_string):
            with open(file_or_string) as fp:
                string_stream = fp.read()
        else:
            raise OSError("Given path is a directory, not a file.")
    else:
        string_stream = file_or_string

    string_stream = string_stream.upper()
    char_dict = defaultdict(int)
    char_order = list(string.ascii_uppercase)
    char_order.append('..')

    for c in string_stream:
        if c in string.ascii_uppercase:
            char_dict[c] += 1
        elif c in string.whitespace:
            pass
        else:
            char_dict['..'] += 1

    max_freq = max(char_dict.values())
    max_digit = math.floor(math.log(max_freq, 10)) + 1
    height = max_freq + 2
    width = len(char_order) + 1
    histogram = [['{char:^{digit}s}'.format(char=' ', digit=max_digit) for _ in range(width)]
                 for _ in range(height)]

    for i, c in enumerate(char_order, 1):
        histogram[height-1][i] = '{char:^{digit}s}'.format(char=c, digit=max_digit)

        for j in range(char_dict[c]):
            histogram[height-1-1-j][i] = '{char:^{digit}s}'.format(char='|', digit=max_digit)

    for n in range(0, height, 10):
        histogram[height-1-n][0] = '{char:^{digit}s}'.format(char=str(n), digit=max_digit)

    histogram = '\n'.join(''.join(row) for row in histogram)

    return histogram


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(freq_histogram(sys.argv[1]))
    else:
        lamb = """Merry had a little lamb, little lamb, little lamb.
        Merry had a little lamb, and its name was horse of white now~."""
        print(freq_histogram(lamb))


"""Result

                        |
  |                     |
10|                     |               |
  |       |             |               |
  |       |             |               |
  |       |             | |             |
  |       |       |     | |             |             |
  |       |       |     | |         |   |             |
  | |     |     | |     | |         |   |             |
  | |   | |     | |     | | | |     | | |     |       |
  | |   | |     | |     | | | |     | | |     |   |   |
  | |   | | |   | |     | | | |     | | |     |   |   |
0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ..
"""
