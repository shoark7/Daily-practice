"""Linked array implemented in Python.

Hey guys, this time is linked array in Python.
I know that Python's list is a type of linked array, right?
We implement it with class Node and class Linked_array.

And also, this is one-way linked array.
double-way linked array is next time :)

Let's get started.

Start date : 2017/03/25
End date   : 2017/03/25
"""


class Node:
    """A single element of the linked array."""

    def __init__(self, value):
        """Initialize a node.
        It has next member variable.
        Our linked array is one-way array so before member is not need.
        :input:
            value : value of the node
        :return:
            None
        """
        self._next = None
        self._value = value

    def __repr__(self):
        """String format for checking values."""
        return "Value of this Node is {}".format(self._value)

    def __str__(self):
        """Same as self.__repr__()"""
        return self.__repr__()


class Linked_array:
    """A single-way linked array in Python.

    This array supports adding, deleting node methods.
    You can get the value of the node with index.
    But it don't support slicing.(like array[3:5])
    Also, This don't have __setitem__ method. I'll implement it when needed.
    """
    def __init__(self):
        """Initialize an array.

        head, tail, cursor are protected. You won't need to contact them directly.
        But you can see the length member variable directly.
        But don't change it to another value.
        """

        self._head = None
        self._tail = None
        self._cursor = None
        self.length = 0

    def __getitem__(self, index):
        """Get the value of index node.

        :input: index. It must be an int.
        :return: value of the node of the index.
        """

        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        elif index > self.length - 1:
            raise IndexError("Given index is too long.")
        elif index < 0:
            raise IndexError("Index must be greater or equal to 0.")

        for _ in range(index):
            self._cursor = self._cursor._next

        item = self._cursor._value
        self._cursor = self._head

        return item

    def __repr__(self):
        """String format for print.

        First, print out the length of the array.
        You get each element's value next line.
        """
        print("Total length {}. Elements are ..".format(self.length))
        for i in range(self.length):
            print(self._cursor._value, end=' ')
            self._cursor = self._cursor._next

        self._cursor = self._head

        return ''

    def __str__(self):
        """Same as self.__repr__()"""
        return self.__repr__()

    def add_node(self, value):
        """Add a node to the list.

        :input:
            value : Data to be inserted.
        :return:
            None
        """

        new_node = Node(value)

        if self.length == 0:
            self._head = new_node
            self._tail = new_node
            self._cursor = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

        self.length += 1

    def delete_node(self, index=None):
        """Delete the element of the array.

        If index is not given, last element of the array is removed.

        :input:
            index: Must be an integer. Negative indexing is not supported yet.
        :return:
            None. Just remove the element.
        """

        if index is None:
            index = self.length - 1
        elif isinstance(index, int):
            raise TypeError("Index must be an integer.")
        elif index > self.length - 1:
            raise IndexError("Given index is too long.")
        elif index < 0:
            raise IndexError("Index must be greater or equal to 0.")

        for i in range(index - 1):
            self._cursor = self._cursor._next

        before_node = self._cursor

        if index == 0:
            self._head = self._head._next

        elif index == self.length - 1:
            before_node._next = None
            self._tail = before_node

        else:
            before_node._next = before_node._next._next

        self.length -= 1
        self._cursor = self._head

        print("Successfully deleted.")
