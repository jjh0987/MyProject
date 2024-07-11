import sys
input = sys.stdin.readline
n = int(input())
mapping = [list(map(int,input().split())) for _ in range(n)]

import collections
answer = []
for i in range(n):
    visited = [False for _ in range(n)]
    ans = [0 for _ in range(n)]
    que = collections.deque([i])
    while que:
        tar = que.popleft()
        for j in range(n):
            if visited[j]:
                continue
            if mapping[tar][j] == 1:
                ans[j] = 1
                visited[j] = True
                que.append(j)
    answer.append(ans)
for i in range(n):
    print(*answer[i])