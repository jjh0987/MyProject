x,y,n = 10,40,30

# dp

dp = [0 for i in range(1000001)]
dp[x] = 1

for i in range(x,y+1):
    if dp[i] != 0:
        if i%2 == 0:
            if 2*i == i-n:
                dp[i] = min(dp[2*i],dp[i+n])
        else:
            dp[i] += dp[i] + 1

        if 3*i == i+n:
            dp[i] = min(dp[3*i],dp[i+n])
        else:
            dp[i] += dp[i] + 1
        dp[n] += dp[i] + 1

dp[x:y]
dp[40]