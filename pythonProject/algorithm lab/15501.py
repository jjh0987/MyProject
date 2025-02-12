import sys

input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
test = list(map(int, input().split()))

if n == 1:
    print('good puzzle')
else:
    check = dict()
    check[target[-1]] = {target[-2], target[0]}

    for i in range(n - 1):
        check[target[i]] = {target[i - 1], target[i + 1]}

    for i in range(n):
        try:
            if test[i - 1] not in check[test[i]] or test[i + 1] not in check[test[i]]:
                print('bad puzzle')
                break
        except:
            if test[i - 1] not in check[test[i]] or test[0] not in check[test[i]]:
                print('bad puzzle')
    else:
        print('good puzzle')
