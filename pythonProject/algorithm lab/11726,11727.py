# 11726
n = int(input())

if n == 1:
    start = [1]
elif n == 2:
    start = [2]
else:
    start = [1, 2]
    while len(start) != n:
        start.append(start[-1]+start[-2])

print(start[-1]%10007)


# 11726
n = int(input())

if n == 1:
    start = [1]
elif n == 2:
    start = [3]
else:
    start = [1, 3]
    while len(start) != n:
        start.append(start[-1]+2*start[-2])


print(start[-1]%10007)