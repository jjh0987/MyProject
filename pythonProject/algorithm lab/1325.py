import sys
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    graph[b].append(a)

import collections
def bfs(x):
    que = collections.deque([x])
    visited = [False for _ in range(v+1)]
    visited[x] = True
    cnt = 0
    while que:
        tar = que.popleft()
        for i in graph[tar]:
            if visited[i] == False:
                cnt += 1
                visited[i] = True
                que.append(i)

    return cnt
answer = [bfs(i) for i in range(v+1)]

check = max(answer)
for i in range(v+1):
    if answer[i] == check:
        print(i,end=' ')
