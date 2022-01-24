# fail : n^2 -> nlogn

n,m = map(int,input().split())

target = []
for i in range(m):
    flag,a,b = map(int, input().split())
    if flag == 0:
        for j in target:
            try:
                if a == b:
                    break
                elif (a in j) or (b in j):
                    j.union({a,b})
                else:
                    target.append({a,b})
                    break
            except:
                if len(target) == 0:
                    target.append({a,b})
                break
    else:
        if len(target) == 0:
            print('NO')
        else:
            for j in target:
                if (a in j) and (b in j):
                    print('YES')
                    break
                else:
                    print('NO')
                    break
