import sys
import heapq
import math
input = sys.stdin.readline

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])
    rev_graph[v].append([w,u])

def dj(s,graph):
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
            cost = answer[tar[1]]+w
            heapq.heappush(que,[cost,u])
            answer[u] = min(cost,answer[u])
    return answer

origin = dj(x,graph)
rev = dj(x,rev_graph)
print(max([origin[i]+rev[i] for i in range(1,len(origin))]))