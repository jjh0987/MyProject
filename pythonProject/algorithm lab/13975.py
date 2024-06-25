import sys
input = sys.stdin.readline
T = int(input())

import heapq
for _ in range(T):
    K = int(input())
    target = list(map(int,input().split()))
    heapq.heapify(target)
    i = 0
    ans = 0
    while i < K-1:
        a = heapq.heappop(target)
        b = heapq.heappop(target)
        ans += a+b
        heapq.heappush(target,a+b)
        i += 1
    print(ans)
