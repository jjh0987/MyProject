# 2309
height_list = []
for _ in range(9):
    height_list.append(int(input()))

height_list.sort()
pair_list = []
for i in range(9):
    for j in range(i+1,9):
        temp = []
        temp.append(height_list[i])
        temp.append(height_list[j])
        pair_list.append(temp)

sum_height_list = sum(height_list)

sum_pair = [sum(i) for i in pair_list]
idx = 0
for i in sum_pair:
    if sum_height_list - i == 100:
        break
    else:
        idx += 1

target = set(pair_list[idx])
for i in height_list:
    if i not in target:
        print(i)

# 2116
import sys
input = sys.stdin.readline
n = int(input())
dice_pair = []
for _ in range(n):
    target = list(map(int,input().split()))
    temp = [sorted([target[0],target[5]]),sorted([target[1],target[3]]),sorted([target[2],target[4]])]
    dice_pair.append(temp)

floor_pt = list(range(1,7))
ans_set = []
for i in floor_pt:
    ans = 0
    floor = i
    for j in range(n):
        temp = []
        for k in dice_pair[j]:
            if floor in k:
                for x in k:
                    if floor != x:
                        floor = x
                        break
            else:
                temp += k
        ans += max(temp)
    ans_set.append(ans)
print(max(ans_set))