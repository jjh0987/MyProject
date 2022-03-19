# 2578
bingo1 = []
for i in range(5):
    temp = list(map(int,input().split()))
    bingo1.append(temp)

bingo2 = []
for i in range(5):
    temp = []
    for j in bingo1:
        temp.append(j[i])
    bingo2.append(temp)

bingo3 = []
bingo4 = []
for i in range(5):
    for j in range(5):
        if i == j:
            bingo3.append(bingo1[i][j])
            if i+j == 4:
                bingo4.append(bingo1[i][j])
        elif i+j == 4:
            bingo4.append(bingo1[i][j])

bingo = bingo1 + bingo2 + [bingo3] + [bingo4]

temp = [list(map(int,input().split())) for _ in range(5)]
ans = []
for i in range(5):
    ans += temp[i]

for label in range(25):
    cnt = 0
    for bin in bingo:
        if ans[label] in bin:
            bin.pop(bin.index(ans[label]))
        if not bin:
            cnt += 1
    if cnt >= 3:
        print(label+1)
        break
# 11047
n,k = map(int,input().split())
money = [int(input()) for i in range(n)]
money.reverse()
cnt = 0
for coin in money:
    temp = 0
    if k - coin < 0:
        continue
    if k - coin >= 0:
        temp += k//coin
        k -= temp*coin

    cnt += temp
    if k == 0:
        break

print(cnt)

# 18870
import sys
n = int(input())
input = sys.stdin.readline
target = [i for i in list(map(int,input().split()))]
ls = sorted(list(set(target))) # dict
label = {ls[i]:i for i in range(len(ls))}

for i in target:
    print(label[i],end=' ')