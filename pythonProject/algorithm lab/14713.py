import sys
input = sys.stdin.readline
n = int(input())

import collections
bird = dict()
length = 0
for i in range(1,n+1):
    bird[i] = collections.deque(input().split())
    length += len(bird[i])
target = collections.deque(input().split())
if length != len(target):
    print('Impossible')
else:
    while target:
        tar = target.popleft()
        flag = True
        for i in range(1,n+1):
            if bird[i]:
                if bird[i][0] == tar:
                    bird[i].popleft()
                    flag = False
                    break
        if flag:
            print('Impossible')
            break
    check = sum([len(bird[i]) for i in range(1,n+1)])
    if not target and check == 0:
        print('Possible')