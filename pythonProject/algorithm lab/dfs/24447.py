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
ans1 = [-1]*N
ans2 = [0]*N

cnt = 0

def bfs(x):
    global queue
    global cnt
    queue.append(x)
    visited[x] = True
    depth = 0
    ans1[x-1] = depth
    while queue:
        now_node = queue.popleft()
        cnt += 1
        ans2[now_node-1] = cnt # operation time
        for i in node[now_node]:
            if not visited[i]:
                ans1[i-1] = ans1[now_node-1]+1 # depth
                queue.append(i)
                visited[i] = True

bfs(V)
ans = 0
for i in range(len(ans1)):
    ans += ans1[i]*ans2[i]
print(ans)