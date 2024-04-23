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
j = 1
for i in range(lsi + 1, len(tree)):
    try:
        tree[i] = [tp[j - 1], j]
    except:
        tree[i] = [math.inf, j]
    j += 1


def set_tree(i):
    while i != 1:
        if tree[i][0] < tree[i - 1][0]:
            tree[i // 2] = tree[i]
        else:
            tree[i // 2] = tree[i - 1]
        i -= 2


set_tree(len(tree) - 1)


def get_min(s, e):
    answer = [math.inf, 0]
    while s <= e:
        if s % 2 == 1:
            if answer[0] > tree[s][0]:
                answer = tree[s]
            elif answer[0] == tree[s][0]:
                answer = [answer[0], min(answer[1], tree[s][1])]
            s += 1
        if e % 2 == 0:
            if answer[0] > tree[e][0]:
                answer = tree[e]
            elif answer[0] == tree[e][0]:
                answer = [answer[0], min(answer[1], tree[e][1])]
            e -= 1
        s //= 2
        e //= 2
    return answer[1]


def change_val(idx, val):
    diff = val - tree[idx][0]
    tree[idx][0] = tree[idx][0] + diff
    while idx > 1:
        if idx % 2 == 0:
            if tree[idx][0] <= tree[idx + 1][0]:
                tree[idx // 2] = tree[idx]
            else:
                tree[idx // 2] = tree[idx + 1]
        else:
            if tree[idx][0] < tree[idx - 1][0]:
                tree[idx // 2] = tree[idx]
            else:
                tree[idx // 2] = tree[idx - 1]
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