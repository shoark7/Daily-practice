"""A 2D matrix implementation in Python.
--------------------------------------------------------------------------

    I know matrices in R and numpy and I referred to them slightly.
    Matrix can only have numeric type elements, rejecting other types.

    This module has 2 attributes:
        is_matrix, Matrix

    is_matrix is a function that judges if input can be a instance of Matrix class.
    Matrix is a matrix class.

    This matrix doesn't give high performances to use for various reasons:
        1. Initializing is fucking hard.
            You have to make 2d lists yourself and hand them in to __init__ function.
            Making matrices in R or numpy is so easy compared to mine.
        2. Using list is not effective.
            Believe me, List is so expensive.

    And the codes are simple, just check __mul__ method of Matrix.

    Start date: 2017/04/19
    End   date: 2017/04/20
"""


__all__ = ['is_matrix', 'Matrix']


def is_matrix(matrix):
    """Check if input can be a instance of Matrix.

    This function checks 3 things.
        1. Check if input is a list type itself.
        2. Check if all rows' lengths are equal.
        3. Check if all elements in input are numeric type.

    If input passes these 3 tests, return True, else False

    :input:
        matrix: A target to be tested. Only one can be submitted.
    :return:
        Bool value of whether input can be a Matrix instance or not.
    """

    # Check if matrix and elements in matrix are both lists.
    if not isinstance(matrix, list) or \
       not all(map(lambda x: isinstance(x, list), matrix)):
        return False
    # Check if lengths of rows in the matrix are all same.
    elif not all(map(lambda x: x == len(matrix[0]), (len(row) for row in matrix))):
        return False
    # Check all elements in the matrix are either int or float type.
    else:
        for row in matrix:
            if not all(map(lambda x: isinstance(x, (int, float)), row)):
                return False
    return True


class Matrix:
    """2D numeric Matrix class.

        Multiplication between matrix instances are supported.
        When __mul__ is called, a new Matrix is created and returned.

        Item indexing is possible like 'row, col'(e.g. matrix[1, 2])
        Otherwise, :P Sorry, mine is not numpy.

        This matrix class supports these attributes:
            dim: Dimension of the matrix. You can't change.
            name: You can initialize its name. Can be changed.
            sum: You can get the sum of all elemtns in the matrix. Cannot be changed.

        Also supports this method:
            print: Print out all values in the matrix. One row in one line.
    """

    def __init__(self, matrix, name=None):
        """Initialize a matrix.

        :input:
            matrix: matrix should pass is_matrix test. Check is_matrix.__doc__
            name: if name is not None, it is changed to str and name attribute is set.
        """

        if isinstance(matrix, Matrix):
            return 
        elif not is_matrix(matrix):
            raise TypeError("Given input is not a matrix")
        self.__matrix = matrix
        self.__row = len(self.__matrix)
        self.__col = len(self.__matrix[0])
        self.__total_size = self.__row * self.__col
        self._name = str(name) if name else None
        self.__sum = sum(sum(row) for row in self.__matrix)

    def __getitem__(self, tup):
        """Item indexing in Matrix instance.

        You sholud pass a 2-integer tuple.(e.g. k[1, 2])
        Otherwise you get error.
        """
        x, y = tup
        return self.__matrix[x][y]

    def __repr__(self):
        """Representation string for matrix. If the matrix has a name, it's printed."""
        if self._name:
            return "{} : A {} X {} matrix that has {} items".format(self._name,
                                                                    self.__row,
                                                                    self.__col,
                                                                    self.__total_size)
        else:
            return "A {} X {} matrix that has {} items".format(self.__row,
                                                               self.__col,
                                                               self.__total_size)

    def __mul__(self, other_matrix):
        """Multiplication between matrices.

        It's a normal matrix multiplication.
        Left operand's col length and right operand's rows length should be same.

        Remember, both 2 operands should be the instances of Matrix.
        Return a new matrix with the result of calculation.
        """
        if not isinstance(other_matrix, Matrix):
            raise TypeError("Multiplication is possible only between 2 Matrix instances")
        elif self.__col != other_matrix.__row:
            raise ValueError("Length of columns and rows should be same")

        new_one = [[0 for col in range(other_matrix.__col)] for row in range(self.__row)]

        for i in range(self.__row):
            for j in range(other_matrix.__col):
                temp = 0
                for k in range(self.__col):
                    temp += self.__matrix[i][k] * other_matrix.__matrix[k][j]
                new_one[i][j] = temp

        new_one = Matrix(new_one)

        return new_one

    # I wanted to support statemens like sum(matrix). But..
    # Python don't support __sum__ method
    # def __sum__(self, *args, **kwargs):
    #    return self.sum

    def __str__(self):
        """Same as __repr__"""
        return self.__repr__()

    @property
    def dim(self):
        """Dimension of the matrix. Return a tuple of row and column length."""
        return (self.__row, self.__col)

    @dim.setter
    def dim(self, *args, **kwargs):
        """You can not change dimension of the matrix"""
        raise TypeError("You can't change the matrix's dimension")

    @property
    def name(self):
        """Return name of the matrix if it exists. Otherwise alt string."""
        return self._name if self._name else "I don't have a name"

    @name.setter
    def name(self, new_name):
        """Name can be changed with new value.

        Name is automatically changed to string type.

        :input:
            new_name: A new name you want.
        :return:
            None. Just set the name.
        """
        self._name = str(new_name)

    def print(self):
        """Print values in a matrix."""
        for row in self.__matrix:
            print(row)

    @property
    def sum(self):
        """Return sum of all elements in the matrix."""
        return self.__sum

    @sum.setter
    def sum(self, *args, **kwargs):
        """You can not change sum of the matrix."""
        raise TypeError("You can't change sum of the matrix")
