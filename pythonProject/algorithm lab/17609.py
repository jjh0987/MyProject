import sys

input = sys.stdin.readline


def isP(x):
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False
    return True


T = int(input())
for _ in range(T):
    s = input().rstrip('\n')
    test = []
    if s[0] != s[-1]:
        test.append(s[1:])
        test.append(s[:-1])
    for i in range(1, len(s) // 2):
        if s[i] != s[-1 - i]:
            test.append(s[:i] + s[i + 1:])
            test.append(s[:-1 - i] + s[-i:])
            break
    flag = False
    for t in test:
        if isP(t):
            flag = True
            break
    if not test:
        print(0)
    else:
        if flag:
            print(1)
        else:
            print(2)