import sys
input = sys.stdin.readline
v,e = map(int,input().split())

graph = {i:[] for i in range(1,v+1)}
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(v+1)]
visited[1] = True
import collections
que = collections.deque([[1,0]])
answer = [0 for _ in range(v+1)]

while que:
    node,w = que.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            que.append([i,w+1])
            answer[i] = w+1

M = max(answer)
import math
m = math.inf
cnt = 0
for i in range(v+1):
    if answer[i] == M:
        cnt += 1
        m = min(m,i)
print(m,M,cnt)