n,t = map(int,input().split())
A = list(map(int,input().split()))
i = 0
while i < t:
    ans = 0
    l,r = map(int, input().split())
    temp_A = A[l-1:r]
    s = list(set(temp_A))
    for i in s:
        Ks = temp_A.count(i)
        ans += Ks*Ks*i
    print(ans)
    i += 1