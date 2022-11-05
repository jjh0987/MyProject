import sys
input = sys.stdin.readline
n = int(input())
# tar = [list(map(int,input().split())) for _ in range(n)]

dp_max = [0] * 3
dp_min = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3


for i in range(n):
    a,b,c = map(int,input().split())
    cal1,cal2,cal3 = min_tmp[0],min_tmp[1],min_tmp[2]
    dp_min[0] = min(cal1,cal2) + a
    dp_min[1] = min(cal1,cal2,cal3) + b
    dp_min[2] = min(cal2,cal3) + c
    min_tmp[0] = dp_min[0]
    min_tmp[1] = dp_min[1]
    min_tmp[2] = dp_min[2]

    cal1,cal2,cal3 = max_tmp[0],max_tmp[1],max_tmp[2]
    dp_max[0] = max(cal1, cal2) + a
    dp_max[1] = max(cal1, cal2, cal3) + b
    dp_max[2] = max(cal2, cal3) + c
    max_tmp[0] = dp_max[0]
    max_tmp[1] = dp_max[1]
    max_tmp[2] = dp_max[2]

print(f'{max(dp_max)} {min(dp_min)}')