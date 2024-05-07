import sys
import math
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
    dp[i][i] = 1
    dp[i][1] = i

for i in range(2, n + 1):
    for j in range(3, n + 1):
        dp[j][i] = dp[j - 1][i] + dp[j - 1][i - 1]
        dp[j][i] %= 10007
print(dp[n][k])