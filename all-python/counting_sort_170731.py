"""Cumulative counting sort algorithm implemenation in Python.

    I learned a new impressive sorting algorithm, counting sort.
    This sort algorithm is useful for an array with a min, max value.

    Cons of this algorithm is that if outlier value exists,
    too much memory is wasted.

    But I think with Python's dict, it can be much better as to memory space.
    I use a cumulative way. Let's go!


    Start Date : 2017/07/31
    End Date   : 2017/07/31
"""


def count_sort(arr, descending=False):
    """Count sort algorithm in Python

    This version can control any numeric values in arr.
    But values otherwise cannot be sorted. It would raise TypeError.

    This version also uses dict to minimize memory usage whih is often criticized for
    counting sort.
    Also like Python sorted function, descending direction can be assigned.

    NOTICE : ORIGINAL arr is not changed. So you have to assign the result to any variable.


    :input:
        arr: Numeric iterable
        descending: Whether sorting direction is reverse or not. Default: False
    :return:
        Numeric array. Return value is always list type no matter what it was given.
        ORIGINAL arr is not changed. You can say,
        This function works like sorted(), not list's sort().
    """

    arr = list(arr)  # Change to list for the case arr is iterator or something.
    length = len(arr)
    return_arr = [None for _ in range(length)]
    unique_arr = sorted(list(set(arr)), reverse=descending)  # Value set of arr
    counting_dict = {n: 0 for n in unique_arr}
    cum_sum_arr = [0 for _ in range(len(unique_arr))]  # Cumulative sum array for sort

    for n in arr:
        counting_dict[n] += 1

    for i, n in enumerate(unique_arr):
        cum_sum_arr[i] = cum_sum_arr[i-1] + counting_dict[n]

    for n in arr[::-1]:
        i = unique_arr.index(n)
        cum_sum_arr[i] -= 1
        index = cum_sum_arr[i]  # We have to use subtracted i by 1 because list starts at 0! Basic.
        return_arr[index] = n

    return return_arr


# Test code
if __name__ == '__main__':
    import random

    test_set = [random.randint(1, 100) for _ in range(100)]
    print("Before: ", test_set, sep='')
    test_set = count_sort(test_set)
    print("After : ", test_set, sep='')
