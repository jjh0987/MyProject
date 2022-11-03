import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    sticker = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    for j in range(1,n-2):
        dp[0][j] = max()
        dp[1][j] =

sticker