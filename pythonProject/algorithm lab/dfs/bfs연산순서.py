import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N,M,V = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
node = [sorted(i) for i in node]

visited = [False]*(N+1)
import collections
queue = collections.deque()
ans = [0]*N
cnt = 0
def bfs(x):
    global queue
    global cnt
    queue.append(x)
    visited[x] = True
    while queue:
        now_node = queue.popleft()
        if not visited[now_node]:
            ans.append(now_node)
            visited[now_node] = True
        cnt += 1
        ans[now_node-1] = cnt
        for i in node[now_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(V)
for i in ans:
    print(i)




import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N,M,V = map(int,input().split())

node = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
node = [sorted(i) for i in node]