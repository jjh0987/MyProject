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
for i in range(lsi + 1, lsi + 1 + n):
    tree[i] = int(input())


def set_tree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1


set_tree(len(tree) - 1)


def change_val(idx, val):
    diff = val - tree[idx]
    while idx > 0:
        tree[idx] = tree[idx] + diff
        idx //= 2


def get_sum(s, e):
    answer = 0
    while s <= e:
        if s % 2 == 1:
            answer += tree[s]
            s += 1
        if e % 2 == 0:
            answer += tree[e]
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
        print(get_sum(s, e))
