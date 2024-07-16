import sys
input = sys.stdin.readline
data = input()

import collections
data = data.split()
data = collections.deque(data)
cnt = 0
tp = []
while data:
    tar = data.popleft()
    if tar == '<br>':
        print(' '.join(tp))
        tp = []
        cnt = 0
        continue
    if tar == '<hr>':
        if tp:
            print(' '.join(tp))
        print('-'*80)
        tp = []
        cnt = 0
        continue
    cnt += len(tar) + 1
    tp.append(tar)
    if cnt > 80:
        data.appendleft(tp.pop())
        print(' '.join(tp))
        tp = []
        cnt = 0
        continue
if tp:
    print(' '.join(tp))
