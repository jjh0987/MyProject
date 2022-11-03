import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return
    return x

n = int(input())
import sys
limit_number = 10**9
sys.setrecursionlimit(limit_number)

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1,10):
            if prime(num*10+i):
                dfs(prime(num*10+i))

dfs(2)
dfs(3)
dfs(5)
dfs(7)


