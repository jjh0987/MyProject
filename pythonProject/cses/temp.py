from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
queue = deque()
for i in range(n):
    queue.append(i+1)
if k >= n:
    k = k % n

ans = ''
while 1:
    if len(queue) == 0:
        print(ans)
        break
    for i in range(k):
        queue.append(queue.popleft())
    ans += str(queue.popleft())+' '

# test case : 123456 666666 : fail