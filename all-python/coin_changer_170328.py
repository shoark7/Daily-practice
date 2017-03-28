"""Get number of coin changes.

This algorithm is an easy example of greedy algorithm.
With given change, you get the least number of coins you receive.

In Korea, we use won and coin units here are:
    "500, 100, 50, 10, 1"

Start date : 2017/03/28
End date   : 2017/03/28
"""


def least_coin_number(change):
    original_change = change
    units = [500, 100, 50, 10, 1]
    total_num = 0
    combinations = {}
    return_string = ''

    for unit in units:
        number, change = divmod(change, unit)

        if number:
            total_num += number
            combinations[unit] = number

    return_string += 'Given change : {}, Total numbers : {}\n'.format(
        original_change, total_num)
    return_string += '-' * 20 + '\n'

    for unit, number in sorted(combinations.items(), reverse=True):
        return_string += '{:3d} : {}\n'.format(unit, number)

    return return_string


if __name__ == '__main__':
    change = 7800
    print(least_coin_number(change))
    print('\n')

    change = 13200
    print(least_coin_number(change))
    print("\n")
