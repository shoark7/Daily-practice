"""
Our plan now is to get a sum of divisors of a natural number, n.
For example , let's say n is 12.  12 = (2**2) * (3**1),
Formula to get a sum of divisors of 12 is (2**0 + 2**1 + 2**2) * (3**0 + 3**1) = 28.
Divisors of 12 is [1, 2, 3, 4, 6, 12, ], so the formula is right.
We realize this algorithm.

Start date = 2016/09/29
End date = 2016/09/29
"""


def sum_of_divisors(n):
    """input : natural number n. output : sum of divusors of n"""
    # 0. Type verification Test

    if str(n).isnumeric():
        if int(n) >= 2:
            n = int(n)
        else:
            raise ValueError("n should be over 1.")
    else:
        raise TypeError("Input should be a natural number.")

    # 1. Get the least divisors of n
    def get_min_divisor(n):
        divisor_count = []
        divisor = 2

        while True:
            count = 0
            while n % divisor == 0:
                count += 1
                n //= divisor
            if count >= 1:
                divisor_count.append((divisor, count))
            if n == 1: break
            divisor += 1

        return divisor_count

    # 2. Get sum of the list.
    count_tuple = get_min_divisor(n)

        # User list comprehension for bluff
    return eval('*'.join([str(sum([divisor ** c for c in range(count+1)])) for divisor, count in count_tuple]))


print(sum_of_divisors(12000))
print(sum_of_divisors(100000))

"""
Actually, just divising number by from 1 to number would be much more easier to implement.
But how about functionality issue? Is mine better or not?
If it's not better than the classic method, where has my time gone then? haha :)
"""
