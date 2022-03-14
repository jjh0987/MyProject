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


