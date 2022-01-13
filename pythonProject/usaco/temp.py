N = int(input())
b = list(map(int,input().split()))
perm = list(range(1,N+1))

a = []
i = 0
while i < N:
    j = 0
    a.append(perm[i])
    while j < len(b):
        a.append(b[j] - a[j])
        if a[j+1] > N or a[j+1] <= 0:
            a = []
            break
        j += 1
    if len(a) != 0:
        break
    i += 1

#output statement
temp = ''
i = 0
while i < N:
    temp += str(a[i]) + ' '
    i += 1
print(temp)

