import sys
import string
import collections

input = sys.stdin.readline


def check(test, true):
    for i in true:
        if test[i] != true[i]:
            return False
    return True


T = int(input())
for _ in range(T):
    alpha = {i: 0 for i in string.ascii_lowercase}
    encoded = input().rstrip('\n')
    origin = input().rstrip('\n')
    len_origin = len(origin)
    origin = collections.Counter(origin)

    for i in encoded[:len_origin]:
        alpha[i] += 1

    if check(alpha, origin):
        print('YES')
    else:
        flag = False
        for i in range(len(encoded) - len_origin):
            alpha[encoded[len_origin + i]] += 1
            alpha[encoded[i]] -= 1
            if check(alpha, origin):
                print('YES')
                flag = True
                break
        if not flag:
            print('NO')        