import sys
input = sys.stdin.readline
n = int(input())
graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(int(input())):
    x,y,m = map(int,input().split())
    graph[x][y] = m

graph

answer = [0]*(n+1)
start, end = map(int,input().split())


answer = []

# tp =
# while 1:
