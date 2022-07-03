# 1931
import sys
n = int(input())
input = sys.stdin.readline
clock = [list(map(int,input().split())) for _ in range(n)]
clock.sort(key=lambda x:(x[1],x[0]))

start,end = clock[0][0],clock[0][1]
if start == end:
    cnt = 0
else:
    cnt = 1

for i in clock:
    if end <= i[0]:
        end = i[1]
        cnt += 1
print(cnt)