import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

import collections
que = collections.deque()
que.append((0,0))
flag = False
while que:
    x,y = que.popleft()
    if x < 0 or x >= n or y < 0 or y >= n:
        continue
    if not visited[x][y]:
        if x == n-1 and y == n-1:
            flag = True
            break
        visited[x][y] = True
        que.append((x+graph[x][y],y))
        que.append((x,y+graph[x][y]))

if flag:
    print('HaruHaru')
else:
    print('Hing')