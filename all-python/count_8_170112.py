"""
This is from 'http://codingdojang.com/scode/393#answer-filter-area'

It counts total number of '8' in a range from 1 to number(given by call).
If a number is 888 --> it counts up by 3.
881 --> by 2.

Start Date : 2017/01/12
End Date : 2017/01/12
"""


### My way.

def count_8(number):
    count = 0
    for i in range(1, number + 1):
        count += str(i).count('8')
    return count

### An user's way

user_way = ''.join(str(i) for i in range(1, 10001)).count('8')

if __name__ == '__main__':
    print('count_8 of 10000 is', count_8(10000))
    print("An user's way of 10000 is", user_way)
