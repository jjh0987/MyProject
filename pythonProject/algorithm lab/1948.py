import sys

input = sys.stdin.readline
import collections

n = int(input())
e = int(input())
table = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
rev_table = [[] for _ in range(n + 1)]
for i in range(1, e + 1):
    a, b, t = map(int, input().split())
    table[a].append([b, t])
    indegree[b] += 1
    rev_table[b].append([a, t])
s, e = map(int, input().split())

que = collections.deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        que.append(i)
que.popleft()
answer = [0 for _ in range(n + 1)]
while que:
    tar = que.popleft()
    for b, t in table[tar]:
        indegree[b] -= 1
        answer[b] = max(answer[tar] + t, answer[b])
        if indegree[b] == 0:
            que.append(b)
print(answer[e])

visited = [False for _ in range(n + 1)]
que = collections.deque([[e, answer[e]]])
ans = 0
while que:
    e, t = que.popleft()
    for i in rev_table[e]:
        if answer[i[0]] + i[1] == answer[e]:
            ans += 1
            if not visited[i[0]]:
                visited[i[0]] = True
                que.append(i)
print(ans)
