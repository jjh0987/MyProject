import sys
input = sys.stdin.readline
limit_number = 10**9
sys.setrecursionlimit(limit_number)

n,m = map(int,input().split())
check = [False]*(n+1)
node = []
for i in range(m):
    a,b = map(int, input().split())
    node.append([a,b])
    node.append([b,a])

graph = {i:[] for i in range(1,n+1)}
for i in node:
    graph[i[0]].append(i[1])

def dfs(x):
    check[x] = True
    for i in graph[x]:
        if check[i] == False:
            dfs(i)

ans = 0
for i in range(1,n+1):
    if check[i] == False:
        dfs(i)
        ans += 1
print(ans)


graph