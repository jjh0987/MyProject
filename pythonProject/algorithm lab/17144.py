import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())
mapping = []
for _ in range(r):
    mapping.append(list(map(int,input().split())))

# data = '''0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0'''
# mapping = [list(map(int,i.split())) for i in data.split('\n')]

for _ in range(t):
    visited = [[0 for _ in range(c)] for _ in range(r)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    aero = []
    for j in range(c):
        for i in range(r):
            if mapping[i][j] == -1:
                visited[i][j] = -1
                aero.append(i)
                continue
            if mapping[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if x < 0 or y < 0 or x >= r or y >= c or mapping[x][y] == -1:
                    cnt += 1
                    continue
                visited[x][y] += mapping[i][j]//5
            visited[i][j] -= mapping[i][j]//5 * (4-cnt)
            visited[i][j] += mapping[i][j]

    mapping = [[j for j in i] for i in visited]

    for i in range(1,aero[0]):
        visited[i][0] = mapping[i-1][0]
    visited[aero[0]][0] = -1
    for i in range(1,c):
        visited[0][i-1] = mapping[0][i]
    for i in range(1,aero[0]+1):
        visited[i-1][-1] = mapping[i][-1]
    for i in range(2,c):
        visited[aero[0]][i] = mapping[aero[0]][i-1]
    visited[aero[0]][1] = 0
    for i in range(aero[1],r-1):
        visited[i][0] = mapping[i+1][0]
    visited[aero[1]][0] = -1
    for i in range(1,c):
        visited[-1][i-1] = visited[-1][i]
    for i in range(r-1,aero[1],-1):
        visited[i][-1] = visited[i-1][-1]
    for i in range(2,c):
        visited[aero[1]][i] = mapping[aero[1]][i-1]
    visited[aero[1]][1] = 0
    mapping = [[j for j in i] for i in visited]
print(sum([sum(i) for i in mapping])+2)
