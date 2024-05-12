import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for i in range(1,m+1):
        if i % nums[0] == 0:
            dp[i] += 1

    for num in nums[1:]:
        for i in range(1,m+1):
            if i >= num:
                dp[i] = dp[i-num] + dp[i]
    print(dp[-1])
