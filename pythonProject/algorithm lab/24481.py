import sys
import collections

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

d = [-1 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for node in graph[x]:
        if not visited[node]:
            dfs(node, depth + 1)


dfs(r, 0)
print(*d[1:], sep='\n')                        