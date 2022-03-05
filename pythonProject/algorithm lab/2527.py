# 2527
for _ in range(4):
    target = list(map(int,input().split()))
    square1_x = [target[0],target[2]]
    square1_y = [target[1],target[3]]
    square2_x = [target[4],target[6]]
    square2_y = [target[5],target[7]]

    if square1_x[0] > square2_x[1] or square1_x[1] < square2_x[0]:
        print('d')
    elif square1_y[0] > square2_y[1] or square1_y[1] < square2_y[0]:
        print('d')
    elif square1_x[0] == square2_x[1] or square1_x[1] == square2_x[0]:
        if square1_y[0] == square2_y[1] or square1_y[1] == square2_y[0]:
            print('c')
        else:
            print('b')
    elif square1_y[0] == square2_y[1] or square1_y[1] == square2_y[0]:
        if square1_x[0] == square2_x[1] or square1_x[1] == square2_x[0]:
            print('c')
        else:
            print('b')
    else:
        print('a')