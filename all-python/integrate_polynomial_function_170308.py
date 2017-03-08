"""
What fill follow after diffential is integral.
Now I'll make a integral polynomial function.
It will take a slightly different method of approach.
We will use a closure. I think this would be better.

Start date : 2017/03/08
End date   : 2017/03/08
"""


def integral_polynomial_function(*factors, a=None, b=None):
    """Integrate polynomial function. Read manual carefully.
    :input:
        Without a and b, you will get indefinite integral.
        With a and b together, you will get definite integral.

        factors: function factors in a sequence
                 like 'x^2 + 1' -> '1, 0, 1'.
                 You need zeros in blank degrees.
        a: Start point of your integral area.
        b: End point of your integral area.
    :return:
        if indefinite integral:
            expression
        else:
            expression and calculated definite integrated area.

        Start date : 2017/03/08
        End date   : 2017/03/08
    """

    SUPERSCRIPTS = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    string_expression = ''
    factors = list(factors)
    max_degree = len(factors) - 1
    if a and b:
        mathmatical_expression = 0

    def integral_once(factor, degree, *x):
        result_sum = 0
        result_string = ''
        if x:
            a, b = x

        if factor > 0:
            result_string += ' + '
        elif factor == 0:
            pass
        else:
            result_string += ' - '

        result_string += '{}x{}'.format(1 / (degree + 1) * factor, SUPERSCRIPTS[degree + 1])

        if x:
            result_sum += factor / (degree + 1) * (b ** (degree + 1)) - factor / (degree + 1) * (a ** (degree
                                                                                             + 1))
            return result_string, result_sum
        else:
            return result_string

    for i, factor in enumerate(factors):
        string_expression += integral_once(factor, max_degree - i)
        if a and b: # 정적분(definite integral)
            mathmatical_expression += integral_once(factor, max_degree - i, a, b)[1]
        else:
            pass    # 부정적분(indefinite integral)

    string_expression = string_expression[3:]

    if a and b:
        return string_expression, mathmatical_expression
    else:
        return string_expression


print(integral_polynomial_function(3, 1, 2, a=2, b=4))
print(integral_polynomial_function(1,1,1,1,1, a=2, b=3))
