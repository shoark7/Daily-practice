"""
This file is also about divisors. Say, you get a natural number, N
N has many divisors, right? You have to make result as " a string of 1-digit divisors."

candidates for f(12) can be
26, 223, 112 and 62. You can see that product of strings is always 12.
But we want smallest one, 26.
Let's go

Start date = 2016/09/29
End date = 2016/09/29
"""

def get_divisors(n):
    result_list = []
    divisor = 9
    # divisor starts from 9 because we want '26' instead of '223'. If you start from small, result will be too long.

    while True:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count >= 1:
            result_list.append((divisor, count))
        if n == 1:
            break
        divisor -= 1
        if divisor <= 1 and n >2:
            return -1

    result_list.sort(key=lambda x: x[0])
    """
    # result_list would be like this : [(5,2), (7,2)].
    1. we concatenate divisor for count times tuple by tuple and make it a string.
    2. Next, we concatenate strings. Results are below. And make it int again. ↓↓↓↓
    """
    return int(''.join([''.join([str(divisor) for n in range(count)]) for divisor, count in result_list]))


print(get_divisors(19))
print(get_divisors(450))
