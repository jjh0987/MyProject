A = '20:00'
B = '06:00'

A = [int(i) for i in A.split(':')]
B = [int(i) for i in B.split(':')]

hours = list(range(24))
minutes = list(range(60))
starting = [0,15,30,45]
cnt = 0
hour_cnt = abs(B[0] - A[0])
for i in starting:
    if i in range(A[1],B[1]-A[1]+2):
        cnt += 1

if A[0] > B[0]:
    if cnt == 0:
        print(96-hour_cnt*4)
    else:
        print(96-hour_cnt*4+cnt-1)
else:
    if cnt == 0:
        print(hour_cnt*4)
    else:
        print(hour_cnt*4+cnt-1)
