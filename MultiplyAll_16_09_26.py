"""
This file will have multiple ways for a single result.
Function it has is that it multiplies all numbers inside digit by digit.
It has to contain only numbers.

ex) '12312' --> 12
    'm123'  --> x
    'asdzx' --> x

There will be 3 ways for this.
1. for
2. eval
3. reduce.

Let's go.
Start date = 2016/09/26
End date = 2016/09/26
"""

from functools import reduce

def multipy_allr(n):
    if not str(n).isnumeric():
        raise TypeError('Only numbers are allowed here.')
    # if n contains any non-numeric values, raise an error.`

    elif '0' in str(n):
        return 0
    # elif n contains '0', result is always 0

    else:
         # 1. for
        result_for = 1
        for i in str(n):
            result_for *= int(i)
        return result_for

        # 2. eval
        result_eval = eval('*'.join(str(n)))
        return result_eval
        #strings are iterables so they can be joined, so join the numeric string with '*'.
        # And then eval the expression so the answer comes out.

        # 3. reduce
        result_reduce = reduce(lambda x, y: str(int(x)*int(y)), str(n))
        return result_reduce
        # Using reduce is useful. Number itself is not iterable so input must be strified.


"""
Doing something has several answers many times.
So we should think and think to find out more ways and which is better among them.
"""

print(multipy_allr('123'))
