def factorial(n):
    if n == 1:
        return 1
    else:
        ans = n*factorial(n-1)
        return ans

target = ','.join(str(factorial(int(input())))).split(',')
target.reverse()
cnt = 0
for i in target:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)

N = int(input())
ans = 1
for i in range(1,N+1):
    ans = ans*i

target = ','.join(str(ans)).split(',')
target.reverse()
cnt = 0
for i in target:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)