import sys
input = sys.stdin.readline
n,k = map(int,input().split())

h = []
for i in range(n):
    w,v = map(int,input().split())
    h.append([w,-v])

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
dp = [0 for _ in range(100001)]
wkey = set()
for _ in range(n):
    w,v = map(int,input().split())
    wkey.add(w)
    if dp[w] > 0:
        dp[w] = max(dp[w],v)
    else:
        dp[w] = v

for i in range(len(wkey)):
    wkey = list(set(wkey))
    wkey.sort()
    for j in range(i,len(wkey)):
        if i == j:
            continue
        w1 = wkey[i]
        w2 = wkey[j]
        if w1+w2 > k:
            continue
        dp[w1+w2] = max(dp[w1+w2],dp[w1]+dp[w2])
        wkey.append(w1+w2)
print(dp[k])



import sys
input = sys.stdin.readline
n,k = map(int,input().split())
dp = [[0 for i in range(101)] for _ in range(100001)]
h = []
for i in range(n):
    w,v = map(int,input().split())
    h.append([w,v])

