"""Implement an optimal version of FizzBuzz problem.

    I have implemented several kinds of fizzbuzz problems.
    Now using type validation and generator expression,
    I implemented an optimal version of FizzBuzz.

    You can check previous versions and check how it goes.
    This is the final version of fizzbuzz and I think it is quite meaningful.
    Please check it ou.

    Start date: 2017/05/03
    End date  : 2017/05/03
"""


def fizzbuzz(n, *args):
    """Make a fizzbuzz string.

    Merits of this fizzbuzz is that you can extend
    fizzbuzz strings as many as you want.
    Normal fizzbuzz uses only (3, 'fizz'), (5, 'buzz'), but
    you can use (7, 'zzzz'), (11, 'ok!!') and even more.

    :input:
        n: max number of fizzbuzz string.
           Range of numbers are 1 ~ n.
        args: tuples of tuples.
              Small tuples consist of (number, word).
    """

    # Input validation
    if not isinstance(n, int) or n < 1:
        raise TypeError("First argument must be an integer over 1")

    if not all(isinstance(arg, tuple) for arg in args) or \
       not all(len(arg) == 2 for arg in args):
        raise TypeError("You must give tuples of numbers and strings")

    # args sorted by first element of each iterable
    args = list(args)
    args.sort(key=lambda x: x[0])

    # make fizzbuzz string 1. List comprehension way. I prefer this to map, filter, etc.
    result = '\n'.join(
        ''.join(word if i % number == 0 else '' for number, word in args)
        if ''.join(word if i % number == 0 else '' for number, word in args)
        else str(i) for i in range(1, n+1)
    )

    # make fizzbuzz string 2. map, filter way. But I should use this method well too!
    result2 = '\n'.join(map(lambda x:
                  ''.join(map(lambda y: y[1] if x % y[0] == 0 else '', args))
                  if ''.join(map(lambda y: y[1] if x % y[0] == 0 else '', args))
                  else str(x),
                  range(1, n+1)))

    return result2


# Test code
if __name__ == '__main__':
    print('fizzbuzz(100, (3, "fizz"), (5, "buzz"), (7, "kizz")) is..')
    print('-' * 50)
    print(fizzbuzz(100, (3, 'fizz'), (5, 'buzz'), (7, 'kizz')))
