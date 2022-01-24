T = int(input())
i = 0
while i < T:
    test = input()
    for j in range(25):
        test = test.replace('()','')
        if len(test) == 0:
            print('YES')
            break
    if len(test) != 0:
        print('NO')
    i += 1
