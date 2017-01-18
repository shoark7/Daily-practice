"""
Implement combination with generation.

It's from http://codepractice.tistory.com/61

Start date : 2017/01/18
End date   : 2017/01/18
"""


def combination(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield elements[i]
        else:
            for next in combination(elements[i+1:len(elements)], length-1):
                yield elements[i] + next


"""
This code is very good, but it has some problems.

    1. Only adaptable to string-contains-iterables.
        - It is appended with + operator.
    2. It can't be use number character over than 9.
        - When it is 10, 11, 12, one of combinations is '101112'.
        - It's not what I want..
"""
