n,k = map(int,input().split())

dp = [0]*100001
if n == k:
    print(0)
else:
    pop_timing = [3**i for i in range(1,20)]
    from collections import deque
    answer = deque([n])
    while 1:
        tar = answer.popleft()
        if tar == k:
            print(dp[tar])
            break
        for i in (tar-1, tar+1, tar*2):
            if 0 <= i <= 100000 and dp[i] == 0:
                dp[i] = dp[tar] + 1
                answer.append(i)

import sys
input = sys.stdin.readline
n,s = map(int,input().split())
tar = list(map(int,input().split()))

presum = [0 for _ in range(len(tar)+1)]
presum[1] = tar[0]
for i in range(1,len(tar)+1):
    presum[i] = presum[i-1] + tar[i-1]

i = 0
j = 0
answer = []
while i < len(tar)+1:
    if presum[i] - presum[j] < s:
        i += 1
    else:
        while 1:
            if presum[i] - presum[j] < s:
                break
            answer.append(i-j)
            j += 1
if answer:
    print(min(answer))
else:
    print(0)


