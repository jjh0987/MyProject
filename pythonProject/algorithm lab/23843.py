import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ipad = list(map(int,input().split()))
ipad = [-i for i in ipad]

import heapq
heapq.heapify(ipad)
consent = {i:0 for i in range(1,m+1)}

if m == 1:
    print(-sum(ipad))
else:
    while ipad:
        if consent[1] <= consent[2]:
            consent[1] += -heapq.heappop(ipad)
        for i in range(2,m+1):
            try:
                while consent[1] > consent[i]:
                    consent[i] += -heapq.heappop(ipad)
            except:pass
    print(consent[1])