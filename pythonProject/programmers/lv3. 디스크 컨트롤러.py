jobs = [[0, 3], [1, 9], [2, 6]]

from collections import deque
answer = 0
jobs = [[i[0],i[1],i[1]-i[0]] for i in jobs]
jobs.sort(key=lambda x: (x[0], x[2]), reverse=True)
answer += jobs.pop()[2]
while jobs:
    jobs.sort(key=lambda x:(x[0],x[2]),reverse=True)
    tar = jobs.pop()
    answer += tar[1] + tar[2]



from collections import deque
jobs = [[i[0],i[1],i[1]-i[0]] for i in jobs]
jobs.sort(key=lambda x: (x[0], x[2]))
jobs = deque(jobs)

spt,ept,w = jobs.popleft()
answer = w
while jobs:
    request = []
    e = 0
    while ept > e:
        s, e, w = jobs.popleft()


arr = [1,1]
while len(arr) < 10**19:
    arr.append(arr[-1]+arr[-2])
arr[:10]