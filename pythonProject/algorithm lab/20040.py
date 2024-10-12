import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

flag = False
for i in range(m):
    a,b = map(int,input().split())
    a = find(a)
    b = find(b)
    if a == b:
        flag = True
        print(i+1)
        break
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

if not flag:
    print(0)