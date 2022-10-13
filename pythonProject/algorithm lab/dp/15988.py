


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)
for _ in range(n):
    print(sol(int(input()))%1000000009)


import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*10000
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3,10000):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]-3

for _ in range(n):
    print(dp[int(input())-1])

