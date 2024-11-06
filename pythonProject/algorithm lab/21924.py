import heapq
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,m = map(int,input().split())
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

edges = []
heapq.heapify(edges)
road = 0
for _ in range(m):
    s,e,w = map(int,input().split())
    heapq.heappush(edges,(w,s,e))
    road += w

answer = 0
parent = [i for i in range(n)]
flag = False
check = n-1
while edges:
    w,s,e = heapq.heappop(edges)
    if union(s-1,e-1):
        answer += w
        check -= 1
if check > 0:
    print(-1)
else:
    print(road-answer)