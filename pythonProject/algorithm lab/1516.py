import sys

input = sys.stdin.readline
import collections

n = int(input())
table = [[] for i in range(n + 1)]  # 인접
indegree = [0 for _ in range(n + 1)]  # 진입차수
tt = [0 for _ in range(n + 1)]
que = collections.deque()

for i in range(1, n + 1):
    target = list(map(int, input().split()))
    tt[i] = target[0]
    for tp in target[1:]:
        if tp > 0:
            indegree[i] += 1
            table[tp].append(i)

for i in range(len(indegree)):
    if indegree[i] == 0:
        que.append(i)
que.popleft()

answer = [0 for _ in range(n + 1)]
while que:
    tar = que.popleft()
    for i in table[tar]:
        answer[i] = max(answer[i], answer[tar] + tt[tar])
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)

[print(answer[i] + tt[i]) for i in range(1, len(answer))]