import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return
    return x

N = 1
M = 1000
p = set()
p.add(2)
for i in range(N,M+1):
    if i > 2:
        if prime(i) == None:
            pass
        else:
            p.add(prime(i))
N = int(input())
nums = list(map(int,input().split()))
cnt = 0
for i in nums:
    if i in p:
        cnt+=1
print(cnt)