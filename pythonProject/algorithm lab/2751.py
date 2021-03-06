import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l): # n*log(n)
    sys.stdout.write(str(i)+'\n')

N = int(input())
L = []
for i in range(N):
    L.append(int(input()))

def devide_sort(L):
    x = len(L)
    if x == 1:
        return L
    mid = x//2
    g1 = devide_sort(L[:mid])
    g2 = devide_sort(L[mid:])
    target = []
    while g1 and g2:
        if g1[0] < g2[0]:
            target.append(g1.pop(0))
        else:
            target.append(g2.pop(0))
    if g2 == []:
        for i in g1:
            target.append(i)
    else:
        for i in g2:
            target.append(i)

    return target
print(devide_sort(L))
