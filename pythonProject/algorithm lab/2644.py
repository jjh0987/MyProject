import sys
input = sys.stdin.readline
n = int(input())
a,b = map(int,input().split())
graph = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

answer = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            answer[i] = answer[x] + 1
            dfs(i)
dfs(a)

if answer[b] == 0:
    print(-1)
else:
    print(answer[b])