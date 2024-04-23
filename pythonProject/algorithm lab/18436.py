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

for i in range(len(tree) // 2):
    try:
        if tp[i] % 2 == 0:
            tree[i + lsi + 1] = [0, 1]
        elif tp[i] % 2 == 1:
            tree[i + lsi + 1] = [1, 0]
    except:
        tree[i + lsi + 1] = [0, 0]


def set_tree(i):
    while i != 1:
        tree[i // 2] = [tree[i][0] + tree[i - 1][0], tree[i][1] + tree[i - 1][1]]
        i -= 2


set_tree(len(tree) - 1)


def get_sum(s, e):
    answer = [0, 0]
    while s <= e:
        if s % 2 == 1:
            answer[0] += tree[s][0]
            answer[1] += tree[s][1]
            s += 1
        if e % 2 == 0:
            answer[0] += tree[e][0]
            answer[1] += tree[e][1]
            e -= 1
        s //= 2
        e //= 2
    return answer


def change_val(idx, val):
    if val % 2 == 1:
        tree[idx] = [1, 0]
    else:
        tree[idx] = [0, 1]
    while idx > 1:
        if idx % 2 == 0:
            tree[idx // 2] = [0, 0]
            tree[idx // 2][0] += tree[idx][0] + tree[idx + 1][0]
            tree[idx // 2][1] += tree[idx][1] + tree[idx + 1][1]
        else:
            tree[idx // 2] = [0, 0]
            tree[idx // 2][0] += tree[idx][0] + tree[idx - 1][0]
            tree[idx // 2][1] += tree[idx][1] + tree[idx - 1][1]
        idx //= 2


m = int(input())
for _ in range(m):
    q, s, e = map(int, input().split())
    if q == 2:
        s += lsi
        e += lsi
        print(get_sum(s, e)[1])
    elif q == 3:
        s += lsi
        e += lsi
        print(get_sum(s, e)[0])
    else:
        s += lsi
        change_val(s, e)