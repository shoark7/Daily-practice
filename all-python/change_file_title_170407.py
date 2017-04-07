"""Change title of the file of this repository.

First of all, this is very dedicated only to me, Not appliable to others.
Now I need to unify the title format of files in this repository, 'daily practice'.
In this repository, there are many files written in Python, such as..

'huffman_compression_170406.py',   1.
'thread_inpython161225.py',        2.
'WeekdayChecker_16_09_16.py',      3.

First part of the title is the main theme of the file.
Second is its date.

But you can see that date parts are slightly different in all files.
It's because I didn't make specific rule for this.
Now I'll make it right.

The most desirable format now is 'title_of_file_170303.py'.
So format 2 and 3 above is not correct.
I fix this with os and re module


Start date : 2017/04/07
End date   : 2017/04/07
"""


import os
import re


RIGHT_FORMAT = r'(?P<title>\w+)_(?P<year>\d{2})(?P<month>\d{2})(?P<day>\d{2})\.py'
WRONG_FORMAT_1 = r'(?P<title>\w+)_(?P<year>\d{2})_(?P<month>\d{2})_(?P<day>\d{2})\.py'
WRONG_FORMAT_2 = r'(?P<title>\w+[^_])(?P<year>\d{2})(?P<month>\d{2})(?P<day>\d{2})\.py'

file_list = os.listdir('./')

for title in file_list:
    if re.match(WRONG_FORMAT_1, title) or re.match(WRONG_FORMAT_2, title):
        match = re.match(WRONG_FORMAT_1, title) or re.match(WRONG_FORMAT_2, title)
        title_part, year, month, day = match.groups()
        to_be = '{title}_{year}{month}{day}.py'.format(
            title=title_part if title_part[-1] != '_' else title_part[:-1],
            year=year,
            month=month,
            day=day,
        )

        os.rename(title, to_be)
        print("'{}' is changed to '{}'".format(title, to_be))
    else:
        if re.match(RIGHT_FORMAT, title):
            pass
        else:
            print("'{}' is not the right type but not changed. Please check".format(title))
