n = 1000
s = 1001

if n > s:
    print([0])

target = [int(s/n)]*n
tar = s - sum(target)

i = -1
while tar > 0:
    target[i] += 1
    tar -= 1
    i -= 1

