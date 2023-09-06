book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
             ["14:10", "19:20"], ["18:20", "23:59"]]


book_time = [[list(map(int,i.split(':'))) for i in j] for j in book_time]
for i in book_time:
    i[1][1] += 10
    i[1] = (i[1][0]-i[0][0])*60 + (i[1][1]-i[0][1])
    i[0] = i[0][0]*60 + i[0][1]
    if i[0]+i[1] > 24*60-1:
        i[1] = 24*60-1-i[0]


time_table = [0 for _ in range(24*60)]
for i in book_time:
    while i[1] > 0:
        idx = i[0]+i[1]
        time_table[idx-1] += 1
        i[1] -= 1

time_table[1:100] = [1 for _ in range(len(time_table[1:100]))]
time_table[1:100]
len(time_table)