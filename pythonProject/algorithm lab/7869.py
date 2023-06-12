x1,y1,r1,x2,y2,r2 = [float(i) for i in input().split()]
import math
d = math.sqrt((x1-x2)**2+(y1-y2)**2)

if d > r2+r1:
    print('0.000')
elif d <= abs(r1 - r2) and r1 <= r2:
    print(math.pi*(r1**2))
elif d <= abs(r1 - r2) and r2 < r1:
    print(math.pi*(r2**2))
else:
    theta1 = 2*math.acos((d**2+r1**2-r2**2)/(2*d*r1))
    theta2 = 2*math.acos((d**2+r2**2-r1**2)/(2*d*r2))
    s1 = 1/2*(r1**2)*theta1+1/2*(r2**2)*theta2
    s2 = 1/2*(r1**2)*math.sin(theta1)+1/2*(r2**2)*math.sin(theta2)
    if s1-s2 == 0:
        print('0.000')
    else:
        print(round(1000*(s1-s2),3))

