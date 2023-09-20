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

