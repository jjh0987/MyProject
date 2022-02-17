from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    queue.append(i+1)
k = 2
ans = ''
while 1:
    if len(queue) == 0:
        ans = ans.rstrip(', ')
        print(ans)
        break
    for i in range(k-1):
        queue.append(queue.popleft())
    ans += str(queue.popleft())+' '