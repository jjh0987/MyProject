n = int(input())

import math
def prime(x):
    for j in range(2,int(math.sqrt(x))+2):
        if x%j == 0:
            return
    return x

if n == 1:
    print(2)
elif n == 2:
    print(2)
else:
    for i in range (n,1005001):
        tar = prime(i)
        if tar:
            tar = list(str(tar))
            if tar == list(reversed(tar)):
                print(''.join(tar))
                break

