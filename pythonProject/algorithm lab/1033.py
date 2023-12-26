n = int(input())
graph = [[] for _ in range(n)]

def gcd(a,b):
    x,y = divmod(a,b)
    if y == 0:
        return b
    else:
        return gcd(b,y)

base = 1
for _ in range(n-1):
    a,b,p,q = map(int,input().split())
    graph[a].append([b,[p,q]])
    graph[b].append([a,[q,p]])
    base *= p*q

answer = [base for _ in range(n)]
visited = [False for _ in range(n)]

def dfs(x):
    visited[x] = True
    for node,w in graph[x]:
        if not visited[node]:
            p,q = w[0],w[1]
            answer[node] = answer[x]*q//p
            dfs(node)
dfs(0)

mgcd = answer[0]
for i in range(1,n):
    mgcd = gcd(mgcd,answer[i])


print(*[i//mgcd for i in answer])