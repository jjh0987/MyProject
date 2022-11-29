flowers = [[1,1],[1,2]]
tp = []
for f in flowers:
    tp.extend(list(range(f[0],f[1])))
len(set(tp))



id_list = ['A B C D','A D','A B D','B D']
id_list = ['JAY','JAY ELLE JAY MAY','MAY ELLE MAY','ELLE MAY','ELLE ELLE ELLE','MAY']
K = 3

id_list = [list(set(i.split())) for i in id_list]
tp = []
for i in id_list:
    tp.extend(i)

import collections
target = collections.Counter(tp)
cnt = 0
for key in target.keys():
    if target[key] > K:
        cnt += K
    else:
        cnt += target[key]


s = '2021:04:12:16:08:35'
times = ['01:06:30:00','01:01:12:00','00:00:09:25']


start = [int(i) for i in s.split(':')]
tp = [0]*4
time_table = [[int(j) for j in i.split(':')] for i in times]

for time in time_table:
    for i in range(4):
        if time[i] > 0:
            tp[i] += time[i]

        if tp[3] >= 60:
            tp[2] += 1
            tp[3] -= 60
        if tp[2] >= 60:
            tp[1] += 1
            tp[2] -= 60
        if tp[1] >= 24:
            tp[0] += 1
            tp[1] -= 24

for i in range(3,-1,-1):
    start[i+2] += tp[i]
    if start[5] >= 60:
        start[5] -= 60
        start[4] += 1
    if start[4] >= 60:
        start[4] -= 60
        start[3] += 1
    if start[3] >= 24:
        start[3] -= 24
        start[2] += 1
    if start[2] >= 30:
        start[2] -= 30
        start[1] += 1
    if start[1] >= 12:
        start[1] -= 12
        start[0] += 1


init_time = [int(i) for i in s.split(':')]
invest_day = 1
dt = [360,30,1]
for i in range(3):
    if start[i] - init_time[i] >= 0:
        invest_day += dt[i]*(start[i] - init_time[i])


start = [int(i) for i in s.split(':')]
time_table = [[int(j) for j in i.split(':')] for i in times]

one_day = [init_time[2]]


for time in time_table:
    for i in range(4):
        start[i+2] += time[i]
        if start[5] >= 60:
            start[5] -= 60
            start[4] += 1
        if start[4] >= 60:
            start[4] -= 60
            start[3] += 1
        if start[3] >= 24:
            start[3] -= 24
            start[2] += 1
        if start[2] >= 30:
            start[2] -= 30
            start[1] += 1
        if start[1] >= 12:
            start[1] -= 12
            start[0] += 1

    if one_day[-1] != start[2]:
        one_day.append(start[2])

ans = []
if invest_day == len(one_day):
    ans.append(1)
else:
    ans.append(0)
ans.append(invest_day)
ans

init_time
start