p = input()

def uv_decomposition(p):
    i = 0
    while 1:
        if p[i] == '(':
            i += 1
        else:
            break
    if i == 0:
        while 1:
            if p[i] == ')':
                i += 1
            else:
                break
    return p[:2*i],p[2*i:]

#u,v = uv_decomposition(p)

def switch(u):
    tp = ' '.join(u[1:len(u)-1]).split()
    tp.reverse()

    if not tp or tp[0] != tp[-1]:
        u = '(' + ''.join(tp) + ')'
    return u


#switch(u)

def check(p):
    tp = p
    while tp:
        tp = tp.replace('()', '')
        if tp == tp.replace('()', ''):
            break
    if tp == '':
        return 1
    else:
        return 0

def solution(p):
    if check(p) == 1:
        return p

    u,v = uv_decomposition(p)
    if check(u) == 0:
        return switch(u) + solution(v)
    elif check(v) == 0:
        return solution(u) + solution(v)
    else:
        return u + v



solution(p)


# import math
# W,H = 8,12
# box = math.gcd(W,H)
#
# sub_W = int(W/box)
# sub_H = int(H/box)
#
# sub_W = min(sub_H,sub_W)
# sub_H = max(sub_H,sub_W)
#
# blank = 0
# cnt = 1
# while 1:
#     if sub_W >= 1 and sub_W < 2:
#         blank += sub_H
#         break
#     else:
#         sub_H = math.ceil(sub_H/2)
#         sub_W = sub_W/2
#         cnt += 1
#
# blank * cnt * box
<<<<<<< HEAD

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
ans = []
import itertools
for i in list(itertools.permutations(range(len(ability[0])))):
    tp = 0
    for j in i:
        tp += max([ability[k][j] for k in range(len(ability))])
    ans.append(tp)
ans
=======
import copy

n = 5
lost = [2,3]
reverse = [3]
reverse.sort()
for i in reverse:
    if i in lost:
        lost.remove(i)
        reverse.remove(i)
reverse

for i in range(len(reverse)):
    try:
        if reverse[i]-1 in lost:
            lost.remove(reverse[i]-1)
        elif reverse[i]+1 in lost:
            lost.remove(reverse[i]+1)
    except:
        pass
print(n-len(lost))

reverse.pop(reverse.index(3))
lost.pop(2)
>>>>>>> c4c9e352bc874ada7c8c5bd0fd5c6e7d7fb152e2
