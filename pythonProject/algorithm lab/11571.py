import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    q, r = divmod(n, m)
    const = str(q)

    q, r = divmod(r, m)
    visited = dict()
    idx = 0
    cnt = 0
    while 1:
        q, r = divmod(r * 10, m)
        if (r,q) not in visited:
            visited[(r,q)] = idx
            idx += 1
        else:
            break
    cnt += visited[(r,q)]

    key = list(visited.keys())
    c = ''.join([str(i[1]) for i in key[:cnt]])
    nc = ''.join([str(i[1]) for i in key[cnt:]])
    print(f'{const}.{c}({nc})')