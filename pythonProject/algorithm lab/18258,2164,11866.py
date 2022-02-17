# 18258
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
len(queue)
for _ in range(n):
    temp = input().split()
    if len(temp) == 2:
        queue.append(int(temp[1]))
    elif temp[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif temp[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
    elif temp[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

# 2164
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    queue.append(i+1)

while 1:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())

# 11866
from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
queue = deque()
for i in range(n):
    queue.append(i+1)

ans = '<'
while 1:
    if len(queue) == 0:
        ans = ans.rstrip(', ')
        print(ans+'>')
        break
    for i in range(k-1):
        queue.append(queue.popleft())
    ans += str(queue.popleft())+', '