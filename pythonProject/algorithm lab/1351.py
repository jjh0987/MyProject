import sys
input = sys.stdin.readline
n,p,q = map(int,input().split())

import collections
que = collections.deque([(int(n/p),p),(int(n/q),q)])
answer = 0
visited = {} # => p,q dp table
while que:
    print(que)
    v,d = que.popleft()
    if v == 0:
        answer += 1
        continue
    que.append((int(v/p),p))
    que.append((int(v/q),q))