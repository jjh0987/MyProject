import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return 0
    return x


primelist = [prime(i) for i in range(2000000)]
max(primelist)