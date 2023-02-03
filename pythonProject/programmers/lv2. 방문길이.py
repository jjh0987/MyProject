dirs = "ULURRDLLU"
dirs = "LULLLLLLU"

node = [[5,5]]
for d in dirs:
    tar = [i for i in node[-1]]
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
    if tar == node[-1]:
        continue
    if tar in node:
        node.append(1)

    node.append(tar)

node