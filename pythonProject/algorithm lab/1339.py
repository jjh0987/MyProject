n = int(input())
arr = []
for _ in range(n):
    tar = input()
    tp = ['-' for _ in range(8 - len(tar))]
    tp.extend(list(tar))
    arr.append(tp)

import string

alpha = set(list(string.ascii_uppercase))
prior = dict()
for i in arr:
    for j in i:
        if j in alpha:
            prior[j] = [0 for _ in range(8)]

import collections

for j in range(8):
    tp = collections.Counter([i[j] for i in arr])
    for s in tp:
        if s == '-':
            continue
        prior[s][j] += tp[s]

import heapq

target = []
for i in prior:
    tp = prior[i]
    for j in range(1, len(tp)):
        if tp[j] == 10:
            tp[j] = 0
            tp[j - 1] += 1
    tp.append(i)
    target.append(tp)
heapq.heapify(target)

i = 0
score = dict()
while target:
    tar = heapq.heappop(target)
    score[tar[-1]] = i
    i += 1

for i in score:
    score[i] += 10 - len(score)
ans = 0
for tar in arr:
    s = ''
    for i in tar:
        if i == '-':
            continue
        s += str(score[i])
    tp = s.lstrip('0')
    if tp:
        ans += eval(tp)
print(ans)

