n = int(input())

tar = '''1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1'''.split('\n')
tar = [[int(j) for j in i.split()] for i in tar]
tar

N = [1, 2, 4, 8, 16, 32, 64] # chopper
N = [i for i in N if i < n]

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
i = 0
while n > 1:
    n = n//2
    while i < 2**i:
        tar = data.popleft()
        conf = only_num(tar)
        if conf == 0:
            data.extend(chopper(tar,n))
        elif conf == 1:
            blue += 1
        else:
            white += 1
    i += 1
data