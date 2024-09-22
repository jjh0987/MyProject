import sys
input = sys.stdin.readline
n,m = map(int,input().split())
import math
graph = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = -1

for i in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if graph[s][e] > graph[s][i]+graph[i][e]:
                graph[s][e] = -1

q = int(input())
for _ in range(q):
    s,e = map(int,input().split())
    if graph[e][s] == -1:
        print(1)
    elif graph[s][e] == -1:
        print(-1)
    else:
        print(0)