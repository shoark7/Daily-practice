"""
Draw a one dimensional line of 'y = x + a' with print function.
Input:
    size: Total size of graph. If size = 3, graph range would be -3 to 3.
    a   : Intercept.
Output : 1D line of 'y = x +a'.
         Empty spaces are '.', axises are either '|' or '-',
         (0,0) is drawn into '+'. Line character '/' overlaps the existing points.
"""

def draw_graph(size, a):

    # Make all spaces '.'
    graph = [['.' for one in range(2*size+1)]for row in range(2*size+1)]

    # Draw a y-axis.
    for row in graph:
        row[size] = '|'

    # Draw a x-axis.
    graph[size] = ['-' for i in range(len(graph))]

    # Draw (0,0) point symbol.
    graph[size][size] = '+'

    # Draw a line. If x range goes over the graph, don't draw.
    for i in range(size*2+1):
        if 2*size-i-a >= 0:
            graph[i][2*size-i-a] = '/'
        else:
            pass

    # Type of our graph is 'list'. We beautify it by making it 'string' format and print it.
    beautified_graph = '\n'.join([' '.join(row) for row in graph])

    print(beautified_graph)

draw_graph(3,1)
draw_graph(3,0)
draw_graph(3,5)

"""
results are :

. . . | . . /
. . . | . / .
. . . | / . .
- - - / - - -
. . / | . . .
. / . | . . .
/ . . | . . .

"""