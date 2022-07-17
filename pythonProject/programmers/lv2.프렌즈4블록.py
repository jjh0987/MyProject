n,m = map(int,input().split())
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board = [list(i) for i in board]
board
tp = []

def dfs(x,y,color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if board[x][y] == 'A':
        tp.append((x,y))
        board[x][y] = 'V'
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True,tp
    return False

cnt1 = 0
con,tp = dfs(2,2,'A')
