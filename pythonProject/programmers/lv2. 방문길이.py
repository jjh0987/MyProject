dirs = "ULURRDLLU"

route = [[5,5],[5,5]]
for d in dirs:
    route.append(route[-1])
    tar = route.pop()
    if d == 'U':
        if tar[0] < 11:
            tar[0] += 1
    elif d == 'D':
        if tar[0] > 0:
            tar[0] -= 1
    elif d == 'R':
        if tar[1] < 11:
            tar[1] += 1
    elif d == 'L':
        if tar[1] > 0:
            tar[1] -= 1
    route.append([i for i in tar])


box = [[0,0],[0,0]]
grid = [[[i for i in box] for _ in range(10)] for _ in range(10)]
