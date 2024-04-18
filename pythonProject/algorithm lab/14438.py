import sys
import math

input = sys.stdin.readline
n = int(input())


def get_tree_size(n):
    tr = 0
    while n != 0:
        n //= 2
        tr += 1
    return tr


tr = get_tree_size(n)
tree = [math.inf] * (pow(2, tr + 1))
lsi = len(tree) // 2 - 1
tp = list(map(int, input().split()))
j = 0
for i in range(lsi + 1, lsi + 1 + n):
    try:
        tree[i] = tp[j]
        j += 1
    except:
        break


def set_tree(i):
    while i != 1:
        tree[i // 2] = min(tree[i], tree[i - 1])
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


def change_val(idx, val):
    diff = val - tree[idx]
    tree[idx] = tree[idx] + diff
    while idx > 1:
        if idx % 2 == 0:
            tree[idx // 2] = min(tree[idx], tree[idx + 1])
        else:
            tree[idx // 2] = min(tree[idx], tree[idx - 1])
        idx //= 2


m = int(input())
for _ in range(m):
    q, s, e = map(int, input().split())
    if q == 2:
        s += lsi
        e += lsi
        print(get_min(s, e))
    else:
        s += lsi
        change_val(s, e)