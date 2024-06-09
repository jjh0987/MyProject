import sys
import collections

input = sys.stdin.readline
n,k = map(int,input().split())
jems = [list(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jems.sort()
bags.sort()
jems = collections.deque(jems)

import heapq
h = []
heapq.heapify(h)
answer = 0
for bag in bags:
    while jems:
        m,v = jems.popleft()
        if m <= bag:
            heapq.heappush(h,-v)
        else:
            jems.appendleft([m,v])
            break
    if h:
        answer -= heapq.heappop(h)
print(answer)