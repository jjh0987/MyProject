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
sample.append([' ' for _ in range(n)])
def horizon(row,color):
    lst = []
    for i in range(n):
        if row[i] in set(color):
            lst.append(i)
        else:
            lst.append(' ')
    return lst

R = []
G = []
B = []
for i in range(n+1):
    for color in ['R','G','B']:
        if color == 'R':
            R.append(horizon(sample[i],[color]))
        elif color == 'G':
            G.append(horizon(sample[i],[color]))
        elif color == 'B':
            B.append(horizon(sample[i],[color]))


col_set = [R,G,B]
cnt1 = 0
for col in col_set:
    for i in range(n):
        try:
            if col[i] == set():
                continue
            if col[i].intersection(col[i+1]) == set():
                cnt1 += 1
        except:
            pass

RnG = []
B = []
for i in range(n + 1):
    for color in [['R', 'G'], 'B']:
        if color == ['R','G']:
            RnG.append(horizon(sample[i], color))
        elif color == 'B':
            B.append(horizon(sample[i], [color]))

col_set = [RnG, B]
cnt2 = 0
for col in col_set:
    for i in range(n):
        try:
            if col[i] == set():
                continue
            if col[i].intersection(col[i + 1]) == set():
                cnt2 += 1
        except:
            pass
print(cnt1,cnt2)




import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
graph = [list(input()) for _ in range(n)]

def search(row):
    idx = set()
    for i in range(n):
        if row[i] == 'R':
            idx.add(i)
            row[i] = 'G'
            try:
                if row[i+1] != 'R':
                    continue
            except:
                break
    return idx
cnt1 = 0
tp = [search(graph[i]) for i in range(n)]
for i in range(n):
    try:
        if len(tp[i].intersection(tp[i+1])) != 0:
            cnt1 += 1

    except:
        break


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
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
        dfs(x-1, y-1, color)
        dfs(x+1, y-1, color)
        dfs(x+1, y+1, color)
        dfs(x-1, y+1, color)
    return tp
w = 1

while w != 0:
    island = []
    tp = []
    w,h = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'x' or maps[i][j] == 0:
                tp = []
                continue
            else:
                island.append(dfs(i,j,1))
    if w != 0:
        print(len(island))
    else:
        pass