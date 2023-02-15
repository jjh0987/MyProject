k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

import collections
score = collections.deque(score)
target = []
answer = []

while score:
    tar = score.popleft()
    target.append(tar)
    target.sort()

    if len(target) > k:
        target = target[1:]

    answer.append(min(target))

answer