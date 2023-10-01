import sys
input = sys.stdin.readline

n = int(input())
tar = [list(map(int,input().split())) for i in range(n)]

def chopper(tar,chop_len):
    s1 = [i[:chop_len] for i in tar[:chop_len]]
    s2 = [i[chop_len:] for i in tar[:chop_len]]
    s3 = [i[:chop_len] for i in tar[chop_len:]]
    s4 = [i[chop_len:] for i in tar[chop_len:]]
    return s1,s2,s3,s4

def only_num(target):
    confirm = len(target[0])*len(target[0])
    temp = sum([sum(i) for i in target])
    # blue = 0
    # white = 0
    if temp == confirm:
        # blue += 1
        return 1
    elif temp == 0:
        # white += 1
        return -1
    else:
        return 0

from collections import deque
blue = 0
white = 0

data = deque([tar])
while data:
    tar = data.popleft()
    flag = only_num(tar)
    if len(tar) == 1:
        if tar[0][0] == 1:
            blue += 1
        else:
            white += 1
    else:
        if flag == 0:
            try:
                data.extend(chopper(tar,int(len(tar)/2)))
            except:
                pass
        elif flag == 1:
            blue += 1
        else:
            white += 1

print(white)
print(blue)