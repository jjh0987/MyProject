import sys
input = sys.stdin.readline

n,ini_a = map(int,input().split())
ini_h = 0
tp = []
for _ in range(n):
    t,a,h = map(int,input().split())

    if t == 2:
        tp.append(ini_h)
        ini_a += a
        ini_h -= h
        if ini_h < 0:
            ini_h = 0
    else:
        q,r = divmod(h,ini_a)
        if r > 0:
            q += 1
        ini_h += (q-1)*a

if tp:
    print(max(max(tp),ini_h) + 1)
else:
    print(ini_h + 1)