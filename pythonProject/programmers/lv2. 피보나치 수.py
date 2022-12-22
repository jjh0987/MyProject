def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1)%1234567 + fibo(x-2)%1234567

fibo(20)

n = 100
ans = [0,1]
for i in range(2,n+1):
    ans.append(ans[i-1]+ans[i-2])

print(ans[-1])