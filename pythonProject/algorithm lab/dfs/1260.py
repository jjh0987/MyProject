N,M,V = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
node = [sorted(i) for i in node]

visited = [False]*(N+1)
check = []

def dfs(x):
    print(x,end=' ')
    visited[x] = True
    for i in node[x]:
        if not visited[i]:
            dfs(i)
dfs(V)
print()

visited = [False]*(N+1)
import collections
queue = collections.deque()
def bfs(x):
    global queue
    queue.append(x)
    visited[x] = True
    while queue:
        now_node = queue.popleft()
        print(now_node,end=' ')
        # if not visited[now_node]:
        #     ans.append(now_node)
        #     visited[now_node] = True
        for i in node[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
bfs(V)





N,M,V = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
node = [sorted(i) for i in node]
visited = [False]*(N+1)
check = []
def dfs(x):
    ans = []
    global check
    check.append(x)
    visited[x] = True
    while check:
        now_node = check.pop()
        ans.append(now_node)
        for i in sorted(node[now_node],reverse=True):
            if not visited[i]:
                check.append(i)
                visited[i] = True
    print(*ans)
dfs(V)

visited = [False]*(N+1)
import collections
queue = collections.deque()
def bfs(x):
    ans = []
    queue.append(x)
    visited[x] = True
    while queue:
        now_node = queue.popleft()
        ans.append(now_node)
        for i in node[now_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print(*ans)
bfs(V)


