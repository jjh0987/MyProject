a, b = map(int, input().split())
import math

prime = [i for i in range(10 ** 12 + 1)]
prime[1] = 0
for j in range(2, int(math.sqrt(len(prime))) + 1):
    if prime[j] == 0:
        continue
    for j in range(2 * j, len(prime), j):
        prime[j] = 0

prime = [i for i in prime if i > 1]

