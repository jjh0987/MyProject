import sys
input = sys.stdin.readline
n,m = map(int,input().split())
edges = []
for _ in range(m):
    s,e,w = map(int,input().split())
    edges.append((s,e,w))

edges.sort(key=lambda x:x[2])
parent = [i for i in range(n)]
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    parent[x] = y
    return False

answer = 0
cnt = 0
for edge in edges:
    s,e,w = edge
    if not union(s-1,e-1):
        if cnt == n-2:
            print(answer)
            break
        answer += w
        cnt += 1