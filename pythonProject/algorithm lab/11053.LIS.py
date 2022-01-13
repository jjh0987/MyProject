N = int(input())
A = list(map(int,input().split()))

LIS = [1]*N
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i],LIS[j]+1)
            # LIS[i] 또한 계속 변하게되므로 비교대상이다.
print(max(LIS))

