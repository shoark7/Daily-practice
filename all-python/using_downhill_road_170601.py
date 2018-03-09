"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

answer : 3
"""

row, column = (int(n) for n in input().split())
cache = [[0 for _ in range(column+1)]]

for _ in range(row):
    cache.append([[0 for _ in range(column+1)]])

for r in range(1, row + 1):
    for c in range(1, column + 1):
        cache[r][c] += 1 if cache[r-1][c] > cache[r][c] else 0
        cache[r][c] += 1 if cache[r][c-1] > cache[r][c] else 0


def hi():
    pass
