
# 2953
ls = []
for i in range(5):
    ls.append(sum(map(int,input().split())))
print(ls.index(max(ls))+1,max(ls))

# 4344
n = int(input())
for _ in range(n):
    ls = list(map(int,input().split()))
    cnt = 0
    for i in ls[1:]:
        if i > sum(ls[1:])/ls[0]:
            cnt += 1
    print(f'{format(round(cnt/ls[0],5)*100,".3f")}%')


a = 1,2,3,4
a,b,c,d = a
a
b
c
d

n = int(input())
for _ in range(n):
    m,*scores = map(int,input().split())
    cnt = 0
    for i in scores:
        if i > sum(scores)/m:
            cnt += 1
    print(f'{(cnt/m)*100:.3f}%')

# 2947
import copy
ls = list(map(int,input().split()))
for i in range(5):
    for j in range(4):
        temp_ls = copy.copy(ls)
        if ls[j] > ls[j+1]:
            temp = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = temp
        if temp_ls != ls:
            ans = ''
            for i in ls:
                ans += f'{i} '
            print(ans)

# 1032

n = int(input())
ls = []
for i in range(n):
    ls.append(input())
    if i == 0:
        check = len(ls[0])
        target = ' '.join(ls[0]).split()

for i in range(1,n):
    for j in range(check):
        if target[j] != ls[i][j]:
            target[j] = '?'

print(''.join(target))

# 10798
ls = []
for i in range(5):
    ls.append(input())

ans = ''
for i in range(15):
    for j in range(5):
        try:
            ans += ls[j][i]
        except:
            pass
print(ans)

# 2563


# 2669


# 9291
import sys
input = sys.stdin.readline
n = int(input())
label = list(range(1,10))

from collections import deque
queue = deque()
for _ in range(n*9+n-1):
    put = list(map(int,input().split()))
    if put == []:
        continue
    queue.append(put)

targets = []
for _ in range(n):
    temp = []
    for _ in range(9):
        temp.append(queue.popleft())
    targets.append(temp)

idx = 0
for target in targets:
    idx += 1
    column_target = []
    for j in range(9):
        temp_col = []
        for k in range(9):
            temp_col.append(target[k][j])
        column_target.append(sorted(temp_col))

    box_target = [[],[],[],
                  [],[],[],
                  [],[],[]]
    cnt = -3
    for j in range(0,9):
        if j % 3 == 0:
            cnt += 3
        for k in range(9):
            box_target[cnt + k//3].append(target[j][k])


    acc1 = 0
    for j in range(9):
        if label == sorted(target[j]):
            acc1 += 1

    acc2 = 0
    for j in range(9):
        if label == column_target[j]:
            acc2 += 1

    acc3 = 0
    for j in range(9):
        if label == sorted(box_target[j]):
            acc3 += 1


    if acc1 == 9 and acc2 == 9 and acc3 ==9:
        print(f'Case {idx}: CORRECT')
    else:
        print(f'Case {idx}: INCORRECT')
