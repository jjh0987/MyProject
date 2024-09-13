import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
s = 1
e = max(tree)
while 1:
    mid = (s + e) // 2
    check = 0
    if check < m:
        e = int(mid) - 1
    elif check > m:
        s = int(mid) + 1
    else:
        print(mid)
        break
