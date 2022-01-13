H,M = input().split()
H = int(H)
M = int(M) - 45

if M >= 0:
    print(H,M)
else:
    H = H - 1
    if H >= 0:
        print(H , M + 60)
    else:
        print(H + 24,M + 60)