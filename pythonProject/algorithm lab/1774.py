import sys
import math
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y
        return True
    return False

n,m = map(int,input().split())
target = []
for i in range(1,n+1):
    x,y = map(int,input().split())
    target.append((x,y))

edges = []
for i in range(len(target)):
    for j in range(len(target)):
        if i != j:
            x1,y1 = target[i][0],target[i][1]
            x2,y2 = target[j][0],target[j][1]
            edges.append((math.sqrt((x1-x2)**2+(y1-y2)**2),i,j))

answer = 0
parent = [i for i in range(n)]
for _ in range(m):
    s,e = map(int,input().split())
    union(s-1,e-1)
    x1,y1 = target[s-1]
    x2,y2 = target[e-1]
    # answer += math.sqrt((x1-x2)**2 + (y1-y2)**2)

heapq.heapify(edges)
while edges:
    w, s, e = heapq.heappop(edges)
    if union(s, e):
        answer += w

print(format(answer, ".2f"))