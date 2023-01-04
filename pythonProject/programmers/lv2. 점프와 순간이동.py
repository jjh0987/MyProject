N = 5

ans = 0
while N != 0:
    if N%2 == 1:
        N -= 1
        ans += 1
    else:
        N = N//2