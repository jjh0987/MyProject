for i in range(int(input())):
    f0 = [1, 0]
    f1 = [0, 1]
    a = int(input())
    if a == 0:
        print(f0[0],f0[1])
    elif a == 1:
        print(f1[0],f1[1])
    else:
        for i in range(a-1):
            tempf0 = f0
            f0 = f1
            f1 = [tempf0[0]+f0[0],tempf0[1]+f0[1]]
        print(f1[0],f1[1])

