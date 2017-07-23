"""



"""


import argparse
import math


SUPERSCRIPTS = ['x\u2070', 'x\u00b9', 'x\u00b2']
PLUS_MINUS = ' \u00b1 '


parser = argparse.ArgumentParser(description="Get the answer of quadratic equation formula.",)

parser.add_argument('x2',
                    metavar=SUPERSCRIPTS[2],
                    type=int,
                    help='Coefficient of quadratic term. REQUIRED.')

parser.add_argument('x1',
                    metavar=SUPERSCRIPTS[1],
                    nargs='?',
                    type=int,
                    help='Coefficient of primary term. Can be ommitted.',
                    default=0,)

parser.add_argument('x0',
                    metavar=SUPERSCRIPTS[0],
                    type=int,
                    help='Constant of formula. Can be omitted',
                    nargs='?',
                    default=0,)
parser.add_argument('-v', '--verbose', action='count', default=0)
args = parser.parse_args()


x2, x1, x0 = args.x2, args.x1, args.x0
multiple_root = False

if x2 == 0:
    raise ValueError("Quadratic coefficient must be given beside 0.")


if x1 ** 2 - 4 * x2 * x0 > 0:
    answer = str((-x1) / (x2 * 2)) + PLUS_MINUS + str(math.sqrt(x1**2 - 4*x2*x0) / (x2 * 2))
elif x1 ** 2 - 4 * x2 * x0 == 0:
    multiple_root = True
    answer = str((-x1) / (x2 * 2))
else:
    answer = str(-x1 / (x2 * 2)) + PLUS_MINUS +\
                str(math.sqrt(abs(x1**2 - 4*x2*x0)) / (x2 * 2)) + 'i'

if args.verbose >= 1:
    return_string = "\n\tGiven formula is '"
    for i, x in enumerate([x2, x1, x0]):
        return_string += str(x) + SUPERSCRIPTS[2-i] if x != 0 else ''
    return_string += "'.\n\t"
    if multiple_root:
        return_string += 'It has a multiple root and the answer is {}'.format(answer)
    else:
        return_string += 'It has 2 answers: {}'.format(answer)
else:
    return_string = 'Answer : {}'.format(answer)


print(return_string)
