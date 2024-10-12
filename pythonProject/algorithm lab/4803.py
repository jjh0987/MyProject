import sys
input = sys.stdin.readline
def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])
case = 1
while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    cycle = set()
    parent_set = set(parent[1:])

    for i in range(m):
        a,b = sorted(list(map(int,input().split())))
        a = find(a)
        b = find(b)
        if a in cycle and b in cycle:
            tp = max(a,b)
            cycle.remove(tp)
            try:
                parent_set.remove(tp)
            except:pass
        elif a in cycle and b in parent_set:
            parent_set.remove(b)
        elif a in parent_set and b in cycle:
            cycle.remove(b)
            cycle.add(a)
            parent_set.remove(a)
        if a == b:
            cycle.add(min(a,b))
        if a > b:
            parent[a] = b
            try:
                parent_set.remove(a)
            except:pass
        else:
            parent[b] = a
            try:
                parent_set.remove(b)
            except:pass
    for i in cycle:
        if i in parent_set:
            try:
                parent_set.remove(i)
            except:pass
    answer = len(parent_set)
    if answer <= 0:
        print(f'Case {case}: No trees.')
    elif answer == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {answer} trees.')
    case += 1
