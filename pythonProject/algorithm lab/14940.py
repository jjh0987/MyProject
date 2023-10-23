import collections
n,m = 15,15
target = '''2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1'''

import sys
import collections
input = sys.stdin.readline
n,m = map(int,input().split())
target = [[int(j) for j in input().split()] for _ in range(n)]
sudo = [[False for _ in range(m)] for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if target[i][j] == 0:
            sudo[i][j] = True
def starting_point():
    for i in range(n):
        for j in range(m):
            if target[i][j] == 2:
                return i,j

x,y = list(starting_point())

tars = collections.deque()
tars.append([list(starting_point())])
lv = 0
while tars:
    tar = tars.popleft()
    tp = []
    for i in tar:
        if i[0] < 0 or i[0] >= n or i[1] < 0 or i[1] >= m \
                or sudo[i[0]][i[1]] == True or target[i[0]][i[1]] == 0:
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

for i in range(n):
    for j in range(m):
        if sudo[i][j] == False:
            answer[i][j] = -1

for i in answer:
    print(*i)

