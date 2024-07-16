import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    i, j, v = map(int, input().split())
    graph[i].append([j, v])
    graph[j].append([i, v])

import collections

for _ in range(m):
    s, e = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    que = collections.deque(graph[s])
    while que:
        i, v1 = que.popleft()
        visited[i] = True
        if i == e:
            break
        for j, v2 in graph[i]:
            if visited[j]:
                continue
            que.append([j, v1 + v2])
    print(v1)