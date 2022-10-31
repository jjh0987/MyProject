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
import collections
queue = collections.deque()
ans = [-1]*N
def bfs(x):
    global queue
    queue.append(x)
    visited[x] = True
    depth = 0
    ans[x-1] = depth
    while queue:
        now_node = queue.popleft()
        for i in node[now_node]:
            if not visited[i]:
                ans[i-1] = ans[now_node-1]+1
                queue.append(i)
                visited[i] = True

bfs(V)
for i in ans:
    print(i)