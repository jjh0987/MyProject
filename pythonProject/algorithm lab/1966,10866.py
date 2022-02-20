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

# 10866
# # 18258 reinforce
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
len(queue)
for _ in range(n):
    temp = input().split()
    if len(temp) == 2:
        if temp[0] == 'push_front':
            queue.append(int(temp[1]))
        else:
            queue.appendleft(int(temp[1]))
    elif temp[0] == 'front':
        try:
            print(queue[-1])
        except:
            print(-1)
    elif temp[0] == 'back':
        try:
            print(queue[0])
        except:
            print(-1)
    elif temp[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif temp[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())