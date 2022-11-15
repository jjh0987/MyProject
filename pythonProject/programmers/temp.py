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

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
ans = []
import itertools
for i in list(itertools.permutations(range(len(ability[0])))):
    tp = 0
    for j in i:
        tp += max([ability[k][j] for k in range(len(ability))])
    ans.append(tp)
ans
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


cards = [8,6,3,7,2,5,1,4]
ans = []


for i in cards:
    change = i
    tp = []
    while 1:
        change = cards[change-1]
        tp.append(change)
        if i == change:
            break
    if sorted(tp) in ans:
        pass
    else:
        ans.append(sorted(tp))

ans = sorted([len(i) for i in ans])

# 카운트다운
target = 58

single = [i for i in range(1,21)]
double = [i*2 for i in range(1,21)]
triple = [i*3 for i in range(1,21)]
dt = set(double).union(set(triple))

data = list(dt)
tp = []
for i in data:
    if i > 20:
        tp.append(i)
dt = set(tp)
dt

ans = [0,0]
while 1:
    if target > 60:
        target -= 60
        ans[0] += 1
        ans[1] += 1
    else:
        break

while target:
    if target > 20 and target in dt:
        ans[0] += 1
        break
    elif target > 50 and target not in dt:
        ans[0] += 1
        ans[1] += 1
        target -= 50
    elif target > 20 and target not in dt:
        ans[0] += 1
        ans[1] += 1
        target -= 20
    elif target <= 20:
        ans[0] += 1
        ans[1] += 1
        break

ans


2**20

sorted(['3','30','34','5','9'],reverse=True)
numbers = [3,30,34,5,9]
''.join(sorted([str(i) for i in numbers],key=lambda x: x * 3,reverse=True))

import sys
input = sys.stdin.readline

def collatz(x):
    if x == 1:
        num.append(1)
        return
    if x % 2 == 0:
        num.append(x)
        collatz(x // 2)
    else:
        num.append(x)
        collatz(3 * x + 1)

a,b = map(int,input().split())
num = []
collatz(a)
tp1 = num
num = []
collatz(b)
tp2 = num


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp = [0]*len(triangle)

for i in range(1,len(triangle)):
    for j in range(len(dp)):
        if j == 0:
            dp[j] += triangle[i][0]
        elif j == len(dp):
            dp[j] += triangle[i][-1]
        else:
            dp[j] += max(triangle[i][j],triangle[i][j-1])


