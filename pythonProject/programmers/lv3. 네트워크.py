n = 3
network = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
network
# network = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
network = [[1,0,1],[0,1,0],[1,0,1]] # 양방향 필요
# mapping = [[False for _ in range(n)] for _ in range(n)]
answer = 0
def dfs(x,y):
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return
    if network[x][y] == -1:
        return

    if network[x][y] == 1:
        network[x][y] = -1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)


for i in range(n):
    for j in range(n):
        if network[i][j] == 1:
            answer += 1
            dfs(i,j)

network
