import sys
import math

input = sys.stdin.readline
n, m = map(int, input().split())


def get_tree_size(n):
    tr = 0
    while n != 0:
        n //= 2
        tr += 1
    return tr


tr = get_tree_size(n)
mintree = [math.inf] * (pow(2, tr + 1))
lsi = len(mintree) // 2 - 1
for i in range(lsi + 1, lsi + 1 + n):
    mintree[i] = int(input())

def set_tree(i):
    while i != 1:
        mintree[i // 2] = min(mintree[i - 1], mintree[i])
        i -= 2
set_tree(len(mintree) - 1)
maxtree = []
for i in range(len(mintree)):
    if i < len(mintree)//2:
        maxtree.append(0)
    else:
        if mintree[i] == math.inf:
            maxtree.append(0)
        else:
            maxtree.append(mintree[i])
def set_tree(i):
    while i != 1:
        maxtree[i // 2] = max(maxtree[i - 1], maxtree[i])
        i -= 2
set_tree(len(maxtree) - 1)

def get_min(s, e):
    answer = math.inf
    while s <= e:
        if s % 2 == 1:
            answer = min(answer, mintree[s])
            s += 1
        if e % 2 == 0:
            answer = min(answer, mintree[e])
            e -= 1
        s //= 2
        e //= 2
    return answer

def get_max(s, e):
    answer = 0
    while s <= e:
        if s % 2 == 1:
            answer = max(answer, maxtree[s])
            s += 1
        if e % 2 == 0:
            answer = max(answer, maxtree[e])
            e -= 1
        s //= 2
        e //= 2
    return answer

for _ in range(m):
    s, e = map(int, input().split())
    s += lsi
    e += lsi
    print(get_min(s, e), get_max(s, e))
