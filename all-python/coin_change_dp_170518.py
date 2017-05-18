"""Get least number of coins for the given change.

It's been a long day, without you, my friend.
And I'll tell you all about it when I see you again.
We've come a long way, from where we began.

Hello, I'm pretty busy nowadays because of school work.
Forgive me, but please know that I'm not giving up Python.

This algorithm is to get least numbers of changes with Dynamic programming.
Let's get started.

Start date : 2017/05/18
End date   : 2017/05/18
"""

import math


def coin_change_dp(change, coin_units=[1, 10, 50, 100, 500]):
    """Get least number of coins for the given change.

    People generally want less coins for the change.
    This algorithm gets the least coins for the change with DP.
    Same algorithm with greedy method can lead to an wrong answer.
    But this does not.

    :input:
        change: Given change. Must be an positive interger.
        coin_units: Coin units to calculate. Default is Korean coin units.
                    Must be an iterable.
                    Also, elements must be an integer over 0.
    :return:
        Least number of coins.
        -1 if we cannot make a combination of coins with given units.
    """

    # Input validation
    ## 1. change
    if not isinstance(change, int) and change > 1:
        raise TypeError("Change should be a positive interger")
    ## 2. coin_units
    try:
        coin_units = list(coin_units)
        coin_units.sort(reverse=False)
    except:
        raise TypeError("coin_units should be an iterable")
    else:
        if not all(isinstance(x, int) and x > 0 for x in coin_units):
            raise TypeError("All coin units must be an integer over 0")

    cache = [math.inf for _ in range(change+1)]
    cache[0] = 0

    for i in range(1, change+1):
        number = math.inf
        for unit in coin_units:
            if i >= unit:
                number = min(number, cache[i-unit] + 1)
        cache[i] = number

    answer = cache[change]
    if answer == math.inf:
        return -1

    return answer
