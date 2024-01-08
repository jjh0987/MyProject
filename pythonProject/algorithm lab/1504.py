import sys
import heapq
import math
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])
    graph[v].append([w,u])
v1,v2 = map(int,input().split())

def dj(s):
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
    return answer

origin = dj(1)
path_v1 = dj(v1)
path_v2 = dj(v2)

ans1 = origin[v1] + path_v1[v2] + path_v2[n]
ans2 = origin[v2] + path_v2[v1] + path_v1[n]
ans = min(ans1,ans2)
if ans < math.inf:
    print(ans)
else:
    print(-1)