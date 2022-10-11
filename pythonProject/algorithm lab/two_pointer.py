import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int,input().split())))

cnt = 0

for k in range(len(A)):
    i = 0
    j = n-1
    while i < j:
        if A[i]+A[j] == A[k]:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i]+A[j] < A[k]:
            i += 1
        elif A[i]+A[j] > A[k]:
            j -= 1

print(cnt)