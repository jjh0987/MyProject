# 11720
n = input()
print(sum(map(int,input())))
ls = list(map(int,input())) # 12345
# 인덱스를 이용해서 맵핑 -> [1,2,3,4,5]


# 2750
import heapq

n = int(input())
h = []
for i in range(n):
    heapq.heappush(h,int(input()))
for i in range(n):
    print(heapq.heappop(h))
# --
n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
ls = sorted(ls)
for i in ls:
    print(i)

#
print([i**2 for i in range(1,1+int(input()))])

#
print([f'No.{i}' for i in range(1,1+int(input()))])

# 2562
import sys
input = sys.stdin.readline
ls = []
for _ in range(9):
    ls.append(int(input()))
print(max(ls))
print(ls.index(max(ls))+1)

#
ls = []
for _ in range(6):
    ls.append(input())

import numpy as np
arr1 = []
arr2 = []
for i in range(len(ls)):
    if len(ls[i]) == 7 and i < 3:
        arr1.append(list(map(int,ls[i].split())))
    elif len(ls[i]) == 7 and i > 3:
        arr2.append(list(map(int,ls[i].split())))
arr1 = np.array(arr1)
arr2 = np.array(arr2)

for i in arr1*arr2:
    temp = ''
    for j in i:
        temp += f'{j} '
    print(temp)

# 1100
target = []
for i in range(8):
    target.append(input())
cnt = 0
for i in range(8):
    if i%2 == 0:
        for j in range(8):
            if j%2 == 0 and target[i][j] == 'F':
                cnt += 1
    else:
        for j in range(8):
            if j%2 == 1 and target[i][j] == 'F':
                cnt += 1
print(cnt)