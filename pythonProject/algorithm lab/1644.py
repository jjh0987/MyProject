import math
n = int(input())
answer = 0
prime = [i for i in range(n+1)] # 4*10**6
prime[1] = 0
for j in range(2, int(math.sqrt(len(prime)))+1):
    if prime[j] == 0:
        continue
    for j in range(2*j,len(prime),j):
        prime[j] = 0
prime[0] = 99
prime = [i for i in prime if i != 0 and i > 0]
prime[0] = 0
for i in range(1,len(prime)):
    prime[i] += prime[i-1]

for i in range(len(prime)-1,-1,-1):
    for j in range(i-1,-1,-1):
        tp = prime[i]-prime[j]
        if tp == n:
            answer += 1
        elif tp > n:
            break
print(answer)
