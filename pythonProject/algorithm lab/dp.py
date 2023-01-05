# 1149
import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int,input().split())) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]
dp[0] = house[0]
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + house[i][2]
print(min(dp[-1]))



n = int(input())
start = []
if n%3 == 0:
    start.append(int(n/3))
if n%2 == 0:
    start.append(int(n/2))
start.append(n-1)

def solution(x):
    cnt = 1
    tp = [n,x]
    while x > 1:
        if x%3 == 0:
            x = int(x/3)
        elif x%2 == 0:
            x = int(x/2)
        else:
            x -= 1
        tp.append(x)
        cnt += 1
    return cnt, tp

ans = []
for i in start:
    ans.append(solution(i))
print(min([i[0] for i in ans]))
print(*ans[[i[0] for i in ans].index(min([i[0] for i in ans]))][1])