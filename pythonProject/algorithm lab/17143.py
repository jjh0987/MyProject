import collections
import sys
input = sys.stdin.readline
r,c,m = map(int,input().split())
graph = [[[] for _ in range(c)] for _ in range(r)]
direction = [(-1,0),(1,0),(0,1),(0,-1)]
que = collections.deque()
for i in range(m):
    a,b,s,d,z = map(int,input().split())
    que.append((i,a,b,s,d,z))

nums = len(que)
answer = 0
for t in range(1,c+1):
    t = 1
    visited = [False for _ in range(nums)]
    while que:
        idx,a,b,s,d,z = que.popleft()
        if visited[idx]:
            que.appendleft((idx,a,b,s,d,z))
            break
        if b == t:
            answer += z
            continue
        visited[idx] = True
        que.append((idx,a,b,s,d,z))

    visited = [False for _ in range(nums)]
    while que:
        idx,a,b,s,d,z = que.popleft()
        if visited[idx]:
            que.appendleft((idx,a,b,s,d,z))
            break
        visited[idx] = True
        if d == 1 or d == 2:
            if s%c == 1:
                if d == 1:
                    d = 2
                else:
                    d = 1
            tp = s%c
        else:
            if s%r == 1:
                if d == 3:
                    d = 4
                else:
                    d = 3
            tp = s%r
        print(tp)
        dx,dy = direction[d-1]
        a += tp*dx
        b += tp*dy
        a %= (r+1)
        b %= (c+1)
#        if 0 <= a < r or 0 <= b < c:
        que.append((idx,a,b,s,d,z))
