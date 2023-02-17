number = 10
limit = 3
power = 2

idx_table = [0 for i in range(number+1)]
for j in range(1,number+1):
    for i in range(j,number+1,j):
        if i%j == 0:
            idx_table[i] += 1
answer = 0
for i in idx_table:
    if i > limit:
        answer += power
    else:
        answer += i





import math
def prime(x):
    if x == 1:
        return
    elif x == 2:
        return 2
    for j in range(2, int(math.sqrt(x)) + 2):
        if x % j == 0:
            return
    return x

prime_table = []
for i in range(1,100001):
    tar = prime(i)
    if tar:
        prime_table.append(tar)

prime_table

# cut = [0]*len(prime_table)

ans = []
for i in range(2,number+1):
    temp = []
    while i > 1:
        for j in prime_table:
            if i < int(j/2)+1:
                break
            if i%j == 0:
                temp.append(j)
                i = int(i/j)
                break
    ans.append(temp)

import collections
table = [[j+1 for j in collections.Counter(i).values()] for i in ans]
answer = []
for i in table:
    tp = 1
    for j in i:
        tp *= j
    answer.append(tp)

out = 1
for i in answer:
    if i > limit:
        out += power
    else:
        out += i