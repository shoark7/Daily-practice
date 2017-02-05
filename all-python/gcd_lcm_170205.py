"""GCD means 'Greatest Common Divisor' and
LCM means 'Least Common Multiplier'.

First, I show you my bad code.
Second, I show you best code practice by others.

Start date : 2017/02/05
End date   : 2017/02/05
"""

# my code

def gcd_myway(a, b):
    a, b = (int(i) for i in input().split())
    gcd = 1
    for i in range(2, min(a, b) + 1):
        while a % i == 0 and b % i == 0:
            gcd *= i
            a //= i
            b //= i
    return gcd

def lcm_myway(a, b):
    return a * b // gcd_myway(a, b)


"""
This code sucks... It divdes very many times...
"""


# other guy's code

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // lcm(gcd)
