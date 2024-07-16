import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    root, l, r = map(int, input().split())
    graph[root].append(l)
    graph[root].append(r)

cnt = 0
root = 1
while 1:
    tar = graph[root][1]
    if tar == -1:
        break
    root = graph[root][1]
    cnt += 1

ans = 0
for tp in graph[1:]:
    l, r = tp
    if l > 0:
        ans += 2
    if r > 0:
        ans += 2
print(ans - cnt)