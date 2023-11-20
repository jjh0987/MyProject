n,k = map(int,input().split())

dp = [-1]*100001
dp[n] = 0
if n == k:
    print(0)
else:
    # pop_timing = [3**i for i in range(1,20)]
    from collections import deque
    answer = deque([n])
    while 1:
        tar = answer.popleft()
        if tar == k:
            print(dp[tar])
            break
        for i in (tar*2, tar-1, tar+1):
            if i != tar*2:
                if 0 <= i <= 100000 and dp[i] == -1:
                    dp[i] = dp[tar] + 1
                    answer.append(i)
            else:
                if 0 <= i <= 100000 and dp[i] == -1:
                    dp[i] = dp[tar]
                    answer.append(i)