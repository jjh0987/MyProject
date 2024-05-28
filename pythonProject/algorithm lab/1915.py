import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dp = []
for _ in range(n):
    dp.append(list(map(int,input().rstrip('\n'))))
for i in range(1,n):
    for j in range(1,m):
        if dp[i][j] == 0:
            continue
        dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
print(max([max(i) for i in dp])**2)