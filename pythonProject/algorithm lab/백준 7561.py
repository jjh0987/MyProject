import sys
input = sys.stdin.readline
n = int(input())

def det(M):
    return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])\
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])\
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])

for _ in range(n):
    matrix = []
    for _ in range(3):
        matrix.append(list(map(int,input().split())))
    A = [i[:3] for i in matrix]

    v1 = [i[0] for i in matrix]
    v2 = [i[1] for i in matrix]
    v3 = [i[2] for i in matrix]
    b = [i[3] for i in matrix]

    A1 = []
    A1.append(b)
    A1.append(v2)
    A1.append(v3)

    A2 = []
    A2.append(v1)
    A2.append(b)
    A2.append(v3)

    A3 = []
    A3.append(v1)
    A3.append(v2)
    A3.append(b)
    da1, da2, da3, da = det(A1), det(A2), det(A3), det(A)
    if det(A) == 0:
        print(da1, da2, da3, da)
        print('No unique solution')
        print('')
    else:
        tp1 = '{:.3f}'.format(round(da1/da,3))
        tp2 = '{:.3f}'.format(round(da2/da,3))
        tp3 = '{:.3f}'.format(round(da3/da,3))
        if tp1 == '-0.000':
            tp1 = '0.000'
        if tp2 == '-0.000':
            tp2 = '0.000'
        if tp3 == '-0.000':
            tp3 = '0.000'
        print(da1, da2, da3, da)
        print(f'Unique solution: {tp1} {tp2} {tp3}')
        print('')