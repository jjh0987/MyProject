# 2491
n = int(input())
num = [int(i) for i in input().split()]

ans1 = [1]*n
ans2 = [1]*n
for i in range(1,n):
    if num[i] >= num[i-1]:
        ans1[i] = max(ans1[i],ans1[i-1]+1)
    if num[i] <= num[i-1]:
        ans2[i] = max(ans2[i],ans2[i-1]+1)

print(max(max(ans1),max(ans2)))

# 2559
n,diff = map(int,input().split())
ls = [i for i in list(map(int,input().split()))]
temp = [0]*(n+1-diff)
temp[0] = sum(ls[0:diff])
for i in range(1,n):
    try:
        temp[i] = ls[i+diff-1] + temp[i-1] - ls[i-1]
    except:
        break
print(max(temp))

# 2628
x,y = map(int,input().split())
n = int(input())
chop = [list(map(int,input().split())) for _ in range(n)]

x = [0,x]
y = [0,y]
for i in chop:
    if i[0] == 1:
        x.append(i[1])
    else:
        y.append(i[1])
x.sort()
y.sort()
len_x = []
len_y = []
for i in range(1,len(x)):
    len_x.append(x[i]-x[i-1])
for i in range(1,len(y)):
    len_y.append(y[i]-y[i-1])

print(max(len_x)*max(len_y))