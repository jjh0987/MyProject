import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ans = -1
import collections
q = collections.deque([[n,1]])

while q:
    tar,cnt = q.popleft()
    if tar == m:
        ans = cnt
        break

    if tar < m:
        q.append([2*tar,cnt+1])

    if tar < m:
        q.append([int(str(tar)+'1'),cnt+1])

print(ans)