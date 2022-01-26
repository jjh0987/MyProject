N,M = map(int,input().split())
five_line = [5 ** i for i in range(1, 14)]
two_line = [2 ** i for i in range(1,31)]
five1 = 0
five2 = 0
five3 = 0
two1 = 0
two2 = 0
two3 = 0
for i in five_line:
    five1 += N//i
    five2 += M//i
    five3 += (N-M)//i
for i in two_line:
    two1 += N//i
    two2 += M//i
    two3 += (N-M)//i
print(min(five1-five2-five3,two1-two2-two3))