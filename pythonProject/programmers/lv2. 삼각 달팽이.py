n = 7

mapping = [[0 for _ in range(n)] for _ in range(n)]
tp = 0
mapping[0][0] = 1


x = 0
lv = 0
while lv < 3:
    for i in range(1+lv,n-lv):
        mapping[i][lv] = mapping[i-1][lv] + 1
    for j in range(1+lv,n-lv):
        mapping[i-lv][j] = mapping[i-lv][j-1] + 1
    for k in range(1,n-1):
        mapping[i-k][j-k] = mapping[i-k+1][j-k+1] + 1

    x += 1
    lv += 1
    mapping[0+2*x][0+x] = 1 + mapping[1+2*(x-1)][1+(x-1)]



n = 3
mapping = [[0 for _ in range(n)] for _ in range(n)]

i = 0
j = 0
tp = 0
lv = 0
while lv < divmod(n,3)[0]+1:
    while 1:
        try:
            if mapping[i][j] == 0:
                tp += 1
                mapping[i][j] += tp
                i += 1
            else:
                i -= 1
                break
        except:
            i -= 1
            break
    while 1:
        try:
            if mapping[i][j+1] == 0:
                tp += 1
                j += 1
                mapping[i][j] += tp
            else:
                break
        except:
            break
    while 1:
        if mapping[i-1][j-1] == 0:
            tp += 1
            i -= 1
            j -= 1
            mapping[i][j] += tp
        else:
            break
    i += 1
    lv += 1

answer = []
for i in mapping:
    for j in i:
        if j != 0:
            answer.append(j)
