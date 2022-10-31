import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,V = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
node = [sorted(i,reverse=True) for i in node]

visited = [False]*(N+1)
check = []
ans = [0]*N
cnt = 0
def dfs(x):
    global cnt
    cnt += 1
    ans[x-1] = cnt
    visited[x] = True
    for i in node[x]:
        if not visited[i]:
            dfs(i)
dfs(V)
for i in ans:
    print(i)