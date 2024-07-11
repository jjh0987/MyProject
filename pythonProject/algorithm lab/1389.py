import sys

input = sys.stdin.readline
n, e = map(int, input().split())
graph = {i: set() for i in range(1, n + 1)}
for _ in range(1, e + 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

import collections

answer = []
for i in range(1, n + 1):
    que = collections.deque([i])
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    ans = [0 for _ in range(n + 1)]
    while que:
        tar = que.popleft()
        for k in graph[tar]:
            if visited[k]:
                continue
            visited[k] = True
            ans[k] = ans[tar] + 1
            que.append(k)
    answer.append(sum(ans))
m = min(answer)
for i in range(len(answer)):
    if answer[i] == m:
        print(i + 1)
        break