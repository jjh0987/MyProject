import sys
input = sys.stdin.readline
v = int(input())
e = int(input())
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
        if not visited[i] and w < 2:
            visited[i] = True
            que.append([i,w+1])

print(sum(visited)-1)