import sys
input = sys.stdin.readline
n = int(input())

import heapq
tp = []
heapq.heapify(tp)
for k in range(n):
    for i in list(map(int,input().split())):
        heapq.heappush(tp,i)
    if k > 0:
        for _ in range(n):
            heapq.heappop(tp)

print(tp[0])
