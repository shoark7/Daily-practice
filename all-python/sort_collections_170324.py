"""Sort algorithm collections in Python.

I'm writing a sort algorithm file in C for my assignment.
This time, I write those algorithms in Python again.
This file contains many kinds of sort algorithms like below:

    "selection", "bubble", "insertion", "shell", "merge", "quick"

If you want to master sort algorithm and your most familiar language is Python,
I think this might help you. Thanks a lot.

Start date : 2017/03/24
End date   : 2017/03/27
"""


import random  # For random test code


# Selection Sort
def selection_sort(target_list):
    """Selection sort."""
    length = len(target_list)

    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if target_list[index] > target_list[j]:
                index = j
        target_list[i], target_list[index] = target_list[index], target_list[i]

    return target_list


# Bubble Sort
def bubble_sort(target_list):
    """Bubble sort."""
    length = len(target_list)

    for i in range(length - 1, 0, -1):  # This code needs to be understood.
        for j in range(0, i):           # This too.
            changed = False

            if target_list[j] > target_list[j + 1]:
                target_list[j + 1], target_list[j] = target_list[j], target_list[j + 1]
                changed = True
        if not changed:
            break

    return target_list


# Insertion Sort
def insertion_sort(target_list):
    """Insertion sort."""
    length = len(target_list)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if target_list[j] < target_list[j - 1]:
                target_list[j], target_list[j - 1] = target_list[j - 1], target_list[j]
            else:
                break
    return target_list


# Shell Sort
# 1. Helper for shell Sort
def helper_insertion(target_list, start, last, h):
    """Helper function for shell sort.
    h means 'interval' This algorithm executes insertion sort with given h.
    """
    for i in range(start + h, last + 1, h):
        for j in range(i, start, -h):
            if target_list[j] < target_list[j - h]:
                target_list[j], target_list[j - h] = target_list[j - h], target_list[j]
            else:
                break


# 2. shell sort implementation
def shell_sort(target_list):
    """Shell sort algorithm using help_insertion function."""
    length = len(target_list)
    h = length // 2

    while h >= 1:
        for i in range(h):
            helper_insertion(target_list, i, length - 1, h)

        h //= 2

    return target_list


# Merge sort
def merge_sort(t_list):
    """Merge sort algorithm.

    This sort uses 2 helper functions: divide, merge
    Docs for each function can be checked below.
    """
    def divide(tt_list, start, end):
        """Divde target list into 2 parts."""
        if start >= end:
            return

        mid = (start + end) // 2

        divide(tt_list, start, mid)
        divide(tt_list, mid + 1, end)
        merge(tt_list, start, mid, end)

    def merge(tt_list, start, mid, end):
        """Merge devided target lists into completely sorted one."""
        length = end - start + 1
        temp_list = [0 for _ in range(length)]
        temp_index = 0
        left = start
        right = mid + 1

        while left <= mid and right <= end:
            if tt_list[left] > tt_list[right]:
                temp_list[temp_index] = tt_list[right]
                temp_index += 1
                right += 1
            else:
                temp_list[temp_index] = tt_list[left]
                temp_index += 1
                left += 1

        while left <= mid:
            temp_list[temp_index] = tt_list[left]
            temp_index += 1
            left += 1

        while right <= end:
            temp_list[temp_index] = tt_list[right]
            temp_index += 1
            right += 1

        tt_list[start:end+1] = temp_list[0:length]

    divide(t_list, 0, len(t_list) - 1)


# Quick sort
def quick_sort(t_list):
    """Quick sort algorithm."""
    def get_pivot(tt_list, start, end):
        """Get pivot with given list, start and end point."""
        if start < 0 or end >= len(tt_list):
            raise IndexError("Index rule must be obeyed.")

        pivot = start
        left = start
        right = end

        while left < right:

            while tt_list[pivot] >= tt_list[left] and left < end:
                left += 1

            while tt_list[pivot] < tt_list[right]:
                right -= 1

            if left < right:
                tt_list[left], tt_list[right] = tt_list[right], tt_list[left]

        tt_list[pivot], tt_list[right] = tt_list[right], tt_list[pivot]

        return right

    def sort(tt_list, start, end):
        """Real sort part with get_pivot function."""
        if start < 0 or end >= len(t_list):
            raise IndexError("Index rule must be obeyed.")
        elif start < end:
            pivot = get_pivot(tt_list, start, end)
            sort(tt_list, start, pivot - 1)
            sort(tt_list, pivot + 1, end)
        else:
            return

    sort(t_list, 0, len(t_list) - 1)

    return t_list


if __name__ == '__main__':
    test_list = [random.randint(1, 100) for _ in range(20)]
    print("Before sort : ", test_list)
    quick_sort(test_list)
    print("After  sort : ", test_list)
