import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
A.sort()
i = 0
j = 1
k = 2

cnt = 0
if n < 3:
    print(0)
else:
    while k != n:
        if A[i]+A[j] == A[k]:
            cnt += 1
            k += 1
        elif i-1 == j:
            j += 1
        elif A[i]+A[j] < A[k]:
            if i-1 == j:
                j += 1
                i += 1
            else:
                i+=1
        elif A[i]+A[j] > A[k]:
            k += 1

    print(cnt)