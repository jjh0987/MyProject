import sys
input = sys.stdin.readline
n,k = map(int,input().split())
nums = [int(input()) for _ in range(n)]
nums = sorted(list(set(nums)))

M = 100001
dp = [M for _ in range(k+1)]

for i in nums:
    for j in range(1,k//i+1):
        dp[i*j] = j

for j in nums:
    for i in range(1,k+1):
        if i > j:
            dp[i] = min(dp[i],dp[j]+dp[i-j])

if dp[-1] == M:
    print(-1)
else:
    print(dp[-1])