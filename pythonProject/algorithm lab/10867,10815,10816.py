# 10867
import sys
input = sys.stdin.readline
n = int(input())
line = set(map(int,input().split()))
ans = ''
for i in sorted(line):
    ans += f'{i} '
print(ans)

# 10815
import sys
input = sys.stdin.readline
n = int(input())
line1 = set(map(int,input().split()))
m = int(input())
line2 = list(map(int,input().split()))

ans = ''
for i in line2:
    if i in line1:
        ans += '1 '
    else:
        ans += '0 '
print(ans)

# 10816
import sys
input = sys.stdin.readline
n = int(input())
line1 = list(map(int,input().split()))
m = int(input())
temp = list(map(int,input().split()))
line2 = {i:0 for i in temp}

for i in line1:
    if i in line2.keys():
        line2[i] += 1
    else:
        pass

ans = ''
for i in temp:
    ans += f'{line2[i]} '
print(ans)