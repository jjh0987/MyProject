import sys
import math

input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
for _ in range(n):
    w, v = map(int, input().split())
    bag.append([w, v])

dp = [[0 for _ in range(1001)] for _ in range(10001)]
for i in range(1, n + 1):
    w,v = bag[i - 1]
    for j in range(k + 1):
        if j < w:
            dp[j][i] = dp[j][i - 1]
        else:
            dp[j][i] = max(dp[j][i - 1], dp[j - w][i - 1] + v)
print(dp[k][n])