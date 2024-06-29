import sys
input = sys.stdin.readline
v,e = map(int,input().split())

graph = {i:[] for i in range(1,v+1)}
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)