priorities = [1, 1, 9, 1, 1, 1]
location = 0

import collections
priority = collections.Counter(priorities)
target = collections.deque()
for i in range(len(priorities)):
    target.append([priorities[i],i])

ans = []
show = 0

for i in reversed(priority.keys()): # prior
    while priority[i] != 0:
        tp = target.popleft()
        if tp[0] == i:
            show += 1
            ans.append([tp[0],tp[1],show])
            priority[i] -= 1
        else:
            target.append(tp)

answer = 0
for i in ans:
    if i[1] == location:
        answer = i[2]
        break
print(answer)
ans



priorities = [1, 1, 9, 1, 1, 1]
location = 0

import collections
target = collections.deque()
for i in range(len(priorities)):
    target.append([priorities[i],i])

cnt = 0
flag = 0
breaker = target[location][1]
for i in range(9,0,-1):
    stopper = target.popleft()
    target.append(stopper)
    if stopper[0] == breaker and stopper[1] == location:
        cnt += 1
        break

    while 1:
        tp = target.popleft()
        if tp == stopper:
            target.appendleft(tp)
            break

        if tp[0] == i and tp[1] == location:
            cnt += 1
            flag = 1
            break

        if tp[0] == i:
            cnt += 1
        target.append(tp)

    if flag == 1:
        break



priorities = [2, 1, 3, 2]
location = 2


import collections
target = collections.deque()
for i in range(len(priorities)):
    target.append([i,priorities[i]])
info = [location,priorities[location]]
priorities = collections.Counter(priorities)


cnt = 0
flag = 0
for i in sorted(priorities.keys(),reverse=True):
    while priorities[i] > 0:
        tar = target.popleft()
        if tar[1] == i:
            priorities[i] -= 1
            cnt += 1
            if tar[0] == info[0]:
                flag = 1
                break
        else:
            target.append(tar)
    if flag == 1:
        break