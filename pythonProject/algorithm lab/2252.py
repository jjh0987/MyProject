import sys

input = sys.stdin.readline
import collections

n, e = map(int, input().split())
table = [[] for i in range(n + 1)]  # 인접
indegree = [0 for _ in range(n + 1)]  # 진입차수
que = collections.deque()

for _ in range(e):
    a, b = map(int, input().split())
    table[a].append(b)
    indegree[b] += 1

for i in range(len(indegree)):
    if indegree[i] == 0:
        que.append(i)

que.popleft()
while que:
    tar = que.popleft()
    print(tar, end=' ')
    for i in table[tar]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)