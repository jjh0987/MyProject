begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

tp = [begin]
tp.extend(words)
dp = [[0 for _ in range(len(tp))] for _ in range(len(tp))]
for i in range(len(tp)):
    for j in range(i,len(tp)):
        cnt = 0
        for k in range(len(begin)):
            if tp[i][k] != tp[j][k]:
                cnt += 1
        if cnt == 1:
            dp[i][j] = 1
dp











answer = 0
import collections
words = collections.deque(words)
tp = collections.deque()
tp.append([begin])
answer = 0
while words:
    begin_lst = tp.popleft()
    lv = []
    for begin in begin_lst:
        for _ in range(len(words)):
            flag = 0
            cnt = 0
            tar = words.popleft()

            for i in range(len(tar)):
                if begin[i] != tar[i]:
                    cnt += 1
                if cnt == 1:
                    flag = 1
                else:
                    flag = 0
            if flag == 1:
                lv.append(tar)
            else:
                words.append(tar)
    tp.append(lv)
    answer += 1

if target in tp[0]:
    return answer
else:
    return 0