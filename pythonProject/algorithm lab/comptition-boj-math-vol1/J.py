a, b = map(int, input().split())
import math

prime = [i for i in range(10 ** 6 + 1)]
prime[1] = 0
for j in range(2, int(math.sqrt(len(prime))) + 1):
    if prime[j] == 0:
        continue
    for j in range(2 * j, len(prime), j):
        prime[j] = 0

prime = [i**2 for i in prime if i > 1]
target = [0]
target.extend(list(range(a,b+1)))

for i in range(1,len(target)):
    if target[i] == 0:
        continue
    i = 1
    for j in range(len(prime)):
        if target[i] % prime[j] == 0:
            for k in range(len(target)):
                try:
                    target[i+prime[j]*k] = 0
                except:break
            break

for i in range(len(prime)):
    for j in range(len(target)):
        if target[i] == 0:
            continue
        if target[j] % prime[i] == 0:



print(len([i for i in target if i > 0]))