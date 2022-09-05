import itertools


n,m = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()

marking = [0]
for idx in range(len(lst)):
    tp = []

    for i in range(0,idx):
        tp.append(lst[i])
    for i in range(idx+1,len(lst)):
        tp.append(lst[i])

    if marking == tp:
        continue

    marking = [i for i in tp]

    cnt = 0
    for i in list(itertools.combinations(sorted(tp),m-1)):
        if cnt == len(set(tp)):
            break

        print(lst[idx],end=' ')
        print(*i)

        cnt += 1





