import sys
import string
import collections
input = sys.stdin.readline
T = int(input())
words = [(input().rstrip('\n'),i) for i in range(T)]
words.sort()

answer = []
for i in range(1,T):
    tp = 0
    if words[i-1][0][0] == words[i][0][0]:
        for j in range(len(words[i])):
            try:
                if words[i-1][0][j] == words[i][0][j]:
                    tp += 1
                else:
                    break
            except:
                break
    answer.append((tp,min(words[i-1][1],words[i][1]),
                   words[i-1][1]+words[i][1],
                   words[i-1],words[i]))
answer.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))

s1 = answer[0][3]
s2 = answer[0][4]
if s1[1] > s2[1]:
    print(s2[0])
    print(s1[0])
else:
    print(s1[0])
    print(s2[0])


# 첫 스펠링 dictionary




import sys
import string
import collections
input = sys.stdin.readline
T = int(input())
words = [(input().rstrip('\n'),i) for i in range(T)]
words.sort()

answer = []
for i in range(T):
    for j in range(i+1,T):
        tp = 0
        if words[i][0][0] == words[j][0][0]:
            for k in range(len(words[j][0])):
                try:
                    if words[i][0][k] == words[j][0][k]:
                        tp += 1
                    else:
                        break
                except:
                    break
        if not answer:
            if tp > 0:
                answer.append((tp, min(words[i][1], words[j][1]),
                               words[i][1] + words[j][1],
                               words[i], words[j]))
        else:
            if answer[0][0] < tp:
                answer[0] = (tp, min(words[i][1], words[j][1]),
                               words[i][1] + words[j][1],
                               words[i], words[j])

s1 = answer[0][3]
s2 = answer[0][4]
if s1[1] > s2[1]:
    print(s2[0])
    print(s1[0])
else:
    print(s1[0])
    print(s2[0])
