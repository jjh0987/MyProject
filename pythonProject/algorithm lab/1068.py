import sys

input = sys.stdin.readline
n = int(input())
target = list(map(int, input().split()))
erase = int(input())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(len(target)):
    if target[i] == -1:
        root = i
    else:
        graph[i].append(target[i])
        graph[target[i]].append(i)
answer = 0
visited = [False for _ in range(n)]


def dfs(x):
    global answer
    visited[x] = True
    leaf = 0
    for i in graph[x]:
        if not visited[i]:
            if i != erase:
                dfs(i)
                leaf += 1
    if leaf == 0:
        answer += 1


dfs(root)
if root == erase:
    print(0)
else:
    print(answer)