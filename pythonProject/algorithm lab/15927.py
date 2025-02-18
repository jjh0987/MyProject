import sys
input = sys.stdin.readline
s = input().rstrip('\n')
if len(s)%2 == 1:
    odd = True
    marking = [0 for _ in range(len(s)//2+1)]
else:
    odd = False
    marking = [0 for _ in range(len(s)//2)]

def isP(x):
    for i in range(len(x)//2):
        if x[i] == x[-i-1]:
            marking[i] = 1
    if odd:
        marking[len(x)//2] = 1
isP(s)

try:
    print((len(marking)-marking.index(0))*2)
except:
    print((len(marking)-marking.index(1)-1)*2)
