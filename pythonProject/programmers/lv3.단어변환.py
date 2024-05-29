begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log",'cog']


visited = [False for _ in range(len(words) + 1)]
tp = [begin]
tp.extend(words)
dp = [[0 for _ in range(len(tp))] for _ in range(len(tp))]
ans_idx = 0
for i in range(len(tp)):
    for j in range(len(tp)):
        cnt = 0
        for k in range(len(begin)):
            if tp[i][k] != tp[j][k]:
                cnt += 1
        if cnt == 1:
            dp[i][j] = 1

    if tp[i] == target:
        ans_idx = i

import collections
tp = collections.deque([[0]])
lv = 0
while tp:
    tar = tp.pop()
    tmp = []
    if ans_idx in tar:
        break
    for j in tar:

        visited[j] = True
        for i in range(len(dp[0])):
            cnt = 0
            if dp[j][i] == 1 and not visited[i]:
                tmp.append(i)
    tp.append(tmp)
    lv += 1
    print(visited)

