T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    length = ((x1-x2)**2+(y1-y2)**2)
    R = (r1+r2)**2
    if length > R:
        print(0)
    elif length == R:
        print(1)
    elif length == 0 and r1 == r2:
        print(-1)
    else:
        if length < (max(r1,r2) - min(r1,r2))**2:
            print(0)
        elif length == (max(r1,r2) - min(r1,r2))**2:
            print(1)
        else:
            print(2)