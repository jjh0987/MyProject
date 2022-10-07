import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

S = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        S[i][j] += S[i][j-1] + S[i-1][j] + A[i-1][j-1] - S[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])





S[3][4] - S[1][4] - S[3][1] + S[1][1]
S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
A
S


import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

S = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        S[i][j] += S[i][j-1] + S[i-1][j] + A[i-1][j-1] - S[i-1][j-1]

for _ in range(m):
    tar = list(map(int,input().split()))
    if tar[0] == 0:
        fix = A[tar[1]-1][tar[2]-1] - tar[3]
        A[tar[1]-1][tar[2]-1] = tar[3]
        for i in range(tar[1],n+1):
            for j in range(tar[2],n+1):
                if fix >= 0:
                    S[i][j] += fix
                else:
                    S[i][j] -= fix
    elif tar[0] == 1:
        x1,y1,x2,y2 = tar[1:]
        if x1 == x2 and y1 == y2:
            print(A[x1-1][y1-1])
        else:
            print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])

x1,x2 = [2,2]
tar[1:]
S