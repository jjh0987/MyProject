import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    tp = (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
    if tp > 0:
        return 1
    elif tp < 0:
        return -1
    else:
        return 0

check1 = ccw(x1,y1,x2,y2,x3,y3)
check2 = ccw(x1,y1,x2,y2,x4,y4)
check3 = ccw(x3,y3,x4,y4,x1,y1)
check4 = ccw(x3,y3,x4,y4,x2,y2)

def find_line(x1,y1,x2,y2):
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    return a,b

try:
    a1,b1 = find_line(x1,y1,x2,y2)
    a2,b2 = find_line(x3,y3,x4,y4)
except:pass

if check1*check2 == 1 or check3*check4 == 1:
    print(0)
else:
    if min(x1,x2) > max(x3,x4) or min(x3,x4) > max(x1,x2) or min(y1,y2) > max(y3,y4) or min(y3,y4) > max(y1,y2):
        print(0)
    else:
        print(1)
        try:
            tp = (b2-b1)/(a1-a2)
            print(tp,tp*a1+b1)
        except:
            if x1 == x3 and y1 == y3:
                print(x1,y1)
            elif x1 == x4 and y1 == y4:
                print(x1,y1)
            elif x2 == x3 and y2 == y3:
                print(x2,y2)
            elif x2 == x4 and y2 == y4:
                print(x2,y2)