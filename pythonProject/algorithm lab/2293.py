import sys
input = sys.stdin.readline
n,k = map(int,input().split())
nums = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in range(1,k+1):
    if i%nums[0] == 0:
        dp[i] = 1

for num in nums[1:]:
    for i in range(num,k+1):
        dp[i] = dp[i] + dp[i-num]
dp[0] = 0
print(dp[-1])