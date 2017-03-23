"""Change given x, y coordinates to polar coordinates.

We usually study normal coordinates system.
But it can be changed to polar coordinates.

This function changes given (x, y) coordinates into polar coordinates,
and shows data about the coordinate.

We mostly use built-in math modules for trigonometric funcionts.

Start date : 2017/03/24
End date   : 2017/03/24
"""

import math


def to_polar_coordinates(x, y):
    tan_xy = y / x
    seta = math.atan(tan_xy)
    r = (x ** 2 + y ** 2) ** (1/2)

    return "Your ({x:}, {y:}) is changed to ({cos:}, {sin:})".format(
                    x=x, y=y,
                    cos=str(r)[:3] + "Cos" + str(seta)[:3],
                    sin=str(r)[:3] + "Sin" + str(seta)[:3])


print(to_polar_coordinates(3, 4))
print(to_polar_coordinates(1, 1))
