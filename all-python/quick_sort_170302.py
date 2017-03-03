"""
This is quick sort with Haedeun Kim.
After now, I'll implement quick sort in C too.

Start date : 2017/03/02
End date   : 2017/03/03
"""

def quick_sort(array):

    length = len(array)

    def divide_conquer(left, right):
        if right - left <= 1:
            return

        pivot = left
        low = left + 1
        high = right
        print('pivot is', pivot)

        while low < high:  # 2
            while array[pivot] >= array[low] and low < right: # 3
                low += 1

            while array[pivot] <= array[high] and high > left: # 4
                high -= 1

            if low < high:
                array[low], array[high] = array[high], array[low]
                print('list is', array)

        array[pivot], array[high] = array[high], array[pivot]
        print('list is', array)

        divide_conquer(left, high - 1)
        divide_conquer(high + 1, right)

    divide_conquer(0, length - 1)
    return array

l = [5, 4, 3, 2, 1]
print(quick_sort(l))
