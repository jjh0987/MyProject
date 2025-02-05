import sys
input = sys.stdin.readline

n,d = map(int,input().split())
fast = [tuple(map(int,input().rstrip('\n').split())) for _ in range(n)]
fast.sort()
dp = [i for i in range(d+1)]
for s,e,l in fast:
    try:
        if dp[e] > dp[s]+l:
            dp[e] = dp[s]+l
            for i in range(e+1,d+1):
                dp[i] = min(dp[i],dp[i-1]+1)
    except:pass
print(dp[-1])            