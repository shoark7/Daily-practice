"""Binary tree algorithm in class way

Last post was bianry tree in list way.
Now this time I use class Node and class Tree.
It would be more systematic I think and I recommend this instead of last one.

Start date : 2017/03/20
End date   : 2017/03/20
"""

class Node:
    """Node for the binary tree."""
    def __init__(self, data, left=None, right=None):
        """Initialize node.
        :input:
            data  : (required)Value of the node.
            left  : Left child of the node.
            right : right child of the node.
        :return: None
        """

        self.right = right
        self.left = left
        self.data = data

    def __repr__(self):
        """String formatted print of the node."""
        print("Value of this node is", self.data)


class Binary_tree:
    """Binary tree with class.

    This tree has no node collections but only a root node indicator and ordering algorithms.
    With given root node, it can execute
                            1. pre order,
                            2. in order,
                            3. post order ordering.
    """

    def __init__(self):
        self.root = None

    def __repr__(self):
        if not self.root:
            print("Root is not set. You should set root for ordering.")

        print("Binary_tree object with root node value {}".format(self.root.data))

    def set_root(self, node):
        """Tree must have root node to execute ordering.
        :input:
            node : Node type instance. If the given node is not Node type, error occurs.
        :return:
            None. Just set root node.
        """
        if not isinstance(node, Node):
            raise TypeError("Root must be Node type.")

        self.root = node

    def pre_order_search(self, node=None):
        """Pre order algorithm.
        :input:
            node : It must be Node type.
        :return:
            None. Just print elements. You can override to do other jobs.
        """
        if node is None:
            return

        print(node.data, end=' ')
        self.pre_order_search(node.left)
        self.pre_order_search(node.right)

    def in_order_search(self, node=None):
        """In order algorithm.
        :input:
            node : It must be Node type.
        :return:
            None. Just print elements. You can override to do other jobs.
        """
        if node is None:
            return

        self.in_order_search(node.left)
        print(node.data, end=' ')
        self.in_order_search(node.right)

    def post_order_search(self, node=None):
        """Post order algorithm.
        :input:
            node : It must be Node type.
        :return:
            None. Just print elements. You can override to do other jobs.
        """
        if node is None:
            return

        self.post_order_search(node.left)
        self.post_order_search(node.right)
        print(node.data, end=' ')


# Test code

if __name__ == '__main__':

    f = Node('F')
    e = Node('E')
    c = Node('C', e, f)
    d = Node('D')
    b = Node('B', d)
    a = Node('A', b, c)

    tree = Binary_tree()

    tree.set_root(a)

    print("pre order search")
    tree.pre_order_search(tree.root)

    print("\nin order search")
    tree.in_order_search(tree.root)

    print("\npost order search")
    tree.post_order_search(tree.root)
    print()
