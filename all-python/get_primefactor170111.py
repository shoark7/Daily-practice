"""
Get largest prime facotor of a given number.

Start Date : 2017/01/11
End Date   : 2017/01/11
"""

TEST_NUMBER = 600851475143


""" My one"""
def get_max_primefactor(number):

    prime_set = {}
    start_number = 2

    while start_number <= number:
        count = 0
        while number % start_number == 0:
            count += 1
            number //= start_number
        if count > 0:
            prime_set[start_number] = count
        start_number += 1

    return max(prime_set)


print(get_max_primefactor(TEST_NUMBER))



"""One user's one"""
n=600851475143;m=2
while m<n:
        if not n%m:n/=m
        m+=1
print(n)



"""Refactor this guy's code"""
n = 600851475143
m = 2

while m < n:
    if not n % m:
        n //= m
    m += 1
print(n)



"""
This guy's code is not good.
It looks simple in a glance but
when you put 27, the n is 9.
"""
