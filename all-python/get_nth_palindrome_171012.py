"""
Mission of this problem is to get nth palindrome.

1~9 is counted.

Start Date : 2017/01/12
End Date   : 2017/01/12
"""

def is_palindrome(number):
    number = str(number)
    for i in range(int(len(number)) // 2):
        if number[i] != number[int(len(number)) - 1 - i]:
            return False
    return True


def get_nth_palindrome(nth):
    count = 0
    start = 1
    while count != nth:
        if is_palindrome(start):
            count += 1
            if count == nth:
                return start
        start += 1


if __name__ == '__main__':
    print('7 is is_palindrome', is_palindrome(7))
    print('1000 nth palindrome is', get_nth_palindrome(1000))
