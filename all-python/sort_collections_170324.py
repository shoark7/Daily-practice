"""Sort algorithm collections in Python.

I'm writing a sort algorithm file in C for my assignment.
This time, I write those algorithms in Python again.
This file contains many kinds of sort algorithms like below:

    "selection", "bubble", "insertion", "shell", "merge", "quick"

If you want to master sort algorithm and your most familiar language is Python,
I think this might help you. Thanks a lot.

Start date : 2017/03/24
End date   : 2017/????
"""

import random # For random test code


# Swap function for code
def swap(a, b):
    return b, a


# Selection Sort
def selection_sort(target_list):
    length = len(target_list)

    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if target_list[index] > target_list[j]:
                index = j
        target_list[i], target_list[index] = swap(target_list[i], target_list[index])

    return target_list


# Bubble Sort
def bubble_sort(target_list):
    length = len(target_list)

    for i in range(length - 1, 0, -1):  # This code needs to be understood.
        for j in range(0, i):           # This too.
            changed = False

            if target_list[j] > target_list[j + 1]:
                target_list[j + 1], target_list[j] = swap(target_list[j + 1], target_list[j])
                changed = True
        if not changed:
            break

    return target_list


# Insertion Sort
def insertion_sort(target_list):
    length = len(target_list)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if target_list[j] < target_list[j - 1]:
                target_list[j], target_list[j - 1] = swap(target_list[j], target_list[j - 1])
            else:
                break
    return target_list


# Shell Sort
# 1. Helper for shell Sort
def helper_insertion(target_list, start, last, h):
    for i in range(start + h, last + 1, h):
        for j in range(i, start, -h):
            if target_list[j] < target_list[j - h]:
                target_list[j], target_list[j - h] = swap(target_list[j], target_list[j - h])
            else:
                break

# 2. shell sort implementation
def shell_sort(target_list):
    length = len(target_list)
    h = length // 2

    while h >= 1:
        for i in range(h):
            helper_insertion(target_list, i, length - 1, h)

        h //= 2

    return target_list


# Merge sort
def merge_sort(t_list):
    def divide(tt_list, start, end):
        if start >= end:
            return

        mid = (start + end) // 2

        divide(tt_list, start, mid)
        divide(tt_list, mid + 1, end)
        merge(tt_list, start, mid, end)


    def merge(tt_list, start, mid, end):
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


if __name__ == '__main__':
    test_list = [random.randint(1, 101) for _ in range(100)]
    print("Before sort : ", test_list)
    merge_sort(test_list)
    print("After  sort : ", test_list)


