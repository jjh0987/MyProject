import sys
input = sys.stdin.readline
n,m = map(int,input().split())

tar = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    tar[a].append(b)
    tar[b].append(a)


def dfs(x,depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    check[x] = True
    for i in tar[x]:
        if not check[i]:
            dfs(i,depth+1)
    check[x] = False

check = [False] * (n+1)
arrive = False
for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

