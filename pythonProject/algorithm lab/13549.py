from collections import deque

n, k = map(int, input().split())
dp = [-1] * 100001
dp[n] = 0
if n == k:
    print(0)
else:
    answer = deque([n])
    while answer:
        tar = answer.popleft()
        if tar == k:
            print(dp[tar])
            break
        for i in (tar * 2, tar - 1, tar + 1):
            if 0 <= i <= 100000:
                if i == tar * 2:
                    if dp[i] == -1:
                        dp[i] = dp[tar]
                        answer.append(i)
                    else:
                        dp[i] = min(dp[i], dp[tar])
                else:
                    if dp[i] == -1:
                        dp[i] = dp[tar] + 1
                        answer.append(i)

