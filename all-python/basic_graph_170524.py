"""Basic graph implemented with class.

Next algorithm chapter is 'graph'
It's like an web, with vertices and edges.
    You can think "Vertex = node, edge = link"

I implement graph with class and basic functions like traversal.

Start date : 2017/05/24
End date   : 2017/?????
"""


# Basic implementation 1. with list
class List_graph:
    """Basic graph form implemented by list

    Throught methods, you can find variable name 'noi'
    'noi' means "Name of index", you can insert vertex's name or its number.
    """

    def __init__(self, max_number, directed=False):
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
        if isinstance(noi, str):
            try:
                noi = self._names.index(noi)
            except:
                raise IndexError("Given name is not valid")
        elif not isinstance(noi, int) or noi >= self._max_size:
            raise IndexError("noi should be a valid integer")

        return noi

    def adjacent(self, noi):
        vertices = []
        try:
            noi = self._noi_to_index(noi)
        except:
            print("Given noi is not valid")
            return

        for i in range(self._vertex_n):
            if self._graph[noi][i] == 1:
                vertices += [i]
        return vertices

    def delete_edge(self, noi1, noi2):
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
        return self._vertex_n

    def insert_vertex(self, name):
        if name in self._names:
            print("Same name is registered. Try with another name.")
            return
        if self.index == self._max_size:
            print("graph size is full. Maybe you should enlarge graph size.")
        self._names[self.index] = str(name)
        self._vertex_n += 1

    def insert_edge(self, noi1, noi2):
        changed = False
        try:
            noi1 = self._noi_to_index(noi1)
            noi2 = self._noi_to_index(noi2)
        except:
            print("Given nois are not valid. Please check")
            return
        if self._directed and not self._graph[noi1][noi2]:
            self._graph[noi1][noi2] = 1
            changed = True
        elif not self._directed and not self._graph[noi1][noi2]:
            self._graph[noi2][noi1] = 1
            self._graph[noi1][noi2] = 1
            changed = True
        if changed:
            self._edge_n += 1
        else:
            print("Edge already exsits. Return..")

    def is_empty(self):
        return True if self._vertex_n <= 0 else False

    def size_up(self, n):
        self._max_size += n
        for row in self._graph:
            row.extend([0 for _ in range(n)])
        self._graph.extend([[0 for _ in range(self._max_size)] for _ in range(n)])
