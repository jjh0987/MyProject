# fail
n = int(input())
start = int(input())
idx = 0
if n == 1:
    print(start)
else:
    for i in range(1,501):
        target = list(map(int,input().split()))
        start += max(target[idx],target[idx+1])
        idx = target.index(max(target[idx],target[idx+1]))
        if i == n-1:
            break
7
10 15
18 max(11 16) 15
20 max(25 23) max(20 19) 19
..


n = int(input())
start = [int(input())]
if n == 1:
    print(start)
else:
    for i in range(1,501):
        target = list(map(int,input().split()))
        for j in range(len(target)):

        if i == n - 1:
            break