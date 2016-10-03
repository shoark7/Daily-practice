"""
We have dynamic programming. It's solving a problem by dividing it into smaller ones.
The most common technique is memoization. It's not memorization.
We record the results and next time we just index to it.
By using a decorator, we figure out how to solve fibonacci.
"""

# We make a memoization decorator
def memoization(func):
    __cache = {}  # make a cache to store the data
    return lambda *args: __cache[args] if args in __cache \
        else __cache.update({args:func(*args)}) or __cache[args]

@memoization
def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)

print(fibo(100))
print(fibo(200))

"""
YOu have to remember a few things to know the memoization.
1. Update method in Dictionary. It returns None and update dict.
2. or operator. Cause udpate returns None, expression follwing or is executed.
3. Packing and unpacking. You should be able to tell the difference between starred variable and not.
"""