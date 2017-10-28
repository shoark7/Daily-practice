"""Implement D3 Linear scale in Python

    Do you know the awesome javascript library D3(Data-Driven Document)?
    If you don't, check it out here: https://d3js.org
    This library provides various methods to make a plot with data.

    And its core function is making a 'scale'
    scale gets real data and changes it into a printable size(mainly pixel)
    In D3, data input range is 'domain', and ouput range is 'range'.

    Also D3 supports method chaining, which you can concatenate method calls
    as many times as you want.

    I implemented this points into Python.
    This time only supports linear scale, later log scale and exp scale will be updated.

    Start Date : 2017/10/28
    End   Date : 2017/10/28
"""


class LinearScale:
    """Linear scale class in D3"""
    def __init__(self):
        """Initialize a linear scale."""
        self.x = [0, 1]
        self.x_range = 1
        self.y = [0, 1]
        self.y_range = 1

    def __call__(self, v):
        """Change v to adequate y ranged value."""
        if not self.x[0] <= v <= self.x[1]:
            raise ValueError("Given value is beyond domain limits")

        ratio = abs(self.x[0] - v) / self.x_range
        y_value = ratio * self.y_range

        if self.y[0] <= self.y[1]:
            return self.y[0] + y_value
        else:
            return self.y[0] - y_value

    def __repr__(self):
        """Representation string for linear scale"""
        return "Linear scale of x: " + str(self.x) + ", y: " + str(self.y)

    def __str__(self):
        """Stringed format for linear scale"""
        return self.__repr__()

    def _test_limit(self, limit):
        """Check input 'limit' for domain and range methods
        Both domain and range function gets limit for input argument.
        limit should 
            1. be a sequence of length 2.
            2. have elements which are all numbers

        _test_limit protected method checks for that.
        If any one doesn't satisfy this conditions,
        raise Error.
        """
        if len(limit) != 2:
            raise TypeError("Limit should be a Sequence that contains 2 length values")
        elif not all(type(x) in (int, float) for x in limit):
            raise ValueError("Each element should be a int or a float")
        else:
            pass

    def domain(self, limit=None):
        """Set x range

            In D3, domain means input x area.
            With given limit, this function
            sets x domain

            if limit is None:
                just print current x domain.
        """
        if limit is None:
            return self.x
        self._test_limit(limit)
        x1, x2 = limit
        self.x = [x1, x2]
        self.x_range = abs(x1 - x2)
        return self

    def range(self, limit=None):
        """Set y range

            In D3, range means pixel print area.
            With givien limit, this function
            sets y range.

            If limit is None:
                just print current y range.
        """
        if limit is None:
            return self.y

        self._test_limit(limit)
        y1, y2 = limit
        self.y = [y1, y2]
        self.y_range = abs(y1 - y2)
        return self
