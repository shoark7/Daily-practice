"""
Upgraded FizzBuzz with lambda or list comprehension.
With given a number and tuples of numbers and their strings, I realize FizzBuzz.
For example, new_fizzbuzz(n, (3, 'Fizz'), (5, 'Buzz'):

1.  1
2.  2
3.  'Fizz'
4.  4
5.  'Buzz'
...
15. 'FizzBuzz' and so on until n.

Input tuples are limitless.
Please compare this to the previous FizzBuzz version.
It must have been extended and got better. Thanks.

Start date = 2016/09/24
End date = 2016/09/24
"""

## list comprehension version.
def new_fizzbuzz_comp(n, *args):
    # arg[0] is a number and arg[1] is a text string.
    result = '\n'.join(
                            [ ''.join(
                                            [arg[1] if i%arg[0] == 0 else '' for arg in args ]
                                    ) if ''.join([arg[1] if i%arg[0] == 0 else '' for arg in args ]) else str(i) for i in range(1, n+1)]
                        )
    return result

print(new_fizzbuzz_comp(100, (3, 'fizz'), (5, 'buzz')))

print('=' * 20 )
print('Comprehsion version is finished!')
print('Lambda version is beginning!')
print('=' * 20 )
## lambda version
def new_fizzbuzz_lambda(n, *args):
    # arg[0] is a number and arg[1] is a text string.
    result = '\n'.join(map(lambda n:
                    ''.join(map(lambda arg:
                        arg[1] if n%arg[0] == 0 else ''
                        , args))
                   if ''.join(map(lambda arg:
                        arg[1] if n%arg[0] == 0 else ''
                        , args))
                   else str(n)
                 , range(1, 101)))
    return result

print(new_fizzbuzz_lambda(100, (3, 'fizz'), (5, 'buzz')))
print('Lambda version is finished!')


"""
With this version, the len(tuple) can be any numbers from 1 to ~~.
So this version is much better I think.
But the limit of this version is that I cannot handle the kwargs input.
A more precise version may have to handle the inputs of dict.
Like 'new_fizzbuzz(100, fizz = 3, buzz = 3)'.
But this seems good also. :)
"""
