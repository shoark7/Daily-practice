"""
This is merge sort algorithm that I wrote.

Start date : 2017-02-15
End date   : 2017-02-15
"""

def merge_sort(the_list):
       
    def divide(the_list, start, end):
        if end - start < 1:
            return None
        
        middle = (start + end) // 2
        divide(the_list, start, middle)
        divide(the_list, middle + 1, end)
        
        merge(the_list, start, middle, end)

        
    def merge(the_list, start, middle, end):
        destination = [None for _ in range(end - start + 1)]
        left = start            # until left is smaller or equals to middle
        right = middle + 1      # until right is smaller or equals to end.
        i = 0

        
        while left <= middle and right <= end:
            if the_list[left] > the_list[right]:
                destination[i] = the_list[right]
                right += 1
            else:
                destination[i] = the_list[left]
                left += 1
            i += 1
            
        while left <= middle:
            destination[i] = the_list[left]
            left += 1
            i += 1
            
        while right <= end:
            destination[i] = the_list[right]
            right += 1
            i += 1
            
        the_list[start : end + 1] = destination
        
    divide(the_list, 0, len(the_list) - 1)
    return the_list
    

the_list = [1,12, 12,4,11, 120 ,4, 53]
print(merge_sort(the_list))
