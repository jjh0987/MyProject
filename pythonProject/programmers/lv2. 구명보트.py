people = [70, 80, 50]
limit = 100

import collections
people = collections.deque(sorted(people))

cnt = 0
while people:
    try:
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            cnt += 1
        else:
            people.pop()
            cnt += 1
    except:
        cnt += 1
        break