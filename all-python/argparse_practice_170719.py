"""A simple argparse module practice.

    Hello, You know I'm alive.

    I've seen so many projects supporting cli environments use argparse modules.
    So I read module tutorial and module official doc page and wrote examples.
    Let's get it

    Start date : 2017/07/19
    End date   : 2017/07/19
"""


import argparse


# 1. Simple calcuator
parser = argparse.ArgumentParser(description='Calculator for 4 simple jobs')
parser.add_argument('x', type=int, help='First number')
parser.add_argument('y', type=int, help='Second number')

group = parser.add_mutually_exclusive_group()
group.add_argument('--plus', '-p', action='store_true', help='Plus')
group.add_argument('-s', '--subtract', action='store_true', help='Subtract')
group.add_argument('-m', '--multiply', action='store_true', help='Multiply')
group.add_argument('-d', '--divide', action='store_true', help='Divide')

args = parser.parse_args()

if args.plus:
    print(args.x + args.y)
elif args.subtract:
    print(args.x - args.y)
elif args.multiply:
    print(args.x * args.y)
elif args.divide:
    print(args.x / args.y)
else:
    print("No optional argument")


# 2. Get number of ints
parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='An integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='Sum the integers(default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


# 3. Open a file and write something
parser = argparse.ArgumentParser(description='Write a file with given text')
parser.add_argument('infile', type=argparse.FileType('r', encoding='utf-8'),
                    help='File name to be written')
parser.add_argument('texts', nargs=argparse.REMAINDER, help='Any string to write')

args = parser.parse_args()

texts = ' '.join(args.texts)
args.infile.write(texts)
args.infile.close()

print("Successfully written!")
