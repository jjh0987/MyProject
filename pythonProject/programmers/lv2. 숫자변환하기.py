x,y,n = 10,40,30

# dp
dp = [float('inf') for i in range(1000001)]
dp[x] = 0

for i in range(x+1,y+1):
    if i%3 == 0:
        dp[i] = min(dp[int(i/3)]+1,dp[i-n]+1,dp[i]+1)
    elif i%2 == 0:
        dp[i] = min(dp[int(i/2)]+1,dp[i-n]+1,dp[i]+1)

dp[x:y+1]
dp[40]

min(dp[10],100)