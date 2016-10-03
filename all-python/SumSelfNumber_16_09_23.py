"""
There's a naturl number n, and d(n) is the sum of each digit in n and itself.
d(91) = 9 + 1 + 91 = 101
This time, 91 is generator of 101

And there are some numbers that don't have generators.(1, 3, 5, 7...)
They are called 'self numbers'.

Question is to get sum of self number between(1 <=    < 5000)

Start date = 2016/09/23
End date = 2016/09/23

"""

# Define a function.
# my version
def get_selfnumber(n):
    """Get sum of self numbers from 1 and to right before n"""
    def d(k):
        return k + eval('+'.join(list(str(k)))) # d 함수 구현 완료

    result = [i for i in range(n + 1)]
    for i in range(1, n):
        try:
            result[d(i)] = 0
        except IndexError:
            break
    return sum(result)

"""
Principle of my version:
Always, n < d(n).
So, I make a array between 0 and 5000.
And [n for n in 1 ~ 5000] time, I make d(n) 0, because d(n) has a generator.
And when time has come that d(n) gets out of index(5000), error occurs and function returns.
"""


# other person's version
sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)})

"""
This awesome code's principle is using the set's specialty. It's really beautiful...
"""

# my revision with 'eval'
print(sum(set(range(1, 5000)) - {i + eval('+'.join(list(str(i)))) for i in range(5000)}))
