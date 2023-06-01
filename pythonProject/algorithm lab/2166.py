import sys
input = sys.stdin.readline
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
points.sort()

import math
def find_length(pt1,pt2):
    return math.sqrt((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)
def triangle(pt1,pt2,pt3):
    a = find_length(pt1,pt2)
    b = find_length(pt2,pt3)
    c = find_length(pt3,pt1)
    s = (1/2)*(a+b+c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

pts = [points[0],points[1],points[2]]
ans = triangle(pts[0],pts[1],pts[2])
try:
    for i in range(3,n):
        choice = [find_length(pts[0],points[i]),
                  find_length(pts[1],points[i]),
                  find_length(pts[2],points[i])]
        pts[choice.index(max(choice))] = points[i]
        ans += triangle(pts[0],pts[1],pts[2])
except:pass
print(round(ans,1))



import sys
input = sys.stdin.readline
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
points.append(points[0])
s1,s2 = 0,0
for i in range(n):
    s1 += points[i][0] * points[i+1][1]
    s2 += points[i][1] * points[i+1][0]
print(round(abs(s1-s2)/2,1))
