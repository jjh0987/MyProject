n = int(input())
dp = [0 for _ in range(50)]
dp[0] = 0
dp[1] = 1
for i in range(2,50):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])