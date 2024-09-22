import sys

input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))
m = int(input())

s = 1
e = max(tree)
cnt = len(tree)
while s <= e:
    mid = (s + e) // 2
    check = 0
    for i in tree:
        if i <= mid:
            check += i
        else:
            check += mid
    if check <= m:
        s = int(mid) + 1
    else:
        e = int(mid) - 1
print(e)