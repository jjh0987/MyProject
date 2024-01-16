import sys
import heapq
import math
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])
s,e = map(int,input().split())

que = [[0,s]]
heapq.heapify(que)
answer = [math.inf for _ in range(n+1)]
answer[s] = 0
visited = [False for _ in range(n+1)]

while que:
    tar = heapq.heappop(que)
    if visited[tar[1]]:
        continue
    visited[tar[1]] = True
    for w,u in graph[tar[1]]:
        heapq.heappush(que,[answer[tar[1]]+w,u])
        answer[u] = min(answer[tar[1]]+w,answer[u])

print(answer[e])