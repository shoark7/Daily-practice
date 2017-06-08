"""Get all number of possible coin cases.

This is an other version of "coin change" algorithm here.
Previous ones only get least number of coins it can make,
but now I get all coin changes as many as possible.

For example, change is 10, and coin set is (1, 2, 5)
    answer is..
        1,1,1,1,1,1,1,1,1,1
        1,1,1,1,1,1,1,1,2
        1,1,1,1,1,1,2,2
        1,1,1,1,2,2,2
        1,1,2,2,2,2
        2,2,2,2,2
        5,1,1,1,1,1
        5,1,1,1,2
        5,1,2,2
        5,5
    "10"

Start date : 2017/05/19
End date   : 2017/05/19
"""

# my sucking version
## Took 6688 ms in baekjoon online judge
def coin_change_max_noc(change, coin_units):
    """Get all number of possible coin cases.

    Get number of all cases to make the given change.

    :input:
        change: An integer over 0
    :coin_units:
        An iterable containing only integers over 0.
    """
    coin_units.sort(reverse=True)
    cache = [[0 for _ in range(change+1)] for _ in coin_units]

    for i, unit in enumerate(coin_units):
        for j in range(1, change + 1):
            if i == 0:
                if j % unit == 0:
                    cache[i][j] = 1
            else:
                count = 1
                cache[i][j] = cache[i-1][j]
                while j - count * unit >= 0:
                    cache[i][j] += cache[i-1][j-count*unit]
                    count += 1
    answer = cache[len(coin_units)-1][change]
    del(cache)
    return answer


# insung151's awesome code
## Took 92 ms in baekjoon online judge
def coin_change_max_noc_insung_ver(change, coin_uni0ts):
    cache = [0 for _ in range(change+1)]
    cache[0] = 1

    for unit in coin_units:
        for j in range(1, change+1):
            cache[j] += cache[j-unit]

    return cache[change]


"""
With comparing mine to insung152, I could know that mine sucks too much.
His' is much shorter and takes much less time.
More importantly, mine is difficult to understnad...
WTF... 
"""
