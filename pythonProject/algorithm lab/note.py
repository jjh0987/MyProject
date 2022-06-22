n = int(input())
target = input()

nums = [target[i] for i in range(0,n,2)]
operations = [target[i] for i in range(1,n,2)]
nums
operations
'''
nums_idx_0 = [(nums[i],nums[i+1]) for i in range(0,len(nums),2)]
nums_idx_1 = [nums[0]]
for i in range(1,len(nums),2):
    try:
        nums_idx_1.append((nums[i],nums[i+1]))
    except:
        pass
nums_idx_1.append(nums[-1])
'''
import itertools
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

group_nums = [i for i in pairwise(nums)]
pair1 = [list(group_nums[i]) for i in range(0,len(group_nums),2)]
pair2 = [list(group_nums[i]) for i in range(1,len(group_nums),2)]


pair1_sub = [] # start idx 0
pair2_sub = [] # start idx 1
for i in range(len(pair1)+1):
    pair1_sub += list(itertools.combinations(pair1,i))
for i in range(len(pair2)+1):
    pair2_sub += list(itertools.combinations(pair2,i))

pair1_sub
pair2_sub







M,N = map(int,input().split())
start_x,start_y,dir = map(int,input().split())
sample = []
for _ in range(M):
    sample.append(list(map(str,input().split())))
def make_grid():
    grid = []
    cnt_x = 0
    for i in sample:
        cnt_y = 0
        for j in i:
            if j == '0':
                grid.append((cnt_x,cnt_y))
            cnt_y += 1
        cnt_x += 1
    return grid

start = (start_x,start_y)
x_dr = [0,1,0,-1]
y_dr = [-1,0,1,0]
start_dir = [x_dr[dir],y_dr[dir]]

answer = []
grid = make_grid()

answer.append(grid.pop(grid.index(start)))
x_test,y_test = start_x,start_y
while True:


    cnt = -1
    for dir_ in range(4):
        tp = (dir - dir_ - 1)%4
        x_test = start[0] + y_dr[tp]
        y_test = start[1] + x_dr[tp]
        if (x_test,y_test) in grid:
            start = (x_test,y_test)
            answer.append(grid.pop(grid.index(start)))
            dir = tp
            break
        else:
            cnt += 1

    if cnt == 3:
        tp = (dir+2)%4
        x_test = start[0] + y_dr[tp]
        y_test = start[1] + x_dr[tp]
        start = (x_test, y_test)
        if (x_test,y_test) in grid:
            answer.append(grid.pop(grid.index(start)))
            dir = tp
            break

    if (x_test < 1) or (x_test > M - 2) or (y_test < 1) or (y_test > N - 2):
        break

print(len(answer))
