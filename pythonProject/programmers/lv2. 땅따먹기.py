land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]


# dp = [i for i in land[0]]

for i in range(1,len(land)):
    land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
    land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
    land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
    land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])

