fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN",
           "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN",
           "23:00 5961 OUT"]

cars = {i.split()[1]:[] for i in records}
ans = {i:0 for i in cars.keys()}
for reco in records:
    t,car,mark = reco.split()
    cars[car].append(t)

for car in cars:
    if len(cars[car])%2 == 1:
        cars[car].append('23:59')

for car in cars:
    for i in range(0,len(cars[car]),2):
        h2,m2 = [int(j) for j in cars[car][i+1].split(':')]
        h1,m1 = [int(j) for j in cars[car][i].split(':')]
        ans[car] += (int(h2) - int(h1)) * 60 + (int(m2)-int(m1))

f_ans = {i:0 for i in cars.keys()}
for car in ans:
    f_ans[car] += fees[1]
    if ans[car] > fees[0]:
        q,r = divmod((ans[car]-fees[0]),fees[2])
        if r > 0:
            f_ans[car] += (q+1)*fees[3]
        else:
            f_ans[car] += q*fees[3]

target = [[i,f_ans[i]] for i in f_ans]
target.sort(key=lambda x:x[0])

# parking_time = dict(sorted(parking_time.items()))