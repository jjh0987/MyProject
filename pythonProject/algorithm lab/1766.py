import sys

input = sys.stdin.readline
import heapq
import collections

n, e = map(int, input().split())
table = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    table[a].append(b)
    indegree[b] += 1

root = []
for i in range(len(indegree)):
    if indegree[i] == 0:
        root.append(i)
root = root[1:]
heapq.heapify(root)

visited = [0 for _ in range(n + 1)]
while root:
    tar = heapq.heappop(root)
    print(tar, end=' ')
    for i in table[tar]:
        visited[i] += 1
        if visited[i] == indegree[i]:
            heapq.heappush(root, i)