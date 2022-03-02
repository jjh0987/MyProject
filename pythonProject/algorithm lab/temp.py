# 2527
for _ in range(4):
    target = list(map(int,input().split()))
    square1_x = [target[0],target[2]]
    square1_y = [target[1],target[3]]
    square2_x = [target[4],target[6]]
    square2_y = [target[5],target[7]]

    if square1_x[0] > square2_x[1] or square1_x[1] < square2_x[0]:
        print('d')
    elif square1_y[0] > square2_y[1] or square1_y[1] < square2_y[0]:
        print('d')
    elif square1_x[0] == square2_x[1] or square1_x[1] == square2_x[0]:
        if square1_y[0] == square2_y[1] or square1_y[1] == square2_y[0]:
            print('c')
        else:
            print('b')
    elif square1_y[0] == square2_y[1] or square1_y[1] == square2_y[0]:
        if square1_x[0] == square2_x[1] or square1_x[1] == square2_x[0]:
            print('c')
        else:
            print('b')
    else:
        print('a')

# 2564
import sys
input = sys.stdin.readline
box = list(map(int,input().split()))
n = int(input())
store = []
for _ in range(n+1):
    store.append(list(map(int,input().split())))

guard = store.pop(-1)
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


LR_setting = []
for i in LR:
    temp = []
    if guard[0] == 1:
        temp.append(i[0] - (box[1] + guard[1]))
        temp.append(i[1] + (box[1] + guard[1]))
    elif guard[0] == 2:
        temp.append(i[0] + guard[1])
        temp.append(i[1] - guard[1])
    elif guard[0] == 3:
        temp.append(i[0] - (box[1] - guard[1]))
        temp.append(i[1] + (box[1] - guard[1]))
    elif guard[0] == 4:
        temp.append(i[0] - (box[0] + box[1] + guard[1]))
        temp.append(i[1] + (box[0] + box[1] + guard[1]))
    LR_setting.append(temp)

LR_setting
for i in LR_setting:
    i.sort()
    if i[0] < 0: