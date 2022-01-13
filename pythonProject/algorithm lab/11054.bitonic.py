N = int(input())
A = list(map(int,input().split()))

LIS = [1]*N
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i],LIS[j]+1)
ans1 = LIS

A.reverse()
LIS = [1]*N
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i],LIS[j]+1)
ans2 = LIS
ans2.reverse()

ans = 0
for i in range(N):
    ans = max(ans,ans1[i]+ans2[i]-1)
print(ans)