A = [1,4,2]
B = [5,4,4]
ans = 0
A.sort()
B.sort()
for i in range(len(A)):
    ans += A[i]*B[i]