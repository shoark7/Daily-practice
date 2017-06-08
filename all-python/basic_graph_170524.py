"""Basic graph implemented with class.

Next algorithm chapter is 'graph'
It's like an web, with vertices and edges.
    You can think "Vertex = node, edge = link"

I implement graph with class and basic functions like traversal.

Start date : 2017/05/24
End date   : 2017/05/25
"""


##### Basic implementation 1. with list
class List_graph:
    """Basic graph form implemented by list
    List has vertices and edges. Vertices are like a point or a node,
    edges are like a line.

    Throught methods, you can find variable name 'noi'
    'noi' means "Name of index", you can insert either vertex's name or its number.

    Attributes:
        _max_size : Max size of the graph
        _graph    : List implementation of the graph
        _names    : A list of vertices' names
        _directed : Bool. True : directed, False : undirected
        _vertex_n : Number of current vertices
        _edge_n   : Number of current edges between vertices
    """
    def __init__(self, max_number, directed=False, *, weight=False):
        """Initialize a graph.
        You decide the size of the graph.
        You can choose graph is either a direted or undirected graph.
        Default is an undirected graph.

        :input:
            max_number: Int. size of the graph. Should be an integer over 0.
                        You can size up the size later.
            directed  : Bool. Whether the graph is a directed or an undirected graph.
                        Default is undirected.
        """
        self.__type = "Graph"
        self._max_size = max_number
        self._graph = [[0 for _ in range(max_number)] for _ in range(max_number)]
        self._names = ['' for _ in range(max_number)]
        self._directed = directed
        self._vertex_n = 0
        self._edge_n = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} graph with {} vertices and {} edges".format(
            'A directed' if self._directed else 'An undirected', self.index, self._edge_n)

    def _noi_to_index(self, noi):
        """Change noi string form to integer
        Every vertex here has its name and its id number.
        For methods like traversal, name format should be changed to id format.
        It changes string name to id. If given noi is number format, just return it.
        If given noi is not valid, like an wrong name or wrong index, raises IndexError

        :input:
            noi: Name or Index of a vertex
        :return:
            Int. Number format of noi
        """
        if isinstance(noi, str):
            try:
                noi = self._names.index(noi)
            except:
                raise IndexError("Given name is not valid")
        elif not isinstance(noi, int) or noi >= self._max_size:
            raise IndexError("noi should be a valid integer")

        return noi

    def adjacent(self, noi):
        """Return a vertex's adjacent vertices

        With given noi,
        this method returns a list of adjacent vertices.
        Element of the list is id of vertices.

        :input:
            noi. A vertex's number noi
        :return:
            A list of adjacent vertices
        """
        vertices = []
        try:
            noi = self._noi_to_index(noi)
        except:
            print("Given noi is not valid")
            return

        for i in range(self._vertex_n):
            if self._graph[noi][i] != 0:
                vertices += [i]
        return vertices

    def delete_edge(self, noi1, noi2):
        """Delete an edge

        An edge is affiliated with 2 vertices.
        This function delete a edge between 2 vertices
        If the edge doesn't exist, nothing happenes

        :input:
            noi1
            noi2
            2 noi of vertices
        :return:
            None
        """
        changed = False
        try:
            noi1 = self._noi_to_index(noi1)
            noi2 = self._noi_to_index(noi2)
        except:
            print("Given nois are not valid. Please check")
            return
        if self._directed and not self._graph[noi1][noi2]:
            self._graph[noi1][noi2] = 0
            changed = True
        elif not self._directed and not self._graph[noi1][noi2]:
            self._graph[noi2][noi1] = 0
            self._graph[noi1][noi2] = 0
            changed = True

        if changed:
            self._edge_n -= 1
        else:
            print("Edge already doesn' exist. Return..")

    def delete_vertex(self, noi):
        """Delete a vertex in a graph

        This job is somewhat complicated.
        code checking is recommeneded

        :input:
            noi: Vertex noi to be deleted
        :return:
            None. Just delete the vertex
        """
        noi = self._noi_to_index(noi)
        self._vertex_n -= 1
        if self._directed:
            self._edge_n -= sum(self._graph[noi]) + sum(self._graph, key=lambda x: x[noi])
            if self._graph[noi][noi] == 1:
                self._edge_n += 1
        else:
            self._edge_n -= sum(self._graph[noi])
        for row in self._graph:
            row.pop(noi)
        self._graph.pop(noi)
        self._names.pop(noi)

    @property
    def index(self):
        """Number of vertices in a graph

        This is a property of _vertex_n
        I use thisn because checking vertices' number is often
        and _vertex_n is not that visual.
        You can check the number of vertices

        :input:
            None
        :return:
            Int. Number of vertices in a graph
        """
        return self._vertex_n

    def insert_vertex(self, name):
        """Insert an vertex

        My graph's vertex must have its name.
        So name is required. Also duplicate ones are not permitted.

        :input:
            name : Vertex's name. Any input will be translateed to string.
        :return:
            None. Just a new vertex is made.
        """
        if name in self._names:
            print("Same name is registered. Try with another name.")
            return
        if self.index == self._max_size:
            print("graph size is full. Maybe you should enlarge graph size.")
            return
        self._names[self.index] = str(name)
        self._vertex_n += 1

    def insert_edge(self, noi1, noi2, weight=1):
        """Insert an edge

        It's an opposite action against delete_edge
        Create an edge between 2 given nois
        If the edge exists, nothing happens

        :input:
            noi1, noi2: noi of 2 vertices
        :return:
            None
        """
        changed = False
        try:
            noi1 = self._noi_to_index(noi1)
            noi2 = self._noi_to_index(noi2)
        except:
            print("Given nois are not valid. Please check")
            return
        if self._directed and not self._graph[noi1][noi2]:
            self._graph[noi1][noi2] = weight
            changed = True
        elif not self._directed and not self._graph[noi1][noi2]:
            self._graph[noi2][noi1] = weight
            self._graph[noi1][noi2] = weight
            changed = True
        if changed:
            self._edge_n += 1
        else:
            print("Edge already exsits. Return..")

    def is_empty(self):
        """Check if the graph is empty or not

        'Empty' means it doesn't have any vertices
        Retrun True if the graph is empty. Else False

        :input:
            None
        :return:
            Bool of whether if the graph is empty or not
        """
        return True if self._vertex_n <= 0 else False

    def size_up(self, n):
        """Size up the graph's max size

        One of the demerits of using a graph with list is that 
        You cannot change the max vertex number.

        But with Python, you can size up the graph.(Please use Python)

        :input:
            n : An integer over 0. How much do you wanna bulk up?
        :return:
            None. Just size up the graph
        """
        if not isinstance(n, int) or n > 0:
            raise ValueError("Give me an integer over 0")
        self._max_size += n
        for row in self._graph:
            row.extend([0 for _ in range(n)])
        self._graph.extend([[0 for _ in range(self._max_size)] for _ in range(n)])
        self._names.extend(['' for _ in range(n)])

    def show_graph(self):
        """Show each vertex's adjacent vertices

        I wanna show you the consititution of the graph.
        An way defined here is to show every vertex' adjacent vertices
        Printed line by line

        :input:
            None
        :return:
            None. Just print the result
        """
        if not self._directed:
            for i in range(self._vertex_n):
                print("{} is connected to : ".format(self._names[i]), end='')
                vertices = self.adjacent(i)
                for j in vertices:
                    print('{} '.format(self._names[j]), end='')
                print()
        else:
            for i in range(self._vertex_n):
                print("Vertex {}".format(self._names[i]))
