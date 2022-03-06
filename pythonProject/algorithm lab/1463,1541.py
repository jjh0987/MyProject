# 1463
n = int(input())

dp = [0,0,1,1] # 1,2,3

for i in range(4,10**6+1):
    if i%2 == 0:
        temp1 = dp[int(i/2)] + 1
    else:
        temp1 = dp[i-1] + 1
    if i%3 == 0:
        temp2 = dp[int(i/3)] + 1
    else:
        temp2 = dp[i-1] + 1
    dp.append(min(temp1,temp2))
print(dp[n])

# 1541
target = input().split('-')
target = [i.lstrip('0') for i in target]
temp = []
for i in target:
    if not i:
        temp.append('0')
    else:
        temp.append(i)
target = [i.split('+') for i in temp]
temp = []
for i in target[1:]:
    for j in i:
        temp.append(int(j))

first = [int(i) for i in target[0]]

print(sum(first)-sum(temp))