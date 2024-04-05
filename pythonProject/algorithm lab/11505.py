import sys
import math

input = sys.stdin.readline
n, m, k = map(int, input().split())


def get_tree_size(n):
    tr = 0
    while n != 0:
        n //= 2
        tr += 1
    return tr


tr = get_tree_size(n)
tree = [0] * (pow(2, tr + 1))
lsi = len(tree) // 2 - 1
mod = 1000000007
for i in range(lsi + 1, lsi + 1 + n):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        tree[i // 2] = (tree[i - 1] * tree[i]) % mod
        i -= 2


set_tree(len(tree) - 1)


def change_val(idx, val):
    tree[idx] = val
    while idx > 1:
        if idx % 2 == 1:
            tree[idx // 2] = (tree[idx] * tree[idx - 1]) % mod
        elif idx % 2 == 0:
            tree[idx // 2] = (tree[idx] * tree[idx + 1]) % mod
        idx //= 2


def get_mul(s, e):
    answer = 1
    while s <= e:
        if s % 2 == 1:
            answer *= tree[s] % mod
            s += 1
        if e % 2 == 0:
            answer *= tree[e] % mod
            e -= 1
        s //= 2
        e //= 2
    return answer


for _ in range(m + k):
    q, s, e = map(int, input().split())
    if q == 1:
        s += lsi
        change_val(s, e)
    else:
        s += lsi
        e += lsi
        print(get_mul(s, e) % mod)
