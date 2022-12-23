brown = 24
yellow = 24

box = brown+yellow

import math
for i in range(1,int(math.sqrt(box))+2):
    if (box//i)*i == box:
        if ((box//i)-2)*(i-2) == yellow:
            ans = [box//i,i]

print(sorted(ans,reverse=True))