n = 110011
k = 3

import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x == 2:
            return 2
        if x%j == 0:
            return
    if x == 1:
        return
    return x

target = ''
k_map = []
i = 0
while 1:
    tar = k**i
    if tar > n:
        break
    else:
        k_map.append(tar)
    i += 1

while k_map:
    k_tar = k_map.pop()
    tar, n = divmod(n,k_tar)
    target += str(tar)

cnt = 0
for i in target.split('0'):
    try:
        if prime(int(i)) == int(i):
            cnt += 1
    except:pass