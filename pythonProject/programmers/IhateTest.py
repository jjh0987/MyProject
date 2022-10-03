words = ['may','with','may','you','you']

dictionary = {}
for i in range(len(words)):
    if words[i] in dictionary:
        continue

    dictionary[words[i]] = i+1

ans = [dictionary[word] for word in words]


nums = [1,2,7,6,4]
cnt = 0

import math
import itertools

def prime(x):
    if x == 1:
        return
    if x == 2:
        return 2
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return
    return x


for i in [sum(i) for i in list(itertools.combinations(nums,3))]:
    if prime(i):
        cnt += 1

cnt


maps = [[1,0,1,1],
        [0,0,1,1],
        [1,1,0,1],
        [1,1,0,0]]

maps = [[0,0,1,0,0],
        [0,1,1,0,1],
        [0,0,1,0,1],
        [1,1,1,0,1]]


def dfs(x,y,color):
    if x < 0 or y < 0 or x >= len(maps) or y >= len(maps[0]):
        return False
    if maps[x][y] == 1:
        tp.append((x,y))
        maps[x][y] = 'x'
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)


    if len(tp) == 1:
        return tp
    else:
        a = max([i[0] for i in tp]) - min([i[0] for i in tp]) + 1
        b = max([i[1] for i in tp]) - min([i[1] for i in tp]) + 1
    return tp


# dfs(1,2,1)
# maps

island = []
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 'x' or maps[i][j] == 0:
            tp = []
            continue
        else:
            island.append(dfs(i,j,1))

def make_tar_map(island):
    target_map = [[0 for _ in range(len(maps[0])+2)] for _ in range(len(maps)+2)]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (i,j) in island:
                target_map[i+1][j+1] = 1

    return target_map
ans = []
for land in island:
    target_map = make_tar_map(land)
    cnt = 0
    for i in range(len(target_map)):
        for j in range(len(target_map[0])):
            if target_map[i][j] == 1:
                if target_map[i-1][j] == 0:
                    cnt += 1
                if target_map[i][j-1] == 0:
                    cnt += 1
                if target_map[i+1][j] == 0:
                    cnt += 1
                if target_map[i][j+1] == 0:
                    cnt += 1
    ans.append(cnt)






numbers = [8,3,5,7,3,4]
numbers


import copy
operator_list = []
def operator(tar, n):
    if len(tar) == n:
        operator_list.append(copy.deepcopy(tar))
        return

    tar.append('+')
    operator(tar, n)
    tar.pop()

    tar.append('-')
    operator(tar, n)
    tar.pop()

operator([],len(numbers))

lst = [str(i) for i in numbers]

cnt = 0
for oper in operator_list:
    tp = ''
    for j in range(len(oper)):
        tp += oper[j]
        tp += lst[j]
    if eval(tp) == 0:
        cnt += 1

cnt


direction = ((-1,0), (1,0), (0, -1), (0, 1))

def sol(st_y, st_x):
    global w, h
    cnt = 0
    for d in direction:
        next_y = st_y + d[0]
        next_x = st_x + d[1]
        if next_y<0 or next_y>=len(maps) or next_x<0 or next_x>=len(maps[0]) or maps[next_y][next_x] == 0:
            cnt += 1
    return cnt

while True:

    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                continue
            answer += sol(i,j)

    print(answer)




# n = int(input())
# scores = list(map(int,input().split()))
# tp = max(scores)
# scores = [(i/tp)*100 for i in scores]
# print(sum(scores)/len(scores))
#
# import collections
# s = input().upper()
# target = dict(collections.Counter(s))
# marking = []
# for i in target:
#     if target[i] == max(target.values()):
#         marking.append(i)
#
# if len(marking) == 1:
#     print(marking[0])
# else:
#     print('?')
#
# n = int(input())
# lst = sorted(list(map(int,input().split())))
# print(f'{lst[0]} {lst[-1]}')
#
# print(len(input().split()))
#
# tar = [eval(''.join(list(reversed(i)))) for i in input().split()]
# if tar[0] > tar[1]:
#     print(tar[0])
# else:
#     print(tar[1])
#
#
# tp = set()
# for _ in range(10):
#     tp.add(int(input())%42)
# print(len(tp))