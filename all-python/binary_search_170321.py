"""Binary search function for list or tuple.

Start date : 17/03/21
End date   : 17/03/21
"""

from random import randint


def _binary_search(iterable, value, start, end):
    """Binary search function.
    Return the position of value in the iterable.
    It not found, return -1.
    :input:
        iterable: List or tuple.
        value: Value you're looking for.
        start: Start position of iterable.
        end: End position of iterable.
    :return:
        index: If value is found.
        -1   : If not.
    """

    iterable.sort()

    if not (iterable[start] <= value <= iterable[end]):
        return -1

    if start > end:
        return -1

    mid = (start + end) // 2

    if iterable[mid] > value:
        return binary_search(iterable, value, start,  mid - 1)
    elif iterable[mid] == value:
        return mid
    else:
        return binary_search(iterable, value, mid + 1, end)


"""
Well, it works anyway. But how about its pragmaticity?
It's not that good because when you have to use it,
you have to insert its start index 0 and last index of your wanted iterable.

So we fix it.
"""


def binary_search(iterable, value):

    iterable.sort()

    if not (iterable[0] <= value <= iterable[len(iterable) - 1]):
        return -1

    def recursive_search(iterable, value, start, end):

        if start > end:
            return -1

        mid = (start + end) // 2

        if iterable[mid] > value:
            return recursive_search(iterable, value, start, mid - 1)
        elif iterable[mid] == value:
            return mid
        else:
            return recursive_search(iterable, value, mid + 1, end)

    index = recursive_search(iterable, value, 0, len(iterable) - 1)

    return index


# Test code

random_numbers = [randint(1, 1000) for _ in range(1000)]
binary_search(random_numbers, 300)
