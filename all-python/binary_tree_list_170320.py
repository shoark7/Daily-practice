"""Implement binary tree in Python.

Today, I'll implement binary trees in Python in list way.

This file will be added to algorithm class asignment file due this Sunday.

Start date : 2017/03/20
End date   : 2017/03/20
"""

import math

class Tree:
    """Binary tree with pre, in, post order algorithm.
    This is implemented in a list way."""

    def __init__(self, value):
        """Frist zero is nothing and initialize with given value."""
        self.tree = [0, value]  # value is root node's value

    def __repr__(self):
        """print list as it is."""
        return str(self.tree)

    def left(self, index):
        """Find left value.
        :input: index
        :return: (index of left node, value of left node)
        """
        if 2 * index > len(self.tree) - 1:
            return

        return 2 * index, self.tree[2 * index]   # return index together for search

    def right(self, index):
        """Find left value.
        :input: index
        :return: (index of right node, value of right node)
        """
        if 2 * index + 1 > len(self.tree) - 1:
            return

        return index * 2 + 1, self.tree[2 * index + 1]

    def add_node(self, index, value, direction='left'):
        """Add a new node with given value. Direction is left(default).
        Empty spaces will be filled up with math.nan.
        :input:
            index: parent node's index
            value: value of a new node
            direction: whether a child node is on right or left.
        :return: None
        """

        if index > len(self.tree) - 1 or self.tree[index] == math.nan:
            raise IndexError("Parent node doesn't exist.")

        target_index = index * 2 if direction is 'left' else index * 2 + 1

        if target_index < len(self.tree):
            self.tree[target_index] = value
        else:
            while len(self.tree) < target_index:
                self.tree.append(math.nan)

            self.tree.append(value)

    def preorder_search(self, index=1):
        """Preorder search algorithm."""
        if index is None or index > len(self.tree) - 1:
            return

        print(self.tree[index])
        self.preorder_search(index * 2)
        self.preorder_search(index * 2 + 1)

    def inorder_search(self, index=1):
        """Inorder search algorithm."""
        if index is None or index > len(self.tree) - 1:
            return

        self.inorder_search(index * 2)
        print(self.tree[index])
        self.inorder_search(index * 2 + 1)

    def postorder_search(self, index=1):
        """Postorder search algorith."""
        if index is None or index > len(self.tree) - 1:
            return

        self.postorder_search(index * 2)
        self.postorder_search(index * 2 + 1)
        print(self.tree[index])
