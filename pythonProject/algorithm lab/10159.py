import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
left_graph = [[] for _ in range(n+1)]
right_graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    left_graph[s].append(e)
    right_graph[e].append(s)

answer = [n-1 for _ in range(n+1)]
import collections
for root in range(1,n+1):
    que = collections.deque()
    visited = [False for _ in range(n+1)]
    que.append(root)
    visited[root] = True
    cnt = 0
    while que:
        tar = que.popleft()
        for i in left_graph[tar]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    visited = [False for _ in range(n+1)]
    que.append(root)
    visited[root] = True
    while que:
        tar = que.popleft()
        for i in right_graph[tar]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    answer[root] -= cnt
print(*answer[1:],sep='\n')




import sys
input = sys.stdin.readline
n,m = map(int,input().split())
left_graph = [[] for _ in range(n+1)]
right_graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    left_graph[s].append(e)
    right_graph[e].append(s)

answer = [n-1 for _ in range(n+1)]
import collections
for root in range(1,n+1):
    que = collections.deque()
    visited = [False for _ in range(n+1)]
    que.append(root)
    visited[root] = True
    cnt = 0
    while que:
        tar = que.popleft()
        for i in left_graph[tar]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    visited = [False for _ in range(n+1)]
    que.append(root)
    visited[root] = True
    while que:
        tar = que.popleft()
        for i in right_graph[tar]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    answer[root] -= cnt
print(len([i for i in answer if i == 0]))