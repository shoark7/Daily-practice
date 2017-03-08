"""
This function is focused to differentiate polynomial function.
I'm studying calculus nowadays and I wanted to implement differential &  integral.
First goal is differential.
Let's go

Start date : 2017/03/08
End date   : 2017/03/08
"""


def diffentiate_polynomial_function(*factors, x=None):
    """Diffentiate input function.
    input:
        degrees: a polynomial function(ex. x^2 + x + 1)
        x: the point of wanted instantaneous rate of change

        if your function is 'x^4 + x + 1', input should be,
        '1, 0, 0, 1, 1'. Empty zeros are needed.

    output:
        if x exists:
            instantaneous rate of change of x
        if not exists:
            print differential of your wanted function.
    """

    superscripts = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    factors = list(factors)
    max_degree = len(factors) - 1
    degrees = [i for i in range(max_degree, -1, -1)]

    string_expression = ''
    mathmatical_expression = 0

    for factor, degree in zip(factors[:-1], degrees[:-1]):
        super_number = superscripts[degree - 1]

        if factor > 0:
            string_expression += ' + ' + '{}x{}'.format(factor * degree, super_number)
        elif factor == 0:
            pass
        else:
            string_expression += ' - ' + '{}x{}'.format(factor * degree, super_number)

        if x:
            mathmatical_expression += factor * degree * (x ** (degree - 1))

    string_expression = string_expression[3:]
    print(string_expression)


    if x:
        return string_expression, mathmatical_expression
    else:
        return string_expression


print(diffentiate_polynomial_function(1,1,1, x=3))
print(diffentiate_polynomial_function(1,2,3,4,5, x=7))
