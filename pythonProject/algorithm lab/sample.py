M,N = map(int,input().split())
start_x,start_y,dir = map(int,input().split())
sample = [list(map(str, input().replace('\n','').split())) for _ in range(M)]


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
x_dr = [0,-1,0,1]
y_dr = [-1,0,1,0]
# 반시계
start_dir = [x_dr[dir],y_dr[dir]]
answer = []

grid = make_grid()
answer.append(grid.pop(grid.index(start)))
while True:
    tp = 0
    cnt = -1
    for dir_ in range(4):
        tp = (dir + dir_ + 1)%4
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

        if (x_test < 0 or x_test > N-2) or (y_test < 0 or y_test > M-2):
            break


# break 지점

print(len(answer))

# 10026
n = int(input())
sample = [' '.join(input()).split(' ') for _ in range(n)]

