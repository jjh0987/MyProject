import sys
n = int(input())
l = []
li = [0]*8001
for i in range(n):
    l.append(int(sys.stdin.readline()))
l = sorted(l)
for i in l:
    li[i] += 1
print(round(sum(l)/n))
print(l[n//2])
l2 = []
i = 0
k = max(li)
while i < 8001:
    if li[i] == k:
        if i > 4000:
            l2.append(i-8001)
            i += 1
        else:
            l2.append(i)
            i += 1
    else:
        i += 1
x = sorted(l2)

if len(x) == 1:
    print(x[0])
else:
    print(x[1])

print(l[-1]-l[0])