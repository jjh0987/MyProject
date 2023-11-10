import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return 0
    return x


import collections
n = int(input())
tar = collections.deque()
half_number = [prime(i) for i in range(1,4000000,2)]
half_number = [i for i in half_number if i > 0]
half_number[0] = 2
ans = 0
for i in half_number:
    check = sum(tar)
    while check > n:
        tar.popleft()
    while check < n:
        tar.append(i)
    if sum(tar) == n:
        ans += 1