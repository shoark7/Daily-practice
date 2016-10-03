"""
Purpose of this file is to implement snail algorithm.
You can find many examples of it.

Start date = 2016/09/22
End date = 2016/09/22
"""
from pprint import pprint


def snail_maker(n):
    """Make a snail list. """
    result = [[0 for k in range(n)] for l in range(n)]
    x, y = 0, 0
    direction = [(0, 1), (1,0 ), (0, -1), (-1, 0)]
    turn = 0
    min = 0
    max = n - 1

    for i in range(1, n ** 2 + 1):
        # Assign numbers
        result[x][y] = i
        # Check if I can go next time
        if turn == 0:
            if y < max and result[x + direction[turn][0]][y + direction[turn][1]] == 0:
                x += direction[turn][0]
                y += direction[turn][1]
            else:
                turn += 1
                x += direction[turn][0]
                y += direction[turn][1]
                # 1, 2
        elif turn == 1:
            if x < max and result[x + direction[turn][0]][y + direction[turn][1]] == 0:
                x += direction[turn][0]
                y += direction[turn][1]
            else:
                turn += 1
                x += direction[turn][0]
                y += direction[turn][1]
        elif turn == 2:
            if y > min and result[x + direction[turn][0]][y + direction[turn][1]] == 0:
                x += direction[turn][0]
                y += direction[turn][1]
            else:
                turn += 1
                x += direction[turn][0]
                y += direction[turn][1]
        else:
            if x > min and result[x + direction[turn][0]][y + direction[turn][1]] == 0:
                x += direction[turn][0]
                y += direction[turn][1]
            else:
                turn = (turn + 1) % 4
                x += direction[turn][0]
                y += direction[turn][1]


    return result

pprint(snail_maker(10))


# Any other good codes are appreciated.
