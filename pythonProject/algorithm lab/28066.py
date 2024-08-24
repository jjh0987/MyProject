import sys
input = sys.stdin.readline
n,k = map(int,input().split())

import collections
que = collections.deque([i for i in (range(1,n+1))])
flag = False
while que:
    if flag:
        break
    que.append(que.popleft())
    for _ in range(k-1):
        tp = que.popleft()
        if len(que) == 1:
            flag = True
            print(que[0])
            break