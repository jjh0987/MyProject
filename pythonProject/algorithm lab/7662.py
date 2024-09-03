import sys
input = sys.stdin.readline
n = int(input())

import heapq
for _ in range(n):
    h_min = []
    h_max = []
    heapq.heapify(h_min)
    heapq.heapify(h_max)
    m = int(input())
    for _ in range(m):
        q,v = input().split()
        v = int(v)
        if q == 'I':
            heapq.heappush(h_min,v)
            heapq.heappush(h_max,-v)
        elif q == 'D' and v == -1:
            if h_min:
                heapq.heappop(h_min)
        elif q == 'D' and v == 1:
            if h_max:
                heapq.heappop(h_max)
        print(h_min)
        print(h_max)
    h_min = set(h_min)
    h_max = set(h_max)
    h = h_min.intersection([-i for i in h_max])
    h = list(h)
    h.sort()

    if len(h) == 0:
        print('EMPTY')
    elif len(h) == 1:
        print(h[0],h[0])
    else:
        print(h[-1],h[0])