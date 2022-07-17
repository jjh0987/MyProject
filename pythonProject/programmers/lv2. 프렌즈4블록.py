
def solution1(M, N, board):


    board = [' '.join(i).split() for i in board]


    def cp_board(board):
        board_init = []
        for i in range(M):
            tp = []
            for j in range(N):
                tp.append(board[i][j])
            board_init.append(tp)
        return board_init

    while True:
        tp_list = set()
        init_board = cp_board(board)
        for i in range(M):
            for j in range(N):
                try:

                    if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]) and board[i][j] != 'X':
                        tp_list.add((i,j))
                        tp_list.add((i,j+1))
                        tp_list.add((i+1,j))
                        tp_list.add((i+1,j+1))

                except:
                    pass

        for grid in list(tp_list):
            board[grid[0]][grid[1]] = 'x'

        while True:
            copy_board = cp_board(board)
            for i in range(M):
                for j in range(N):
                    if board[i][j] == 'x' and i > 0:
                        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                    else:
                        continue
            if board == copy_board:
                break
        if board == init_board:
            break

    cnt = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 'x':
                cnt += 1
    return cnt