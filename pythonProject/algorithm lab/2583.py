import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    s1,e1,s2,e2 = map(int,input().split())
    for i in range(e1,e2):
        for j in range(s1,s2):
            graph[i][j] = 1

import collections
answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        que = collections.deque()
        que.append((i,j))
        ans = 0
        while que:
            s,e = que.popleft()
            if s < 0 or s >= n or e < 0 or e >= m:
                continue
            if graph[s][e] == 0:
                graph[s][e] = 1
                ans += 1
                que.append((s-1,e))
                que.append((s,e+1))
                que.append((s+1,e))
                que.append((s,e-1))
        answer.append(ans)

print(len(answer))
print(*sorted(answer))
