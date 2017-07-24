"""Get answer of given quadratic equation formula.

    This is an another example of argparse module.
    This py file gets coefficient of quadratic equation
    and print out the answers.

    Only INTEGER numbers are permitted for arguments and answers can
    reach to complex number.

    I'll extend this to float values later

    To be honest I thought this would be a very easy question.
    But it wasn't

        - How can you determine if a string argument is a int or float?
          This is not that easy, because down casting from int to float is possible
          So it was prone to lose data.


    Start Date : 2017/07/23
    End Date   : 2017/07/24
"""


import argparse
import math


# superscripts for mathematical squares.
SUPERSCRIPTS = ['x\u2070', 'x\u00b9', 'x\u00b2']
PLUS_MINUS = ' \u00b1 '


# Read from here for argparse module. Not that complex as it looks like.
# https://docs.python.org/3/library/argparse.html#module-argparse
parser = argparse.ArgumentParser(description="Get the answer of quadratic equation formula.",)
parser.add_argument('x2',
                    help='Coefficient of quadratic term. REQUIRED.',
                    metavar=SUPERSCRIPTS[2],
                    type=int,)

parser.add_argument('x1',
                    default=0,
                    help='Coefficient of primary term. Can be ommitted.',
                    nargs='?',
                    metavar=SUPERSCRIPTS[1],
                    type=int,)

parser.add_argument('x0',
                    default=0,
                    help='Constant of formula. Can be omitted',
                    metavar=SUPERSCRIPTS[0],
                    nargs='?',
                    type=int,)
parser.add_argument('-v', '--verbose', action='count', default=0)
args = parser.parse_args()


x2, x1, x0 = args.x2, args.x1, args.x0
multiple_root = False  # multiple root is '중근' in korean.

# Coefficient of x ^ 2 can't be 0 here.
if x2 == 0:
    raise ValueError("Quadratic coefficient must be given beside 0.")


# Answers are real numbers
if x1 ** 2 - 4 * x2 * x0 > 0:
    answer = str((-x1) / (x2 * 2)) + PLUS_MINUS + str(math.sqrt(x1**2 - 4*x2*x0) / (x2 * 2))
# Multiple root exists
elif x1 ** 2 - 4 * x2 * x0 == 0:
    multiple_root = True
    answer = str((-x1) / (x2 * 2))
# Answers are complex numbers
else:
    answer = str(-x1 / (x2 * 2)) + PLUS_MINUS +\
                str(math.sqrt(abs(x1**2 - 4*x2*x0)) / (x2 * 2)) + 'i'

# Verbose print format
if args.verbose >= 1:
    return_string = "\n\tGiven formula is '"
    for i, x in enumerate([x2, x1, x0]):
        return_string += str(x) + SUPERSCRIPTS[2-i] if x != 0 else ''
        return_string += '+ ' if x > 0 else '- '
    return_string = return_string[:-2]
    return_string += "'.\n\t"
    if multiple_root:
        return_string += 'It has a multiple root and the answer is {}'.format(answer)
    else:
        return_string += 'It has 2 answers: {}'.format(answer)
# Normal mode. Only print out answers.
else:
    return_string = 'Answer : {}'.format(answer)


print(return_string)
