n = int(input())
import string

alpha = list(string.ascii_uppercase)
up = {alpha[i]: i for i in range(26)}
uprev = {i: alpha[i] for i in range(26)}
up['.'] = -1
tree = [[] for _ in range(n)]
for _ in range(n):
    tar, l, r = input().split()
    tree[up[tar]] = [up[l], up[r]]


def dfs(x):
    print(uprev[x], end='')
    for i in tree[x]:
        if i > -1:
            dfs(i)


dfs(0)
print('')


def dfs(x):
    if x == -1:
        return
    dfs(tree[x][0])
    print(uprev[x], end='')
    dfs(tree[x][1])


dfs(0)
print('')


def dfs(x):
    if x == -1:
        return
    dfs(tree[x][0])
    dfs(tree[x][1])
    print(uprev[x], end='')


dfs(0)
