N,M,K = map(int,input().split())
A = sorted([int(i) for i in input().split()])
B = sorted([int(i) for i in input().split()])
# N+M i,j 이용

i = 0
j = 0
cnt = 0
while i+j < N+M:
    try:
        if abs(B[j]-A[i]) <= K:
            cnt += 1
            i += 1
            j += 1
        elif B[j]-A[i] > K:
            i += 1
        else:
            j += 1
    except:break
print(cnt)