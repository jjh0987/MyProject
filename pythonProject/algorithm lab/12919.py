import sys
input = sys.stdin.readline
s1 = input().rstrip('\n')
s2 = input().rstrip('\n')

import collections
que = collections.deque()
que.append(s2)
visited = set()
visited.add('')
flag = False
while que:
    tar = que.popleft()
    if tar in visited:
        continue
    if tar == s1:
        flag = True
        print(1)
        break
    if tar not in visited:
        visited.add(tar)
        if tar[-1] == 'A':
            que.append(tar[:-1])
        if tar[0] == 'B':
            que.append(tar[len(tar):0:-1])
if not flag:
    print(0)