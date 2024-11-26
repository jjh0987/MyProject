import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())

def dfs(x):
    cycle.append(x)
    if not visited[x]:
        visited[x] = True
        dfs(graph[x])

for _ in range(T):
    n = int(input())
    graph = list(map(int,input().split()))
    graph = [i-1 for i in graph]
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        cycle = []
        dfs(i)
        if i == graph[i]:
            answer += 1
        elif cycle[0] == cycle[-1]:
            answer += len(cycle)-1
    print(n-answer)