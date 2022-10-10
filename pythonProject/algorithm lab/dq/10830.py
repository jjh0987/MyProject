n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def mul(L,R):
    tp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for fix in range(n):
                tp[i][j] += (L[i][fix]*R[fix][j])%1000
    return tp

def divided(A,B):
    if B == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] = A[i][j]%1000
        return A

    tp = divided(A,B//2)

    if B%2:
        return mul(mul(tp,tp),A)
    else:
        return mul(tp,tp)

ans = divided(matrix,m)
for i in ans:
    check = [j%1000 for j in i]
    print(*check)