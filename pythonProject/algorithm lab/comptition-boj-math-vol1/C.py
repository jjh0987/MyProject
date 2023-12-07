import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
pt = list(map(int,input().split()))

import math
const = 180/math.pi
# [[i[0]-pt[0],i[1]-pt[1]] for i in data]
angle_set = set()
for x,y in data:
    angle = math.atan2(x,y)*const
    if angle < 0:
        angle = 360 + angle
    angle_set.add(angle)

tar_dict = {i:[] for i in list(angle_set)}
for x,y in data:
    angle = math.atan2(x,y)*const
    if angle < 0:
        angle = 360 + angle
    d = math.dist([x,y],pt)
    tar_dict[angle].append([x,y,d])

for i in tar_dict:
    tar_dict[i].sort(key=lambda x:x[2])

for tar in sorted(tar_dict.items(),reverse=True):
    print(tar[1][0][0],tar[1][0][1])

tar_dict