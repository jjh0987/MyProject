import sys
input = sys.stdin.readline
n = int(input())

import collections
que = collections.deque([i for i in (range(1,n+1))])
lv = 2
ans = que.popleft()

while que:
    cnt = lv**3
    cnt %= len(que)
    for _ in range(cnt):
        que.append(que.popleft())
    ans = que.pop()
    lv += 1

print(ans)
