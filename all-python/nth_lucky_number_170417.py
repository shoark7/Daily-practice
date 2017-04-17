"""Get nth lucky number.

Number which consists of only '4' and '7' is lucky number.

These numbers are ... 4, 7, 44, 47, 74, 77, 444 ...
This program gets nth lucky number with integer input.

The very core of this code is using binary number to calculate
exact nth lucky number. I got onto the next level of my coding capability.

Start date : 2017/04/17
End date   : 2017/04/17
"""


def nth_lucky_number(nth):
    """Get nth lucky number.

    Its way of operation is
        1. Get the digit of target lucky number.
        2. 4 and 7 is actually another form of binary number(101 = 747)
           So convert nth to a binary number.
        3. Then map 0 to 4 and 1 to 7.

    :input:
        nth: nth number.
    :return:
        nth lucky number. Its form is integer.
    """

    # input validation
    if not isinstance(nth, int) or nth <= 0:
        raise TypeError("Give me a integer over 1")

    expo = 1
    total_index = 0

    while not (1 + total_index <= nth <= total_index + 2 ** expo):
        total_index += 2 ** expo
        expo += 1

    left = nth - total_index - 1
    # This is kind of tricky. Do you know why left is subtracted by 1?

    bin_format = '{:0{}b}'.format(left, expo)
    # When digit size is set, this code converts difference to binary number.

    answer = ''.join(map(lambda x: '4' if x == '0' else '7', bin_format))
    # 0 is mapped to 4, 1 is mapped to 7.
    # Python programmer is familiar with str.join, map, lambda.

    return int(answer)


# Test code
if __name__ == '__main__':

    for nth in range(1, 21):
        print('nth is {:2}, nth lucky number is {:4}'.format(nth, nth_lucky_number(nth)))
