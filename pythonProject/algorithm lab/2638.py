import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
table = sum([sum(i) for i in graph])
cnt = 0

while table > 0:
    que = collections.deque()
    que.append((0, 0))
    start = set()
    start.add((0, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    direction = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    while que:
        x, y = que.popleft()
        for dx, dy in direction:
            xt = x + dx
            yt = y + dy
            if 0 <= xt < n and 0 <= yt < m:
                if graph[xt][yt] == 0:
                    if (xt, yt) not in start:
                        start.add((xt, yt))
                        que.append((xt, yt))
    marker = set()
    while start:
        x, y = start.pop()
        for dx, dy in direction:
            xt = x + dx
            yt = y + dy
            if 0 <= xt < n and 0 <= yt < m:
                if graph[xt][yt] == 1:
                    visited[xt][yt] += 1
                if visited[xt][yt] >= 2:
                    graph[xt][yt] = 0
                    marker.add((xt, yt))
    while marker:
        x, y = marker.pop()
        graph[x][y] = 0
    table = sum([sum(i) for i in graph])
    cnt += 1

print(cnt)
