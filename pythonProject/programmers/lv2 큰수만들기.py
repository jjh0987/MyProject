number = '4177252841'
k = 4

number = [[number[i], i] for i in range(len(number))]
import collections

tp = collections.deque([number.pop()])
while 1:
    tar = number.pop()
    if tar[0] >= tp[0][0]:
        tp.appendleft(tar)
    else:
        number.append(tar)
        break

import heapq

heapq.heapify(number)
while k > 0:
    heapq.heappop(number)
    k -= 1
number.sort(key=lambda x: x[1])
answer = ''
for i in number:
    answer += str(i[0])
while tp:
    answer += str(tp.popleft()[0])