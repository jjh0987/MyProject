import sys
input = sys.stdin.readline
n,k = map(int,input().split())

h = []
for i in range(n):
    w,v = map(int,input().split())
    h.append([w,-v,i])

import heapq
heapq.heapify(h)

m = 0
val = 0
bag = []
heapq.heapify(bag)
ans = []
while h:
    w,v = heapq.heappop(h)
    v = -v
    if w > k:
        break
    m += w
    val += v
    if m <= k:
        heapq.heappush(bag,[w,v])
        ans.append(val)
    else:
        while m > k:
            x,y = heapq.heappop(bag)
            x = -x
            m -= x
            val -= y
        heapq.heappush(bag,[-w,v])
        ans.append(val)
print(max(ans))





import sys
input = sys.stdin.readline
n,k = map(int,input().split())
dp = [0 for _ in range(100001*2)]
bag = []
for _ in range(n):
    w,v = map(int,input().split())
    bag.append([w,v])
    if dp[w] > 0:
        dp[w] = max(dp[m],v)
    else:
        dp[w] = v


