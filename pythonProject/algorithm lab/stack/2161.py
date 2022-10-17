import sys
input = sys.stdin.readline

n = int(input())

import collections
q = collections.deque([i for i in range(1,n+1)])

ans = []
while q:
    try:
        ans.append(q.popleft())
        q.append(q.popleft())
    except:
        break

print(*ans)