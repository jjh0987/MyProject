import sys
input = sys.stdin.readline
n = int(input())

import heapq
time = []
heapq.heapify(time)
for _ in range(n):
    d,c = map(int,input().split())
    heapq.heappush(time,(-d,-c))

dt = max([-i[0] for i in time])
tp = []
heapq.heapify(tp)
answer = 0
while dt > 0:
    while time:
        d,c = heapq.heappop(time)
        d = -d
        c = -c
        if d < dt:
            heapq.heappush(time,(-d,-c))
            break
        heapq.heappush(tp,-c)
    if tp:
        answer -= heapq.heappop(tp)
    dt -= 1
print(answer)