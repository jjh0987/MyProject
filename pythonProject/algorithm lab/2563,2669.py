# 2 차 list comp
n = 5
ls = [list(map(int,input().split())) for _ in range(n)]

# 2563
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]

box_mapping = []
for target in box:
    x_range = list(range(target[0],target[0]+10))
    y_range = list(range(target[1],target[1]+10))
    target_map = [[i,j] for i in x_range for j in y_range]
    box_mapping.append(target_map)

for i in range(n):
    try:
        for j in range(i+1,n):
            for k in range(len(box_mapping[i])):
                if box_mapping[i][k] in box_mapping[j]:
                    box_mapping[j].pop(box_mapping[j].index(box_mapping[i][k]))
    except:
        pass

print(sum([len(i) for i in box_mapping]))


# 2669
box = [list(map(int,input().split())) for _ in range(4)]

box_mapping = []
for target in box:
    x_range = list(range(target[0],target[2]))
    y_range = list(range(target[1],target[3]))
    target_map = [[i,j] for i in x_range for j in y_range]
    box_mapping.append(target_map)

for i in range(4):
    try:
        for j in range(i+1,4):
            for k in range(len(box_mapping[i])):
                if box_mapping[i][k] in box_mapping[j]:
                    box_mapping[j].pop(box_mapping[j].index(box_mapping[i][k]))
    except:
        pass

print(sum([len(i) for i in box_mapping]))