import sys
import collections
input = sys.stdin.readline
n,m = map(int,input().split())
target = [[int(j) for j in input().split()] for _ in range(m)]
sudo = [[False for _ in range(n)] for _ in range(m)]
answer = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if target[i][j] == -1:
            sudo[i][j] = True

tp = []
for i in range(m):
    for j in range(n):
        if target[i][j] == 1:
            tp.append([i,j])
tars = collections.deque([tp])

lv = 0
while tars:
    tar = tars.popleft()
    tp = []
    for i in tar:
        if i[0] < 0 or i[0] >= m or i[1] < 0 or i[1] >= n \
                or sudo[i[0]][i[1]] == True: # or target[i[0]][i[1]] == 0:
            pass
        else:
            sudo[i[0]][i[1]] = True
            answer[i[0]][i[1]] = lv
            tp.append([i[0]+1,i[1]])
            tp.append([i[0],i[1]+1])
            tp.append([i[0]-1,i[1]])
            tp.append([i[0],i[1]-1])
    if tp:
        tars.append(tp)
    lv += 1

if sum([len([j for j in i if j == False]) for i in sudo]) > 0:
    print(-1)
else:
    print(max([max(i) for i in answer]))

target
sudo
answer