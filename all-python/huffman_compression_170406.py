"""Huffman compression algorithm written in Python.

This chapter is the most challenging algorithm in this repository.
Huffman algorithm is an way of file compression.

'''For you busy people!
If you don't much time to analyze code,
at least I hope you check these parts of the code
    1. _encode method of Encoder class
    2. _decode method of Decoder class
These codes are core parts of the whole source code.
Please check :)
'''

Actually, this code is not mine.
It's from 'http://code.activestate.com/recipes/576603-huffman-coding-encoderdeconder/'
Code there was written in Python 2 so I rewrote it in Python 3.
It's challenging at first sight, but not unbreakable.
You'll learn much from this code, I think.

Start date : 2017/04/06
End date   : 2017/04/07

All rights are not reserved.
"""


import os
import pickle
import array


MAX_BITS = 8 # Max size of the bits to chop off.


class Node:
    """Huffman tree's node class."""
    recur_print = False

    def __init__(self, ch=None, fq=None, lnode=None, rnode=None, parent=None):
        """Initialize node.

        :input:
            ch: Character of the node.
            fq: Frequency of the node.
            lnode: Left child node of this node.
            rnode: Right child node of this node.
            parent: Parent node of this node.
        :return:
            None
        """
        self.l = lnode
        self.r = rnode
        self.p = parent
        self.c = ch
        self.fq = fq

    def __gt__(self, other):
        """'Greater than' comparsion for sort"""
        return self.fq > other.fq

    def __gte__(self, other):
        """'Greater than or equals to' comparsion for sort"""
        return self.fq >= other.fq

    def __lt__(self, other):
        """'Less than' comparsion for sort"""
        return self.fq < other.fq

    def __lte__(self, other):
        """'Less than or equals to' comparsion for sort"""
        return self.fq <= other.fq

    def __repr__(self):
        """Representative string format for the node."""
        if Node.recur_print:
            lnode = self.l if self.l else '#'
            rnode = self.r if self.r else '#'
            return ''.join(('{}:{}'.format(self.c, self.fq), str(lnode), str(rnode)))
        else:
            return '{}:{}'.format(self.c, self.fq)


def _pop_first_two_nodes(nodes):
    """Pop two nodes with least frequencies.

    :input:
        nodes: list or other iterables of nodes.
    :return:
        If length of nodes is over 1, return 2 nodes of least frequencies.
        If length of nodes is 1, return a tuple of the (node and None).
    """

    if len(nodes) > 1:
        first = nodes.pop(0)
        second = nodes.pop(0)
        return first, second
    else:
        return nodes[0], None


def _build_tree(nodes):
    """Build tree with nodes.

    :input:
        List or other iterable of the nodes.
    :return:
        Root node for the tree.
    """
    nodes.sort() # 내림 차순 정렬

    while True:
        first, second = _pop_first_two_nodes(nodes)
        if not second:
            return first
        parent = Node(lnode=first, rnode=second, fq=first.fq + second.fq)
        first.p = parent
        second.p = parent
        nodes.insert(0, parent)
        nodes.sort()


def _gen_huffman_code(node, dict_codes, buffer_stack=[]):
    """Generate huffman code with huffman tree.

    With the tree we made before, we assign the code to the node.
    More frequent the node is, Shorter the code is.

    :input:
        node: Node to be assigned.
        dict_nodes: Dictionary connectingthe character and the code.
        buffer_stack: Buffer to complete the code for the node.
    :return:
        None. Just fille the dict_codes.
    """

    if not node.l and not node.r:
        dict_codes[node.c] = ''.join(buffer_stack)
        return
    buffer_stack.append('0')
    _gen_huffman_code(node.l, dict_codes, buffer_stack)
    buffer_stack.pop()

    buffer_stack.append('1')
    _gen_huffman_code(node.r, dict_codes, buffer_stack)
    buffer_stack.pop()


def _cal_freq(long_str):
    """Count the frequency of the character in a string.

    With given string,
    count the frequency of every character in the string.

    :input:
        long_str: String to count.
    :return:
        defaultdict of the frequency counted.
    """
    from collections import defaultdict
    d = defaultdict(int)
    for c in long_str:
        d[c] += 1
    return d


class Encoder:
    """Encoder class.

    Encoder encodes normal string of files into compressed file or string.
    """

    def __init__(self, filename_or_string=None):
        """Initialize the encoder.

        :input:
            filename_or_string:
                if this is filename, we open it and read it.
                if this is just a string, we take it
        :return:
            None. Just open and read the string.
        """
        if filename_or_string:
            if os.path.exists(filename_or_string):
                self.encode(filename_or_string)
        else:
            self.long_str = filename_or_string

    def __get_long_str(self):
        """Property for the string."""
        return self._long_str

    def __set_long_str(self, s):
        """Property setter for the string."""
        self._long_str = s
        if s:
            self.root = self._get_tree_root()
            self.code_map = self._get_code_map()
            self.array_codes, self.code_length = self._encode()
    long_str = property(__get_long_str, __set_long_str)
    # long_str is now the property of the class.

    def _get_tree_root(self):
        """Set and get root node of the nodes"""
        d = _cal_freq(self.long_str)
        return _build_tree(
            [Node(ch=ch, fq=int(fq)) for ch, fq in d.items()])

    def _get_code_map(self):
        """Get the huffman code of file or string."""
        a_dict = {}
        _gen_huffman_code(self.root, a_dict)
        return a_dict

    def _encode(self):
        """Encode the string into huffman code.
        Very important!! Check the source code.
        """
        array_codes = array.array('B', [])
        code_length = 0
        buff, length = 0, 0

        for ch in self.long_str:
            code = self.code_map[ch]
            for bit in list(code):
                if bit == '1':
                    buff = (buff << 1) | 0x01
                else:
                    buff = buff << 1
                length += 1
                if length == MAX_BITS:
                    array_codes.extend([buff])
                    buff, length = 0, 0

            code_length += len(code)

        if length != 0:
            array_codes.extend([buff << (MAX_BITS - length)])

        return array_codes, code_length

    def encode(self, filename):
        """Open file and set long_str attribute.

        :input:
            filename: file to be opened
        :return:
            None. Just set the long_str attribute of the instance.
        """
        fp = open(filename, 'r')
        self.long_str = fp.read()
        fp.close()

    def write(self, filename):
        """Write encoded codes into a file.

        After encoding, we write the result in the name of the given name.

        :input:
            filename: filename to be assigned for the encoded code.
        :return:
            None. Files would be created.
        """
        if self._long_str:
            fcompressed = open(filename, 'wb')
            pickle.dump((self.root, self.code_length, self.array_codes), fcompressed)
            fcompressed.close()
        else:
            print("You should give me a string")


class Decoder:
    """Decoder for the huffman code."""
    def __init__(self, filename_or_bytes=None):
        """Initialize the decoder."""
        if filename_or_bytes:
            if os.path.exists(filename_or_bytes):
                filename = filename_or_bytes
                self.read(filename)
            else:
                print("Decoder got this.. {}".format(filename_or_bytes))
                raw_string = filename_or_bytes
                unpickled_root, length, array_codes = pickle.loads(raw_string)
                self.root = unpickled_root
                self.code_length = length
                self.array_codes = array.array('B', array_codes)

    def _decode(self):
        """Decode the huffman code into a normal string.

        This is also very important. You must see the source code!!
        """
        string_buf = []
        total_length = 0
        node = self.root
        for code in self.array_codes:
            buf_length = 0
            while buf_length < MAX_BITS and total_length != self.code_length:
                buf_length += 1
                total_length += 1
                if code >> (MAX_BITS - buf_length) & 1:
                    node = node.r
                    if node.c:
                        string_buf.append(node.c)
                        node = self.root
                else:
                    node = node.l
                    if node.c:
                        string_buf.append(node.c)
                        node = self.root
        return ''.join(string_buf)

    def read(self, filename):
        """Read binary encoded file.
        :input:
            filename: filename to be readed
        :return:
            None
        """
        fp = open(filename, 'rb')
        unpickled_root, length, array_codes = pickle.load(fp)
        self.root = unpickled_root
        self.code_length = length
        self.array_codes = array.array('B', array_codes)
        fp.close()

    def decode_as(self, filename):
        """Write decoded file in the name of given name.

        :input:
            filename: name to be assigned.
        """
        decoded = self._decode()
        fout = open(filename, 'w')
        fout.write(decoded)
        fout.close()
