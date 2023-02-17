cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

import collections
cards1 = collections.deque(cards1)
cards2 = collections.deque(cards2)

answer = []

i = 0
while i < len(goal):
    try:
        tar = cards1.popleft()
        if goal[i] == tar:
            answer.append(tar)
        else:
            cards1.appendleft(tar)
    except:pass

    try:
        tar = cards2.popleft()
        if goal[i] == tar:
            answer.append(tar)
        else:
            cards2.appendleft(tar)
    except:pass
    i += 1

if answer == goal:
    answer = 'Yes'
else:
    answer = 'No'