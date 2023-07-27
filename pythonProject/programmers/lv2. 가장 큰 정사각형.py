board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,0]]
board = [[1,1,1,0],[1,1,1,0],[1,1,1,1],[1,1,1,1]]
for i in range(1,len(board)):
    for j in range(1,len(board[0])):
        try:
            if board[i-1][j-1] != 0:
                tar = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1])
                if tar > 0:
                    if board[i][j] == 1:
                        board[i][j] = tar + 1
        except:
            pass
max([max(i) for i in board])

print(*board,sep='\n')