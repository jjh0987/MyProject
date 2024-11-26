import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,r,q = map(int,input().split())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

subtree_size = [0] * (n + 1)
def dfs(node):
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if subtree_size[neighbor] == 0:
            subtree_size[node] += dfs(neighbor)
    return subtree_size[node]

dfs(r)

for _ in range(q):
    query = int(input())
    print(subtree_size[query])







import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())

n = int(input())
graph = list(map(int,input().split()))
graph = [i-1 for i in graph]
for i in range(n):
    if i == graph[i]:
        graph[i] = -1

visited = [0 for _ in range(n+1)]
def dfs(x):
    global s
    global cnt
    global flag
    global cycle
    print(x)
    if visited[x] == 2:
        return
    visited[x] += 1
    if graph[x] == -1:
        return
    elif s != graph[x]:
        dfs(graph[x])

dfs(6)

cycle = set()
for i in range(n):
    cnt = 0
    s = int(i)
    flag = False
    dfs(s)
    if flag:
        print(cnt,'hi')
    print()
