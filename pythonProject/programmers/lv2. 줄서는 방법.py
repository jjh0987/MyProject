n = 20
k = 5


k -= 1
number = [i for i in range(1,n+1)]
import math

fact = [math.factorial(i) for i in range(1,n)]
answer = []
for i in range(n,0,-1):
    tar = number.pop(k//fact[i-2])
    answer.append(tar)
    k %= fact[i-2]

answer
fact