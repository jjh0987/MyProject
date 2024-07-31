import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))
alpha = {'a', 'e', 'i', 'o', 'u'}
target = input().split()
target.sort()
import itertools

for tar in itertools.combinations(target, n):
    cnt0 = 0
    cnt1 = 0
    for i in tar:
        if i in alpha:
            cnt0 += 1
        else:
            cnt1 += 1
    if cnt0 >= 1 and cnt1 >= 2:
        print(''.join(tar))
