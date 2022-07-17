import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(input()) for _ in range(n)]
RnG_graph = []
for i in range(n):
    tp = []
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            tp.append('R')
        else:
            tp.append('B')
    RnG_graph.append(tp)


def dfs(x,y,color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] in color:
        graph[x][y] = 'V'
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True
    return False

def dfs_rng(x,y,color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if RnG_graph[x][y] in color:
        RnG_graph[x][y] = 'V'
        dfs_rng(x-1,y,color)
        dfs_rng(x,y-1,color)
        dfs_rng(x+1,y,color)
        dfs_rng(x,y+1,color)
        return True
    return False



cnt1 = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j,['R']) == True:
            cnt1 += 1
        if dfs(i, j, ['G']) == True:
            cnt1 += 1
        if dfs(i,j,['B']) == True:
            cnt1 += 1
cnt2 = 0
for i in range(n):
    for j in range(n):
        if dfs_rng(i,j,['R']) == True:
            cnt2 += 1
        if dfs_rng(i,j,['B']) == True:
            cnt2 += 1

print(cnt1,cnt2)
