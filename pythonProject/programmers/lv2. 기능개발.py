progresses = [93, 30, 55]
speeds = [1, 30, 5]

date = []
for i in range(len(progresses)):
    tp = 100 - progresses[i]
    q,r = divmod(tp,speeds[i])
    if r == 0:
        date.append(q)
    else:
        date.append(q+1)

for i in range(1,len(date)):
    if date[i] <= date[i-1]:
        date[i] = date[i-1]

import collections
list(collections.Counter(date).values())