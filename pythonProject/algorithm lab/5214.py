import sys

input = sys.stdin.readline
n, k, m = map(int, input().split())
graph = {i: set() for i in range(1, n + 1)}
edge = {i: set() for i in range(m)}
for j in range(m):
    tp = set(map(int, input().split()))
    for i in tp:
        graph[i].add(j)
    edge[j] = tp

import collections

que = collections.deque([1])
visited = [False for _ in range(n + 1)]
visited[1] = True
edge_visited = [False for _ in range(m)]
answer = [0 for _ in range(n + 1)]
answer[1] = 1
while que:
    line = que.popleft()
    for i in graph[line]:
        if edge_visited[i]:
            continue
        edge_visited[i] = True
        for j in edge[i]:
            if visited[j]:
                continue
            visited[j] = True
            que.append(j)
            answer[j] = answer[line] + 1
if answer[-1] == 0:
    print(-1)
else:
    print(answer[-1])