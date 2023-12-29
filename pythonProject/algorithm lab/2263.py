import sys
input = sys.stdin.readline
n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))

tree = [[0,0] for _ in range(n)]

def dfs(x):
    if x == -1:
        return
    dfs(tree[x][0])
    dfs(tree[x][1])
