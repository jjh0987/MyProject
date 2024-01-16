import sys
input = sys.stdin.readline
n,k = map(int,input().split())
jem = []
bag = []
import heapq
import collections
heapq.heapify(jem)

for _ in range(n):
    m,v = map(int,input().split())
    heapq.heappush(jem,[m,-v])
for _ in range(k):
    bag.append(int(input()))
bag.sort()

answer = 0
i = 0
j = 0
while i < k:
    m,v = heapq.heappop(jem)
    while j < len(bag):
        b = bag[j]
        if m <= b:
            j += 1
            answer -= v
            break
        j += 1
    i += 1
print(answer)