import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
table = [sum([sum(i) for i in graph])]
cnt = 0

while table[-1] > 0:
    que = collections.deque()
    que.append((0, 0))
    start = set()
    start.add((0, 0))
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
    while start:
        x, y = start.pop()
        for dx, dy in direction:
            xt = x + dx
            yt = y + dy
            if 0 <= xt < n and 0 <= yt < m:
                graph[xt][yt] = 0
    table.append(sum([sum(i) for i in graph]))
    cnt += 1

print(cnt)
print(table[-2]) 