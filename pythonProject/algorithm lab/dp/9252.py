a = input()
b = input()

d = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

print(d[len(a)][len(b)])


tar1 = d[-1]
tar2 = [d[i][len(b)] for i in range(len(b)+1)]
if sum(tar1) <= sum(tar2):
    tar = tar2
    flag = 1
else:
    tar = tar1
    flag = 0

ans = ''

for i in range(1,len(a)+1):
    if tar[i] - tar[i-1] > 0 and flag == 0:
        ans += b[i-1]
    if tar[i] - tar[i-1] > 0 and flag == 1:
        ans += a[i-1]
if ans:
    print(ans)


import sys
input = sys.stdin.readline

A,B = "-"+input().rstrip(),"-"+input().rstrip()
dp = [[0]*(len(A)) for _ in range(len(B))]

for i in range(1,len(B)):
    for j in range(1,len(A)):
        if A[j] == B[i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])

i,j = len(B)-1,len(A)-1
ans = ""
while i>0 and j>0:
    if dp[i][j] == dp[i][j-1]:
        j-=1
    elif dp[i][j] == dp[i-1][j]:
        i-=1
    else:
        ans = A[j] + ans
        i-=1; j-=1
if ans:
    print(ans)
