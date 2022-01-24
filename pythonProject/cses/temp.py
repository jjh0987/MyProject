N, M = map(int, input().split())
A = sorted([int(i) for i in input().split()])
B = [int(i) for i in input().split()]
# N+M i,j 이용

a = A[0]
b = A[-1]
temp = N // 2
for i in B:
    while 1:
        try:
            c = A[temp//2]
            if c > i:
                b = c
            elif c < i:
                a = c
            elif c == i:
                print(A.pop(A.index(c)))
                break
            elif i < a:
                print(-1)
                break
            elif i > b:
                print(A.pop(-1))
            elif c == a:
                print(A.pop(A.index(c)))
        except:
            break
