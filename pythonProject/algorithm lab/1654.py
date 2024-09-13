import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

s = 1
e = max(lan)
while s <= e:
    mid = (s + e) // 2
    check = sum([i // mid for i in lan])
    if check < n:
        e = int(mid) - 1
    else:
        s = int(mid) + 1

print(e)