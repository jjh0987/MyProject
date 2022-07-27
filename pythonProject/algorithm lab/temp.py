# 2564
import sys
input = sys.stdin.readline
box = list(map(int,input().split()))
n = int(input())
store = []
for _ in range(n+1):
    store.append(list(map(int,input().split())))

LR = []
for i in store:
    temp = []
    if i[0] == 1:
        temp.append(box[1] + i[1])
        temp.append(2*box[0] + box[1] - i[1])
    elif i[0] == 2:
        temp.append(2*box[1] + 2*box[0] - i[1])
        temp.append(i[1])
    elif i[0] == 3:
        temp.append(box[1] - i[1])
        temp.append(2*box[0] + box[1] + i[1])
    elif i[0] == 4:
        temp.append(box[0] + 2*box[1] + i[1])
        temp.append(box[0] + box[1] - i[1])
    LR.append(temp)

guard = LR.pop(-1)
# guard 가 + set 인지 - set 인지 구별

plus_store = []
minus_store = []
center_store = []
for i in LR:
    if 0 < i[0] < sum(box):
        plus_store.append(i)
    elif i[0] > sum(box):
        minus_store.append(i)
    elif i[0] == sum(box):
        center_store.append(i)

ans1 = 0
for i in plus_store:
    ans1 += i[0] + guard[1]
ans2 = 0
for i in minus_store:
    ans2 += abs(i[1] - guard[1])

ans = ans1 + ans2 + sum(box)*len(center_store)
print(ans)

# 10157
width,height = map(int,input().split())
loc = int(input())
rec = []

for i in range(50):
    temp = 2 * ((width - 1 - 2 * i) + (height - 1 - 2 * i))
    if temp > 0:
        rec.append(temp)
if width * height - sum(rec) > 0:
    rec.append(width * height - sum(rec))

ans = []
x = 1
if width*height < loc:
    x = 0
else:
    starting_pt = [1,1]
    for i in range(len(rec)):
        loc -= rec[i]
        if loc <= 0:
            loc += rec[i]
            starting_pt = [i+1,i+1]
            height = height-2*i
            width = width-2*i
            rec_target = rec[i]
            break

    temp = [starting_pt]
    for i in range(1,height):
        temp.append([starting_pt[0],starting_pt[1]+i])
    starting_pt = temp[-1]

    for i in range(1,width):
        temp.append([starting_pt[0]+i,starting_pt[1]])
    starting_pt = temp[-1]

    for i in range(1,height):
        temp.append([starting_pt[0],starting_pt[1]-i])
    starting_pt = temp[-1]

    for i in range(1,width):
        temp.append([starting_pt[0]-i,starting_pt[1]])
    temp.pop(-1)
    ans.extend(temp)
if x == 0:
    print(0)
else:
    print(*ans[loc-1])


#
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
shirts = sorted([int(input()) for i in range(N)])
sailor = sorted([int(input()) for i in range(M)])

from collections import deque

cnt = 0
queue = deque(sailor)
for w in shirts:
    idx = len(queue)
    for _ in range(idx):
        temp = queue.popleft()
        if w*1/2 <= temp <= w*3/4 or w <= temp <= w*5/4:
            cnt += 1
            break
        else:
            queue.append(temp)
print(cnt)


# 17298
n = int(input())
test = divmod(n,9)
if len(str(n)) == 1:
    print(1)
else:
    if test[0]%2 == 1 and test[1]%2 == 0:
        if test[1] == 0:
            print(test[0])
        else:
            print(test[0]+2)
    elif test[0]%2 == 1 and test[1]%2 == 1:
        print(test[0]+1)
    elif test[0]%2 == 0 and test[1]%2 == 0:
        if test[1] == 0:
            print(test[0])
        else:
            print(test[0]+2)
    elif test[0]%2 == 0 and test[1]%2 == 1:
        print(test[0]+1)

######



import sys
input = sys.stdin.readline
n,chick = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

house = []
chick_house = []


for i in range(n):
    for j in range(n):
        if box[i][j] == 1:
            house.append((i,j))
        elif box[i][j] == 2:
            chick_house.append((i,j))

from itertools import combinations
result = 10**6
for chi in combinations(chick_house, chick):
    temp = 0
    for h in house:
        chi_len = 105   # maximum
        for j in range(chick):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)