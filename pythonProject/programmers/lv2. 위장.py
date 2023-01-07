clothes = [["yellow_hat", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]

target = [i[1] for i in clothes]
import collections

ans = 1
target = collections.Counter(target)
target = [target[i]+1 for i in target]
for i in target:
    ans *= i


import itertools
for j in range(1,len(set(target))+1):
    for i in itertools.combinations(target.values(),j):
        tp = 1
        for k in i:
            tp *= k
        ans += tp

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

def factor(x):
    ans = []
    if prime(x):
         return [x]
    else:
        while x != 1:
            for i in range(2,x+1):
                if x%i == 0:
                    x = int(x/i)
                    ans.append(i)
                    break
    return ans
import collections
def combi(n,r):
    if r > n - r:
        r = n - r
    n_fact = collections.deque(list(range(n - r + 1, n + 1)))
    n_r_fact = list(range(2, r + 1))
    tp = []
    for i in [factor(i) for i in n_r_fact]:
        tp.extend(i)
    ans = 1
    while tp:
        tar = tp.pop()
        for _ in range(len(n_fact)):
            target = n_fact.popleft()
            if target % tar == 0:
                target = int(target / tar)
                n_fact.append(target)
                break
            if target != 1:
                n_fact.append(target)
    for i in n_fact:
        ans *= i
    return ans

ans = 0
for i in range(1,len(target)+1):
    ans += combi(len(target),i)

