n = int(input())
import math
answer = []
for a in range(1,317):
    for b in range(0,317):
        tar = n-a**2-b**2
        if tar >= 0:
            once = math.sqrt(tar)
            if a**2+b**2 == n:
                answer.append([a,b])
            elif once-int(once) == 0:
                answer.append([a,b,int(once)])
        else:break
if answer:
    print(min([len([j for j in i if j>0]) for i in answer]))
else:
    print(4)

317**2