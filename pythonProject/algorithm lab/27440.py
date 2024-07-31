import sys
input = sys.stdin.readline
n = int(input())

import collections
que = collections.deque([(n,0)])
visited = {}
while que:
    v,trial = que.popleft()
    if v == 1:
        break
    trial += 1
    if v%3 == 0 and v//3 not in visited:
        visited[v//3] = trial
        que.append((v//3,trial))
    if v%2 == 0 and v//2 not in visited:
        visited[v//2] = trial
        que.append((v//2,trial))
    if v-1 not in visited:
        visited[v-1] = trial
        que.append((v-1,trial))

print(trial)


import sys
input = sys.stdin.readline
n = int(input())

import collections
que = collections.deque([(n,0)])
visited = set()
while que:
    v,trial = que.popleft()
    if v == 1:
        break
    trial += 1
    if v%3 == 0 and v//3 not in visited:
        visited.add(v//3)
        que.append((v//3,trial))
    if v%2 == 0 and v//2 not in visited:
        visited.add(v//2)
        que.append((v//2,trial))
    if v-1 not in visited:
        visited.add(v-1)
        que.append((v-1,trial))

print(trial)
