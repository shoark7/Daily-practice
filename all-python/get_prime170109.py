"""
with given number nth, we get the nth-th prime number.
I think this isn't that efficient.
But I upload this.


Start date : 2016/01/09
End date : 2016/01/10
"""

def is_prime(number):
    number = int(number)

    if number < 2:
        return False

    if number == 2 or number == 3:
        return True

    elif number % 2 == 0:
        return False

    else:
        for i in range(2, number // 3 + 1):
            if number % i == 0:
                return False
        return True

def nth_prime(nth):
    count = 0
    number = 1
    while True:
        if is_prime(number):
            count += 1
        if count == nth:
            break
        number += 1
    return number

print(nth_prime(10000))
