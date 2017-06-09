"""Methods using graph data types

This file contains several functions using graph data types.
Graph is from my previous file, basic_graph_170524.py which implements 'graph'.

This file will be updated more with my skills improving.

** Remember, this functions only work for my custom graph data type! **

Until now, this file contains..

    is_cycle :
        Check if subgraph of the original graph is cycle or not. ** NOT WORKING **
    depth_first_search :
        Depth first search. It uses recursive call.
    breadth_first_search:
        breadth first search. It uses custom _Queue class
    _Queue :
        Helper class for breadth_first_search
    shortest_path_dijkstra :
        Dijkstra algorithm finding shortest path from A to B
    tsp_backtracking :
        Traveling Salesman Problem using back tracking algorithm.

Start Date : 2017/06/08
End Date   : 2017/06/09
"""

import math
from basic_graph_170524 import List_graph  # my custom graph for graph type


############ NOT WORKING. NEED FIX ###############
def is_cycle(graph, out_v, in_v):
    """Check if subgraph of a graph is a cycle or not

    :input:
        graph: Target graph.
        out_v: Start point of a subgraph.
        in_v : End point of a subgraphj
    :return:
        Bool. Whether subgraph is a cycle or not
    """
    try:
        out_v = graph._noi_to_index(out_v)
        # This method changes vertex's name to index of a graph
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
    """Depth first search algorithm with recursive call

    DFS can be done with 2 ways: stack & recursive call.
    I used recursive call because I didn't want to implement queue once again..
    This traversal prints vertex's name it visits.

    :input:
        graph : Target graph.
        noi   : Name or index to search from
    :return:
        None. Just print out the vertices
    """
    try:
        noi = graph._noi_to_index(noi)
    except IndexError as e:
        print('Given index sucks')
        return
    visited = [0 for _ in range(graph.index)]

    def search(graph, noi):
        """Recursive call function for searching"""

        visited[noi] = 1
        print('{} '.format(graph._names[noi]), end='')
        adja = graph.adjacent(noi)
        for n in adja:
            if visited[n] == 0:
                search(graph, n)
    search(graph, noi)


def breadth_first_search(graph, noi):
    """Breadth first search algorithm with queue data type

    This search algorithm uses my helper data type _Queue.
    This also prints out vertices it visits

    :input:
        graph : Target graph.
        noi   : Name or index to search from
    :return:
        None. Just print out the vertices
    """
    visited = [0 for _ in range(graph.index)]
    queue = _Queue(graph.index ** 2)

    def search(graph, noi):
        """Traversal function using _Queue"""
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

    Its name starts with '_' because it is focusted to help BFS,
    not to be used in other ways.

    This is basically ring buffer, with given max size
    """
    def __init__(self, max_size=100):
        """Initialize a Queue

        :input:
            max_size : Max length of the queue. Default is 100
        :return:
            The queue
        """
        self._queue = [0 for _ in range(max_size)]
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self, value):
        """Enqueue a value"""
        if self.length == self.max_size:
            raise IndexError("No more push is allowed")

        self._queue[self.tail] = value
        self.tail += 1
        self.tail %= self.max_size
        self.length += 1

    def dequeue(self):
        """Dequeue a value"""
        if self.length <= 0:
            raise IndexError("No value inside")

        answer = self._queue[self.head]
        self.head += 1
        self.head %= self.max_size
        self.length -= 1

        return answer

    def is_empty(self):
        """Check if the queue is empty

        :input:
            None
        :return:
            Bool. If the queue is empty or not
        """
        return True if self.length == 0 else False


def shortest_path_dijkstra(graph, start, end):
    """Find a shortest path from vertex A to B

    This is a basic dijkstra algorithm in Python

    :input:
        start: Start point of a graph
        end  : End point of a graph
    """
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
        """Return fixed vertices of a path"""
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


def tsp_backtracking(graph, noi):
    """Traveling Salesman Problem algorithm using backtracking

    This function is my first try using backtracking algorithm
    Code means a lot to me. I learned a lot.

    :input:
        noi: A name or an index of vertex that starts
    :return:
        None. This funtions prints 1. Best route and 2. its distance
    """
    try:
        noi = graph._noi_to_index(noi)
    except:
        raise ValueError("Graph doesn't have that vertex")

    tour_route_trigger = [noi]
    best_solution = (tour_route_trigger, math.inf)

    def is_route_complete(tour_route):
        """Helper function that checks if given route is complete or not

        Backtracking method checks every possible route it encounters.
        This function checks if given route is complete or need more vertices.
        It checks 3 things.
            1. First element of vertex is given noi
            2. Last element of vertex is given noi
            3. Length of the route == to length of the graph + 1
               Because TSP returns to the starting point with visiting all other vertices once

        :input:
            tour_route : A list containing vertices. It is a part of a complete route
        :return:
            Bool. Whether the route is complete or not
        """
        return True if tour_route[0] == noi \
                    and tour_route[-1] == noi \
                    and len(tour_route) == graph.index + 1 else False

    def search(tour_route, distance):
        """Search and try all possible routes using recursive call

        This code is very core of the algorithm
        It searches every possible routes that can be made.

        Try a look at the code.
        Also it uses nonlocal for the first time of my life
        If you don't know why nonlocal is used, contact me

        :input:
            tour_route : Tour route. It can be tested or used to add more vertices
            distance   : Temporary distance of the given tour route.
        :return:
            None. Just set the best solution
        """
        nonlocal best_solution

        if is_route_complete(tour_route):
            if distance < best_solution[1]:
                best_solution = (tour_route, distance)
        else:
            last_one = tour_route[-1]
            near_vertices = graph.adjacent(last_one)
            for v in near_vertices:
                if (v == noi and len(tour_route) == graph.index) or v not in tour_route:
                    new_tour = tour_route + [v]
                    new_distance = distance + graph._graph[last_one][v]
                    if new_distance < best_solution[1]:
                        search(new_tour, new_distance)
    search(tour_route_trigger, noi)

    print('Best route is ', end='')
    for v in best_solution[0]:
        print(graph._names[v], end=' ')
    print('\nLeast distance is {}'.format(best_solution[1]))


# Test code!!
if __name__ == '__main__':
    g = List_graph(10, False, weight=True)
    # For shortest_path_dijkstra
    """
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
    """

    # For tsp_backtracking
    for i in range(5):
        g.insert_vertex(chr(i+65))

    g.insert_edge('A', 'B', 2)
    g.insert_edge('A', 'C', 7)
    g.insert_edge('A', 'D', 3)
    g.insert_edge('A', 'E', 10)
    g.insert_edge('B', 'C', 3)
    g.insert_edge('B', 'D', 5)
    g.insert_edge('B', 'E', 4)
    g.insert_edge('C', 'D', 6)
    g.insert_edge('C', 'E', 1)
    g.insert_edge('D', 'E', 9)

    tsp_backtracking(g, 'A')
