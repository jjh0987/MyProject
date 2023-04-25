park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]

from copy import deepcopy
for i in range(len(park)):
    for j in range(len(park[0])):
        if park[i][j] == 'S':
            starting = [i,j]
            break


park = [list(i) for i in park]
routes = [i.split() for i in routes]

for i in routes:
    k = 0
    tp = deepcopy(starting)
    if i[0] == 'E':
        while k < int(i[1]):
            starting[1] += 1
            k += 1
            if starting[1] == len(park[0]):
                starting = tp
                break
            if park[starting[0]][starting[1]] == 'X':
                starting = tp
                break
    elif i[0] == 'W':
        while k < int(i[1]):
            starting[1] -= 1
            k += 1
            if starting[1] < 0:
                starting = tp
                break
            if park[starting[0]][starting[1]] == 'X':
                starting = tp
                break
    elif i[0] == 'S':
        while k < int(i[1]):
            starting[0] += 1
            k += 1
            if starting[0] == len(park):
                starting = tp
                break
            if park[starting[0]][starting[1]] == 'X':
                starting = tp
                break
    elif i[0] == 'N':
        while k < int(i[1]):
            starting[0] -= 1
            k += 1
            if starting[0] < 0:
                starting = tp
                break
            if park[starting[0]][starting[1]] == 'X':
                starting = tp
                break