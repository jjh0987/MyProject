import sys
import collections
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
h = 100
answer = [0 for _ in range(h+1)]
direction = {(1,0),(0,1),(-1,0),(0,-1)}

visited = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        que = collections.deque()
        que.append((i,j))
        while que:
            x,y = que.popleft()
            for dx,dy in direction:
                xt,yt = x+dx,y+dy