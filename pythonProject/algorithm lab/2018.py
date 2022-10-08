import sys
input = sys.stdin.readline

n = int(input())
s = 1
e = 1

ans = 1
summation = 1
while e != n:
    if summation == n:
        ans += 1
        e += 1
        summation += e
    elif summation < n:
        e += 1
        summation += e
    else:
        summation -= s
        s += 1

print(ans)