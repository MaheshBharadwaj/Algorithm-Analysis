import numpy as np

v = int(input())
e = int(input())

adjacency = np.array([[False for j in range(v)] for i in range(v)])

for edge in range(e):
    ip = tuple(map(int,input().split(' ')))
    adjacency[ip[0] - 1][ip[1] - 1] = True

for k in range(v):
    for i in range(v):
        for j in range(v):
            adjacency[i][j] = (adjacency[i][j]) or (adjacency[i][k] and adjacency[k][j])

print(adjacency)