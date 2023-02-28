def solution(input_string):
    alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0
            ,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0
            ,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0
                ,'y':0,'z':0}
    input_string += 'A'
    # for alp in input_string:

    i = 0
    while i < len(input_string):
        try:
            check = input_string[i]
            j = i
            while 1:
                j += 1
                if input_string[j] != check:
                    break
            alpha[check] += 1

            i = j
        except:
            break

    answer = ''
    for i in alpha.keys():
        if alpha[i] > 1:
            answer += i

    if not answer:
        answer = 'N'
    return answer





abillity = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
abillity.sort()
abillity

queries = [[3, 1], [2, 3], [3, 9]]


import itertools
start = [['Rr'],['RR','Rr','Rr','rr']]
for i in range(1,4):
    tp = []
    for k in start[i]:
        tp.extend([''.join(sorted(x)) for x in itertools.product(k,repeat=2)])
    start.append(tp)

import itertools
n = 3
p = 1
start = [['Rr'],['RR','Rr','Rr','rr'],[],[],[]]
# n -= 1
x = [p]
loc = [0]*n
while x[0] != 0:
    n -= 1
    x = divmod(x[0],4) # (4개중 이전단계위치,4개중 현재위치)
    loc[n] = x

''.join(start[2])

i = 1
if loc[i][1]-1 > 0:
    start[i+1] = [''.join(sorted(j)) for j in itertools.product(start[i][loc[i][1]-1],repeat=2)]
else:
    start[i+1] = [''.join(sorted(j)) for j in itertools.product(start[i][loc[i][1]+4],repeat=2)]

i += 1

start

p = [100]
tp = []
while 1:
    p = divmod(p[0],4)
    tp.append(p)
    if p[0] == 0:
        break
tp.reverse()
4**4