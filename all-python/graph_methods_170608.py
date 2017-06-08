"""Spanning tree, graph traversal methods using graph




"""


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


if __name__ == '__main__':
    g = List_graph(10)
    for i in range(7):
        g.insert_vertex(chr(i+65))
    g.insert_edge('A', 'B')
    g.insert_edge('A', 'C')
    g.insert_edge('B', 'D')
    g.insert_edge('B', 'E')
    g.insert_edge('C', 'E')
    g.insert_edge('D', 'G')
    g.insert_edge('E', 'G')
    g.insert_edge('F', 'G')

    breadth_first_search(g, 'A')
    print(is_cycle(g, 'A', 'E'))
    print()
