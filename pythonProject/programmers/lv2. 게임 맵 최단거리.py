maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# maps = [[1 for _ in range(100)] for _ in range(100)]
n = len(maps)
m = len(maps[0])
# visited = [[False for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

from collections import deque
que = deque([[0,0]])
while que:
    ox,oy = que.popleft()
    # visited[tar[0]][tar[1]] = True
    for idx in range(4):
        x = ox + dx[idx]
        y = oy - dy[idx]
        if x >= 0 and x < n and y >= 0 and y < m:
            if maps[x][y] == 1:
                que.append([x,y])
                maps[x][y] = maps[ox][oy]+1

maps
