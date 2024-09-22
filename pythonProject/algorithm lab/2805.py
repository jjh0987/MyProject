import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

s = 1
e = max(tree)
while s <= e:
    mid = (s + e) // 2
    check = sum([i-mid for i in tree if i-mid > 0])
    if check < m:
        e = int(mid) - 1
    else:
        s = int(mid) + 1
print(e)