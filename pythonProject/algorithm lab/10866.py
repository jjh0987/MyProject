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
tree = [0] * (pow(2, tr + 1))
lsi = len(tree) // 2 - 1
for i in range(lsi + 1, lsi + 1 + n):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        tree[i // 2] = min(tree[i - 1], tree[i])
        i -= 2


set_tree(len(tree) - 1)


def get_min(s, e):
    answer = math.inf
    while s <= e:
        if s % 2 == 1:
            answer = min(answer, tree[s])
            s += 1
        if e % 2 == 0:
            answer = min(answer, tree[e])
            e -= 1
        s //= 2
        e //= 2
    return answer


for _ in range(m):
    s, e = map(int, input().split())
    s += lsi
    e += lsi
    print(get_min(s, e))
