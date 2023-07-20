board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board

for i in range(1,len(board)):
    for j in range(1,len(board[0])):
        try:
            if board[i][j] != 0:
                if min(board[i-1][j],board[i][j-1],board[i-1][j-1]) > 0:
                    board[i][j] += board[i-1][j-1]
        except:
            pass
max([max(i) for i in board])

print(*board,sep='\n')