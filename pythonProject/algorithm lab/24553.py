import sys
input = sys.stdin.readline
T = int(input())

def isP(x):
    tp = ''
    for i in range(len(x)//2):
        a,b = int(x[i]),int(x[-i-1])
        if x[i] != x[-i-1]:
            tp += f'{min(a,b)}'
        else:
            pass



for _ in range(T):
    s = input().rstrip('\n')
    p_number = s[:len(s)//2] + s[len(s)//2-1::-1]