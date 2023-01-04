N = 8
A = 8
B = 7

if A > B:
    A,B = B,A

import math
cnt = int(math.log2(N))

check = N//2

while 1:
    if check >= A and check < B:
        break
    else:
        cnt -= 1
        if A >= check and B >= check:
            check += 2**(cnt-1)
        else:
            check -= 2**(cnt-1)