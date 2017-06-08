"""Spanning tree, graph traversal methods using graph




"""

import math
from basic_graph_170524 import List_graph


def is_cycle(graph, out_v, in_v):
    try:
        out_v = graph._noi_to_index(out_v)
        in_v = graph._noi_to_index(in_v)
    except IndexError as e:
        print('Given index sucks')
        return
    visited = [0 for _ in range(graph.index)]
    noi = out_v
    before = out_v

    def search(graph, before, noi):
        visited[noi] = 1
        adja = graph.adjacent(noi)
        for n in adja:
            if n == out_v and n != before and visited[in_v] == 1:
                return True
            if visited[n] == 0:
                before = n
                search(graph, before, n)
        return False
    return search(graph, before, noi)


def depth_first_search(graph, noi):
    try:
        noi = graph._noi_to_index(noi)
    except IndexError as e:
        print('Given index sucks')
        return
    visited = [0 for _ in range(graph.index)]

    def search(graph, noi):

        visited[noi] = 1
        print('{} '.format(graph._names[noi]), end='')
        adja = graph.adjacent(noi)
        for n in adja:
            if visited[n] == 0:
                search(graph, n)
    search(graph, noi)


def breadth_first_search(graph, noi):
    visited = [0 for _ in range(graph.index)]
    queue = _Queue(graph.index ** 2)

    def search(graph, noi):
        try:
            noi = graph._noi_to_index(noi)
        except:
            print('Given index sucks')
            return

        queue.enqueue(noi)

        while not queue.is_empty():
            l = queue.dequeue()
            if visited[l] == 0:
                print('{} '.format(graph._names[l]), end='')
                visited[l] = 1
                adj = graph.adjacent(l)
                for n in adj:
                    if visited[n] == 0:
                        queue.enqueue(n)
    search(graph, noi)


class _Queue:
    """Queue data type for Breadth Frist Search


    """
    def __init__(self, max_size=100):
        self._queue = [0 for _ in range(max_size)]
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self, value):
        if self.length == self.max_size:
            raise IndexError("No more push is allowed")

        self._queue[self.tail] = value
        self.tail += 1
        self.tail %= self.max_size
        self.length += 1

    def dequeue(self):
        if self.length <= 0:
            raise IndexError("No value inside")

        answer = self._queue[self.head]
        self.head += 1
        self.head %= self.max_size
        self.length -= 1

        return answer

    def is_empty(self):
        return True if self.length == 0 else False


def shortest_path_dijkstra(graph, start, end):
    try:
        start = graph._noi_to_index(start)
        end = graph._noi_to_index(end)
    except:
        raise IndexError("You gave wrong names")

    distances = [math.inf for _ in range(graph.index)]
    distances[start] = 0
    checked = [0 for _ in range(graph.index)]
    checked[start] = 1

    def get_checked_vertices():
        return [i for i, n in enumerate(checked) if n == 1]

    for i in range(graph.index-1):
        checked_vertices = get_checked_vertices()
        temp_index = 0
        temp_dist = math.inf
        for v in checked_vertices:
            neighbors = graph.adjacent(v)
            for neighbor in neighbors:
                if distances[v] + graph._graph[v][neighbor] < temp_dist and checked[neighbor] == 0:
                    temp_dist = distances[v] + graph._graph[v][neighbor]
                    temp_index = neighbor
        distances[temp_index] = temp_dist
        checked[temp_index] = 1
    return distances[end]


if __name__ == '__main__':
    g = List_graph(10, False, weight=False)
    for i in range(10):
        g.insert_vertex(chr(i+65))
    g.insert_edge('A', 'B', 15)
    g.insert_edge('A', 'D', 12)
    g.insert_edge('B', 'C', 21)
    g.insert_edge('B', 'G', 7)
    g.insert_edge('C', 'H', 25)
    g.insert_edge('D', 'F', 10)
    g.insert_edge('D', 'E', 4)
    g.insert_edge('E', 'F', 3)
    g.insert_edge('E', 'I', 13)
    g.insert_edge('F', 'G', 10)
    g.insert_edge('G', 'H', 19)
    g.insert_edge('G', 'J', 9)
    g.insert_edge('I', 'J', 15)
    g.insert_edge('J', 'H', 15)

    print(shortest_path_dijkstra(g, 'A', 'J'))
    print(shortest_path_dijkstra(g, 'A', 'G'))
    print(shortest_path_dijkstra(g, 'A', 'H'))
    print(shortest_path_dijkstra(g, 'A', 'I'))
    print(shortest_path_dijkstra(g, 'A', 'B'))
