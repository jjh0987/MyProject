n = 2000
target = [n,0]
case = [[n,0]]
while target[0] > 1:
    target[0] -= 2
    target[1] += 1
    case.append(sorted([i for i in target],reverse=True))

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
        if ans >= 1234567:
            ans = ans % 1234567
    return ans


answer = 0
for i in case:
    answer += combi(i[0]+i[1],i[1])
    if answer >= 1234567:
        answer = answer % 1234567

print(answer)

n = 100
r = 30
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

len(n_fact)