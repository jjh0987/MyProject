n = int(input())
tar = [int(i) for i in input().split()]
s = 0
e = len(tar)-1

while 1:
    if tar[0] > 0:
        break
    elif tar[len(tar)-1] < 0:
        break
    else:
        check = tar[s]+tar[e]
        if check > 0:
            s += 1
        elif check < 0:
            e -= 1