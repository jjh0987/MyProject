# 1074

n, i, j = map(int, input().split())
start = 0

while n > 1:
    diff = (2 ** n) * (2 ** n)
    division = 2 ** (n - 1)
    if n > 1:
        if i < division:
            if j < division:
                start = start
            else:
                j -= 2 ** (n - 1)
                start += int(1/4*diff)
        else:
            if j < division:
                start += int(2/4*diff)
                i -= 2 ** (n - 1)
            else:
                start += int(3/4*diff)
                i -= 2 ** (n - 1)
                j -= 2 ** (n - 1)
        n -= 1
if n == 1:
    if i == 0 and j == 0:
        print(start)
    elif i == 1 and j == 0:
        print(start + 2)
    elif i == 0 and j == 1:
        print(start + 1)
    else:
        print(start + 3)