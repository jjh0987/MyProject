# 1966
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

for i in range(n):
    num,loc = map(int,input().split())
    temp = list(map(int,input().split()))
    queue1 = deque()

    target = temp[loc]
    temp[loc] = -1

    for i in temp:
        queue1.append(i)

    cnt = 0

    while target < max(queue1):
        temp = queue1[0]
        if temp == max(queue1):
            queue1.popleft()
            cnt += 1
        else:
            queue1.append(temp)
            queue1.popleft()

    while target == max(queue1):
        temp = queue1[0]
        if temp == target:
            queue1.popleft()
            cnt += 1
        elif temp == -1:
            break
        else:
            queue1.append(temp)
            queue1.popleft()

    while 1:
        temp = queue1[0]
        if temp == -1:
            cnt += 1
            break
        else:
            queue1.append(temp)
            queue1.popleft()

    print(cnt)
