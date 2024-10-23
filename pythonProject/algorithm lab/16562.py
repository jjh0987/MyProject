import sys
input = sys.stdin.readline
def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

n,m,k = map(int,input().split())
parent = [i for i in range(n)]
money = list(map(int,input().split()))
cycle = set()
parent_set = set(parent)
for _ in range(m):
    a, b = sorted(list(map(int, input().split())))
    a = find(a-1)
    b = find(b-1)
    if a in cycle and b in cycle:
        tp = max(a, b)
        cycle.remove(tp)
        try:
            parent_set.remove(tp)
        except:
            pass
    elif a in cycle and b in parent_set:
        parent_set.remove(b)
    elif a in parent_set and b in cycle:
        cycle.remove(b)
        cycle.add(a)
        parent_set.remove(a)
    if a == b:
        cycle.add(min(a, b))
    if a > b:
        parent[a] = b
        money[a] = min(money[a],money[b])
        money[b] = min(money[a],money[b])
        try:
            parent_set.remove(a)
        except:
            pass
    else:
        parent[b] = a
        money[a] = min(money[a],money[b])
        money[b] = min(money[a],money[b])
        try:
            parent_set.remove(b)
        except:
            pass
for i in cycle:
    if i in parent_set:
        try:
            parent_set.remove(i)
        except:
            pass
answer = 0
answer += sum([money[i] for i in cycle])
answer += sum([money[i] for i in parent_set])

if answer <= k:
    print(answer)
else:
    print('Oh no')