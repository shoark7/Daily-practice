"""
It's been in ages from last post.

Today is merge sort implemented by Python.
Of course Python merge sort would not be so fast.
But I have to study C again in order to keep up with my study in college
and this will help implementing merge sort in C.

So let's begin.

Start date : 2017/03/01
End date   : 2017/03/01
"""


def merge_sort(array, descending=False):
    """Merge sort. Default is ascending."""

    try:
        array = list(array)
    except TypeError as e:
        print("Input is not listable.")
        print(e)
        return

    copy_list = array.copy()
    length = len(array)

    def divide(start, end):

        if end - start < 1:
            return

        middle = (start + end) // 2

        divide(start, middle)
        divide(middle + 1, end)

        merge(start, end)

    def merge(start, end):
        middle = (start + end) // 2
        left, right = start, middle + 1
        index = start

        while left <= middle and right <= end:
            if not descending:
                if array[left] > array[right]:
                    copy_list[index] = array[right]
                    right += 1
                    index += 1
                else:
                    copy_list[index] = array[left]
                    left += 1
                    index += 1
            else:
                if array[left] < array[right]:
                    copy_list[index] = array[right]
                    right += 1
                    index += 1
                else:
                    copy_list[index] = array[left]
                    left += 1
                    index += 1

        while left <= middle:
            copy_list[index] = array[left]
            left += 1
            index += 1

        while right <= end:
            copy_list[index] = array[right]
            right += 1
            index += 1

        array[start:end + 1] = copy_list[start: end + 1]

    divide(0, length - 1)
    return array


"""
My concern here is that I hope more efficient for deciding ascending and descending.
In this algorithm, I have to choose every merge process.
I think this will take much time.

What is a good idea?
"""
