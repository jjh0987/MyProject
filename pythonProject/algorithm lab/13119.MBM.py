N,M,X = map(int,input().split())
H = list(map(int,input().split()))

temp2 = ''
for i in range(N,0,-1):
    temp = ''
    for j in range(M):
        if H[j] >= i:
            temp += chr(35)
        else:
            if j%3 == 2 and i < X:
                temp += chr(124)
            else:
                temp += chr(46)
    if i == X:
        temp2 = temp.replace(chr(35),chr(42))
        temp = temp2.replace(chr(46),chr(45))
    print(temp)