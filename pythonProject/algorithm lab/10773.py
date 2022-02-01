import sys
n = int(input())
ans = []
data = [int(sys.stdin.readline()) for i in range(n)]
for i in data:
    if i == 0:
        ans.pop(-1)
    else:
        ans.append(i)
print(sum(ans))



n = int(input())
ans = []
for i in range(n):
    x = int(input())
    if x == 0:
        ans.pop(-1)
    else:
        ans.append(x)
print(sum(ans))
