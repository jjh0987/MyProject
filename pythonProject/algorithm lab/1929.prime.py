N,M = map(int,input().split())
import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return
    return x

if N == 1 or N == 2:
    if M == 1:
        pass
    print(2)
for i in range(N,M+1):
    if i > 2:
        if prime(i) == None:
            pass
        else:
            print(prime(i))

#에라토스테네스의 체