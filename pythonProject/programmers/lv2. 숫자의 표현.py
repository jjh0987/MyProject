n = 15

ans = 0
s = [int(i*(i+1)/2) for i in range(n+1)]

i = 0
j = 0
while i < n+1:
    if s[i]-s[j] < n:
        i += 1
    elif s[i]-s[j] == n:
        ans += 1
        i += 1
    else:
        j += 1

