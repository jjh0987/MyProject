n,k = map(int,input().split())

dp = [-1]*100001
dp[n] = 0
cnt = 0
if n == k:
    print(0)
    print(1)
else:
    from collections import deque
    answer = deque([n])
    while answer:
        tar = answer.popleft()
        if tar == k:
            print(dp[tar])
            break
        for i in (tar-1, tar+1, tar*2):
            if 0 <= i <= 100000 and dp[i] == -1:
                dp[i] = dp[tar] + 1
                answer.append(i)

    min_iter = dp[k]
    que = deque([k])
    while min_iter > 0:
        min_iter -= 1
        tp = []
        while que:
            tar = que.popleft()
            if tar%2 == 0:
                for i in (tar+1,tar-1,int(tar/2)):
                    if 0 <= i <= 100000:
                        if dp[i] == min_iter:
                            tp.append(i)
            else:
                for i in (tar+1,tar-1):
                    if 0 <= i <= 100000:
                        if dp[i] == min_iter:
                            tp.append(i)
        que.extend(tp)
    print(len(que))
