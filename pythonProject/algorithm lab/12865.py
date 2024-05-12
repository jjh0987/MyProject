import sys
import math

input = sys.stdin.readline

k,n = map(int, input().split())
bag = []
for _ in range(n):
    v, w = map(int, input().split())
    bag.append([v, w])
dp = [[math.inf for _ in range(21)] for _ in range(1001)]
v,w = bag[0]
for j in range(k+1):
    dp[j][1] = v*(j//w)

for i in range(1, n + 1):
    v, w = bag[i - 1]
    for j in range(k + 1):
        dp[j][i] = min(dp[j][i - 1], dp[j-w*(j//w)][i] + v*(j//w))
print(dp[k][n])

for i in range(k+1):
    print(dp[i][:10])




import sys
import math
input = sys.stdin.readline
k,n = map(int, input().split())
bag = []
for _ in range(n):
    v, w = map(int, input().split())
    bag.append([v, w])

dp = [math.inf for _ in range(k+101)]
dp[0] = 0
for v,w in bag:
    for i in range(w,k+101):
        if i > w:
            dp[i] = min(dp[i],dp[i-w]+v)
        else:
            dp[i] = min(dp[i],v*(i//w))
print(min(dp[k:]))