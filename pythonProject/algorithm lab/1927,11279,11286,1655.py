import heapq
import sys
input = sys.stdin.readline
n = int(input())

h = []
for _ in range(n):
    target = int(input())
    if target > 0:
        heapq.heappush(h,target)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))

# 11279
import heapq
import sys
input = sys.stdin.readline
n = int(input())

h = []
for _ in range(n):
    target = int(input())
    if target > 0:
        heapq.heappush(h,-target)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))

# 11286

import sys
import heapq
input = sys.stdin.readline
n = int(input())
min_h = []
max_h = []

for _ in range(n):
    target = int(input())
    if target > 0:
        heapq.heappush(min_h, target)
    elif target < 0:
        heapq.heappush(max_h, -target)
    else:
        if len(min_h) == 0 and len(max_h) == 0:
            print(0)
        elif len(max_h) == 0 and len(min_h) != 0:
            print(heapq.heappop(min_h))
        elif len(max_h) != 0 and len(min_h) == 0:
            print(-heapq.heappop(max_h))
        else:
            if min_h[0] == max_h[0]:
                print(-heapq.heappop(max_h))
            elif min_h[0] > max_h[0]:
                print(-heapq.heappop(max_h))
            else:
                print(heapq.heappop(min_h))

# 1655
import sys
import heapq
input = sys.stdin.readline
n = int(input())
h1 = []
h2 = []
for _ in range(n):
    target = int(input())
    heapq.heappush(h1,target)
    if len(h1) != len(h2):
        heapq.heappush(h2,-heapq.heappop(h1))
        try:
            if h1[0] < -h2[0]:
                heapq.heappush(h1, -heapq.heappop(h2))
                heapq.heappush(h2, -heapq.heappop(h1))
        except:pass
    else:
        if h1[0] < -h2[0]:
            heapq.heappush(h1,-heapq.heappop(h2))
            heapq.heappush(h2,-heapq.heappop(h1))

    print(-h2[0])