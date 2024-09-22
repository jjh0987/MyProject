import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
import math
graph = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s][e] = min(graph[s][e], w)

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(1, n + 1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            graph[s][e] = min(graph[s][e],graph[s][i]+graph[i][e])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == math.inf:
            graph[i][j] = 0

for g in graph[1:]:
    print(*g[1:])