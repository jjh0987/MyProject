import sys
import collections
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
T,pos_x,pos_y = map(int,input().split())

pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            pos.append((graph[i][j],0,i,j))
pos.sort()
pos = collections.deque(pos)
dir = [(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(T):
    length = len(pos)
    for _ in range(length):
        v,t,x,y = pos.popleft()
        for dx,dy in dir:
            xt,yt = x+dx,y+dy
            if 0 <= xt < n and 0 <= yt < n:
                if graph[xt][yt] == 0:
                    graph[xt][yt] = v
                    pos.append((v,t+1,xt,yt))

print(graph[pos_x-1][pos_y-1])
